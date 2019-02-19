import requests

requests.packages.urllib3.disable_warnings()

ip_address = '10.130.19.4'

# Authenticate

url = 'https://{host}/rest/mbdetnrs/1.0/oauth2/token'.format(host=ip_address)

json = {'username':'admin','password':'.drD!812','grant_type':'password','scope':'GUIAccess'}

response = requests.post(url, verify=False, json=json)
print(response)
access_token = response.json()['access_token']

print(access_token)

# Get the full API spec for LDAP provider
url = 'https://{host}/rest/mbdetnrs/1.0/accountsService/remoteAccounts/providers/ldap'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.status_code)
print(response.text)

# Get LDAP enabled status
url = 'https://{host}/rest/mbdetnrs/1.0/accountsService/remoteAccounts/providers/ldap/enabled'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.status_code)
print(response.text)

# Get LDAP baseAccess
url = 'https://{host}/rest/mbdetnrs/1.0/accountsService/remoteAccounts/providers/ldap/baseAccess'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.status_code)
print(response.text)

# Get LDAP request parameters
url = 'https://{host}/rest/mbdetnrs/1.0/accountsService/remoteAccounts/providers/ldap/requestParameters'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.status_code)
print(response.text)

# Get LDAP profile mapping
url = 'https://{host}/rest/mbdetnrs/1.0/accountsService/remoteAccounts/providers/ldap/profileMapping'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.status_code)
print(response.text)

# You can use PUT request for all of these endpoints and include JSON payload to update any of the parameters

# You need to add the LDAP certificate information if you are using SSL

# Add LDAP certificate authority
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/certificatesManager/services/ldap/clientsAuthentication/certificateAuthorities'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

json ={'certificate':  '-----BEGIN CERTIFICATE-----\nMIIDhzCCAm+gAwI [...] 1c+0UZwlNBS93/itGnen2qdxlk9g==\n-----END CERTIFICATE-----\n', 'format': 'PEM'}

response = requests.post(url, verify=False, headers=headers, json=json)
print(response.status_code)
print(response.text)

# Add LDAP trusted clients
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/certificatesManager/services/ldap/clientsAuthentication/trustedClients'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

json ={'certificate':  '-----BEGIN CERTIFICATE-----\nMIIDhzCCAm+gAwI [...] 1c+0UZwlNBS93/itGnen2qdxlk9g==\n-----END CERTIFICATE-----\n', 'format': 'PEM'}

response = requests.post(url, verify=False, headers=headers, json=json)
print(response.status_code)
print(response.text)
