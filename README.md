<img width="897" height="505" alt="1754307306259" src="https://github.com/user-attachments/assets/21083b55-b4f6-4d3d-a709-6a4d208a92b1" />

# MSTeams_status
### A simple, and "just for fun", script that check the MSTeams status and send it to a MQTT broker

TL;DR
A Python script that read a pixel color from screen coordinates send it to a MQTT broker for later use.

# Why
Just for fun, of course, against the overcomplicated "official" procedure for getting presence status. (read my [linkedin post](https://www.linkedin.com/pulse/put-fun-back-computing-una-piccola-avventura-al-giorno-luca-perencin-texff/) about it)

# What and how

Just download the three files in a directory, configure the TOML file and run it!  

The main script, __color_check.py__ read a pixel color from the screen and send it to your favourite MQTT broker. After there you can use it to, for example, light up a RGB lamp with corrispondent color, or show it in a dashboard (like a Node-Red Dashboard) or... any other use you like it.
you can simply run it in a shell launching:
```
py.exe .\color_check.py
```
and stopping it with a CTRL-C (or start it as a batch, or as a service..)

The __control.py__ script open a GUI that show you two buttons, for starting and stopping the color check script. Just run:

```
py.exe .\control.py
```
<img width="515" height="235" alt="gui" src="https://github.com/user-attachments/assets/e230e2d4-c365-4af1-98fb-62acee650465" />   

you can easily open the gui, start the service and close it; the process PID is memorized in the .ini file. To stop the service, open it again and press the red button, that will kill the relative PID.

# Requirements and setup
Tested on Windows 11, Python 3.0, Mosquitto for Windows

> [!NOTE]
> - I'm **NOT a programmer**, so scripts can be unprecise, clumsy and "non professional", so everyone is welcome in case for any improvement
> - Be sure that you have the scripts and the TOML files in the same directory
> - Check and configure the TOML file for:
> - Pixel Coordinates (i've used [MPOS portable](https://github.com/Bluegrams/MPos) for checking my screen)
> - MQTT Topic and Broker (eg: the one from mqtt.eclipseprojects.io )
> - The Mosquitto_sub installation path
> - The sleep time (default 10 seconds) The interval between each message

> [!IMPORTANT]
> If you want to read the MSTeams status form the status icon, you need to force it visible on the application bar; go to settings and look for visible/not visible icons in the bar; set MS teams visible >position can change, according to you screen resolution, by best choice was to take the pixel upper the central one to be sure to have >all available colors (statuses) aligned and visible.  

<img width="295" height="279" alt="pixel" src="https://github.com/user-attachments/assets/114acce6-83a3-4143-a74a-528e9fec505b" />  

An example of what you can get is 

```
Color: #92C353 green available 
Color: #C4314B red not available
Color: #FDB913 yellow out of office
Color: #1E222B offline
```

## Final considerations:
As mentioned, is a "just for fun" project, maybe incomplete, maybe silly, but "it works"; Is a gently reminder to the old 
> If you can see or hear it, you can copy it

Happy hacking!

## To-Do
- add Authentication to MQTT.





