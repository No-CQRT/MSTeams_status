import tkinter as tk
import subprocess
import os
import signal
import configparser
from datetime import datetime
import toml

# Verifica che il file config.toml esista / verify the presence of config.toml
if not os.path.exists("config.toml"):
    raise FileNotFoundError("Il file 'config.toml' non è stato trovato. Assicurati che esista nella stessa cartella dello script.")

# Carica la configurazione dal file config.toml / load config from config.toml
config = toml.load("config.toml")

# Estrae le variabili dal file di configurazione / extract variables from config file
INI_FILE = config["settings"]["ini_file"]
LOG_FILE = config["settings"]["log_file"] 
SCRIPT_NAME = config["settings"]["script_name"]

# add line to log
def write_log(message):
    with open(LOG_FILE, 'a') as log_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"[{timestamp}] {message}\n")
# save PID to ini
def save_pid(pid):
    config_ini = configparser.ConfigParser()
    config_ini['SERVICE'] = {'pid': str(pid)}
    with open(INI_FILE, 'w') as configfile:
        config_ini.write(configfile)
#read PID
def read_pid():
    if os.path.exists(INI_FILE):
        config_ini = configparser.ConfigParser()
        config_ini.read(INI_FILE)
        return int(config_ini['SERVICE']['pid'])
    return None

def clear_pid():
    if os.path.exists(INI_FILE):
        os.remove(INI_FILE)
# start service
def avvia_servizio():
    pid = read_pid()
    if pid is None:
        process = subprocess.Popen(["python", SCRIPT_NAME])
        save_pid(process.pid)
        write_log(f"Service started (PID: {process.pid})")
        aggiorna_bottoni(attivo=True)
#stop service
def ferma_servizio():
    pid = read_pid()
    if pid is not None:
        try:
            os.kill(pid, signal.SIGTERM)
            write_log(f"Service stopped (PID: {pid})")
        except Exception as e:
            write_log(f"Error stopping service: {e}")
        clear_pid()
        aggiorna_bottoni(attivo=False)

def aggiorna_bottoni(attivo):
    if attivo:
        btn_avvia.config(state='disabled', bg='darkgreen')
        btn_ferma.config(state='normal', bg='red')
    else:
        btn_avvia.config(state='normal', bg='green')
        btn_ferma.config(state='disabled', bg='darkred')

# Interfaccia grafica / GUI
root = tk.Tk()
root.title("GUI Control")
root.geometry("400x150")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)
# define gui buttons position and dimension, fonts and color
btn_avvia = tk.Button(frame, foreground="white", text="Start service", font=('Arial 10 bold italic'), width=20, height=2, command=avvia_servizio)
btn_avvia.grid(row=0, column=0, padx=10)

btn_ferma = tk.Button(frame, foreground="white", text="Stop Service", font=('Arial 10 bold italic'), width=20, height=2, command=ferma_servizio)
btn_ferma.grid(row=0, column=1, padx=10)

aggiorna_bottoni(attivo=read_pid() is not None)

root.mainloop()
