# SWARYEB-SWExporter-bridge
Since SW-Exporter does not have a working plugin-system at the moment, 
this little python-script will be used to bridge data between 
SW-Exporter and the SWAR-YEB-Ankulua-Bot.  
Rune-Sell-Logic is in this script instead of the botscript on  
android-device, to keep memoryfootprint on android-device low.

## Warning
The code in this repository is experimental. 

## Usage  
Edit variable ``runfilepath = ""`` in ``start_bridge.py`` with full path to ``<username>-<userid>-runs.csv`` in Summoners War Exporter Files-Directory.  <br />
For example: ``runfilepath = "C:\Users\exampleuser\Desktop\Summoners War Exporter Files\exampleuser-9890012-runs.csv"``  <br />
Run ``"run_bridge_windows.cmd"``  
  
Put IP of device running the bridge into Ankulua-Script-Options  <br />

Closing server: 
Keyboard Shortcut CTRL + C 

## Links
Summoner's War Exporter: https://github.com/Xzandro/sw-exporter  
SWAR-YEB Ankulua Bot: https://github.com/YourEvilBuddy/SWAR-YEB  
Ankulua: http://ankulua.boards.net/  