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

# Export webserver certificate
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/certificatesManager/services/webserver/serverAuthentication/certificate/actions/export'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.post(url, verify=False, headers=headers)
print(response.status_code,response.headers,response.text)

# Generate CSR
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/certificatesManager/services/webserver/serverAuthentication/csr/actions/generate'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

json = {'params':{}}

response = requests.post(url, verify=False, headers=headers, json=json)
open('M2-web-server.csr', 'wb').write(response.content)
print(response.status_code,response.headers,response.text)

# Import new web server cert
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/certificatesManager/services/webserver/serverAuthentication/certificate/actions/export'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

json = {'certificate':  '-----BEGIN CERTIFICATE-----\nMIIDhzCCAm+gAwI [...] 1c+0UZwlNBS93/itGnen2qdxlk9g==\n-----END CERTIFICATE-----\n', 'format': 'PEM'}

response = requests.post(url, verify=False, headers=headers, json=json)

print(response.status_code,response.headers,response.text)
