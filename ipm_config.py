import requests, json, hashlib, hmac
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# suppress insecure warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# list of ip addresses you want to scan
ip_addresses = ['10.130.19.4']

# host and authentication
user_name = 'admin'
user_password = 'admin'
host = '10.130.19.15'

# request challenge
url = 'https://{host}:4680/server/user_srv.js?action=queryLoginChallenge'.format(host=host)
data = {'sessionID':'0'}
response = requests.post(url, data=data, verify=False)
json_data = json.loads(response.text)
challenge = json_data['challenge']

# create secret key
sha1_password = hashlib.sha1(user_password.encode()).hexdigest()
password = hmac.new(sha1_password.encode(), msg=challenge.encode(), digestmod=hashlib.sha1).hexdigest()

# request valid session id
url = 'https://{host}:4680/server/user_srv.js?action=loginUser'.format(host=host)
data = {'login':'admin','password':password,'sessionID':'0'}
response = requests.post(url, data=data, verify=False)
json_data = json.loads(response.text)
sessionID = json_data['sessionID']
print(sessionID)

# scan all ip addresses
for ip_address in ip_addresses:

    url = 'https://{host}:4680/server/discovery_srv.js?action=addressScan'.format(host=host)

    headers = {'Cookie': 'mc2LastLogin=admin; sessionID={sessionID}'.format(sessionID=sessionID)}

    authent = '{"xmlpdc":{"username":"admin","password":"admin","enabled":"true"},"snmpv1":{"communityName":"public","enabled":"false"},"snmpv3":{"username":"","securityLevel":0,"privMethod":"DES","privPassword":"","authMethod":"MD5","authPassword":"","enabled":"false"},"nut":{"enabled":"false"},"microsoftServer":{"username":"admin","password":"admin","enabled":"false"},"mqtt":{"username":"","password":"","enabled":"false"}}'

    data = {'address':ip_address,'authent':authent,'force':'false','sessionID':sessionID}

    response = requests.post(url, headers=headers, data=data, verify=False)

    print(response.status_code)
    print(ip_address)
