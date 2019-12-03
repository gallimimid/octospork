import requests

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
