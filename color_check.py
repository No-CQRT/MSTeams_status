import time
import subprocess
import os
from PIL import ImageGrab
import toml

# Verifica che il file config.toml esista / verify the presence of config.toml
if not os.path.exists("config.toml"):
    raise FileNotFoundError("Il file 'config.toml' non è stato trovato. Assicurati che esista nella stessa cartella dello script.")

# Carica la configurazione dal file config.toml / load config from config.toml
config = toml.load("config.toml")

# Estrae le variabili dal file di configurazione / extract variables from config file
PIXEL_COORDS = tuple(config["settings"]["pixel_coords"])
MQTT_TOPIC = config["settings"]["mqtt_topic"]
MQTT_HOST = config["settings"]["mqtt_host"]
MOSQUITTO_PATH = config["settings"]["mosquitto_path"]
SLEEP_TIME = config["settings"]["sleep_time"]

def get_pixel_color(coords):
    img = ImageGrab.grab()
    color = img.getpixel(coords)
    return '#{:02X}{:02X}{:02X}'.format(*color)

def publish_color(color_hex):
    cmd = f'"{MOSQUITTO_PATH}" -h {MQTT_HOST} -t {MQTT_TOPIC} -m "{color_hex}"'
    subprocess.run(cmd, shell=True)

def main():
    while True:
        color = get_pixel_color(PIXEL_COORDS)
        publish_color(color)
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
