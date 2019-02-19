import requests

requests.packages.urllib3.disable_warnings()

ip_address = '10.130.19.4'

# Authenticate

url = 'https://{host}/rest/mbdetnrs/1.0/oauth2/token'.format(host=ip_address)

json = {'username':'admin','password':'reallysecurepassword','grant_type':'password','scope':'GUIAccess'}

response = requests.post(url, verify=False, json=json)
print(response)
access_token = response.json()['access_token']

print(access_token)

# Upgrade network card firmware
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/actions/upgrade'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

files = {'upgradeFile': open('Network-M2 1.5.1 firmware.img', 'rb')}

response = requests.post(url, verify=False, headers=headers, files=files)
print(response.status_code,response.headers)
