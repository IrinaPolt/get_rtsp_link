# RTSP-links

## Description

The project includes the RTSP-links patterns for the most common producers of IP-cameras.
Having received the IP-adsress, username and password from console, the script identifies the producer with ONVIF.
With producer as a dictionary key, the script sorts through the given link patterns until the RTSP-stream can be started (by OpenCV) from working link

The 'auto-py-by-exe' allows to convert the project into .exe