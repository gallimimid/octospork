import requests
import time

requests.packages.urllib3.disable_warnings()

ip_address = '10.130.78.16'

url = 'http://{host}/Forms/app_upload_1'.format(host=ip_address)

# Upgrade network card firmware
files = {'file': open('NetworkMS_LB.bin', 'rb')}

response = requests.post(
    url,
    verify=False,
    auth=requests.auth.HTTPBasicAuth('admin', 'admin'),
    files=files
    )

print(response.status_code,response.headers)

while True:
    time.sleep(5)
    response = requests.get(
        'http://{host}/app_upload.htm'.format(host=ip_address),
        verify=False,
        auth=requests.auth.HTTPBasicAuth('admin', 'admin')
        )
    print(response.status_code,response.headers)
    if response.status_code != 200:
        break
