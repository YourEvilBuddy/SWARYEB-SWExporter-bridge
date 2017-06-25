# !/usr/bin/python
import os, sys
import time
import hashlib
import threading
import tailhead

from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer


server = HTTPServer(('', 8999), SimpleHTTPRequestHandler)
thread = threading.Thread(target = server.serve_forever)
thread.daemon = True
try:
    thread.start()
    print 'Server successfully started'
except KeyboardInterrupt:
    server.shutdown()
    sys.exit(0)


## full path to <username>-<userid>-runs.csv in Summoners War Exporter Files-Directory
## For example: "C:\Users\exampleuser\Desktop\Summoners War Exporter Files\exampleuser-9890012-runs.csv"
runfilepath = ""

def log(logmsg):
    localtime = time.localtime(time.time())
    timestring = time.strftime ('%d.%m.%Y - %H:%M:%S')
    with open("bridge_log.txt", 'a') as f:
        f.write("%s %s\n"%(timestring,logmsg))
        f.close()
        print logmsg

def rune_eval(input):
    timestamp, area, result, runtime, mana, crystal, energy, drop, grade, sell_value, set, efficiency, slot, rarity, main_stat, prefix_stat, sub1, sub2, sub3, sub4, team1, team2, team3, team4, team5 = input.split(',')
    try:
        if drop == "Rune":
            if sub1 == "":
                sub1 = False				
            if sub2 == "":
                sub2 = False  
            if sub3 == "":
                sub3 = False  
            if sub4 == "":
                sub4 = False  
            if 'Legend' in rarity:
                if '6' in grade:
                    log(" ## Found 6*-Legendary: Keeping*")
                    return True
                elif '5' in grade:
                    if '%' in main_stat:
                        log(" ## Found 5*-Legendary with mainstat %: Keeping*")
                        return True
                    elif 'SPD' in main_stat:
                        log(" ## Found 5*-Legendary with mainstat SPD: Keeping*")
                        return True
                    elif '1' in slot or '3' in slot or '5' in slot:
                        log(" ## Found 5*-Legendary on 1/3/5: Keeping*")
                        return True
                    else:
                        log(" ## Found 5*-Legendary with mainstat flat: Selling")
                        return False
                else:
                    log(" ## Found unknown Legendary: Keeping")
                    return True
            elif 'Hero' in rarity:
                if '6' in grade:
                    if '%' in main_stat:
                        log(" ## Found 6*-Hero with mainstat %: Keeping")             
                        return True
                    elif 'SPD' in main_stat:                
                        log(" ## Found 6*-Hero with mainstat SPD: Keeping")                
                        return True
                    elif '1' in slot or '3' in slot or '5' in slot: 
                        log(" ## Found 6*-Hero on 1/3/5: Keeping")                
                        return True
                    else:                
                        log(" ## Found 6*-Hero with mainstat flat: Selling")                
                        return False
                else:
                    log(" ##Found 5*-Hero: Selling")
                    return False
            elif 'Rare' in rarity:
                if '6' in grade:
                    if '%' in main_stat:                
                        log(" ## Found 6*-Rare with mainstat %: Keeping")                
                        return True
                    elif 'SPD' in main_stat:                
                        log(" ## Found 6*-Rare with mainstat SPD: Keeping")                
                        return True
                    elif '1' in slot or '3' in slot or '5' in slot:         
                        if 'SPD' in sub1 or 'SPD' in sub2 or 'SPD' in sub3 or 'SPD' in sub4:
                            log(" ## Found 6*-Rare on 1/3/5 with SPD-Subs: Keeping")
                            return True
                        else:							
                            log(" ## Found 6*-Rare on 1/3/5: Selling")                
                            return False
                    else:                
                        log(" ## Found 6*-Rare with mainstat flat: Selling")                
                        return False
                else:
                    log(" ## Found 5*-Rare: Selling")
                    return False
            else:
                log(" ## Found Rune with unknown Rarity: Keeping")
                return True
        else:
            log(" ## No rune-drop - skipping")
            return norune
    except ImportError:
        log("Checkrune failed - keeping Rune")
        return True
		
		
		

	

def makehash(xy):
    string2hash = xy
    hash_object = hashlib.md5(string2hash.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig
	
def write_file(msg):
    localtime = time.localtime(time.time())
    timestring = time.strftime ('%d.%m.%Y - %H:%M:%S')
    hash = makehash(msg)
    keep_rune = rune_eval(msg)
    with open("runesell.txt", 'w') as f:
        f.write("%s %s\n"%(hash,keep_rune))
        f.close()
        print msg
	
for line in tailhead.follow_path(runfilepath):
	if line is not None:
		print(line)
		write_file(line)
	else:
		time.sleep(5)