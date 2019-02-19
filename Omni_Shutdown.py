import argparse, requests

requests.packages.urllib3.disable_warnings()

parser = argparse.ArgumentParser(description='Shutdown Virtual Controller')
parser.add_argument('host')
parser.add_argument('-u','--username',required=True)
parser.add_argument('-p','--password',required=True)

args = parser.parse_args()

# Set the base URL for REST API requests.
url = 'https://{host}/api/'.format(host=args.host)

# Authenticate user and generate access token.
response = requests.post(url+'oauth/token', auth=('simplivity', ''), verify=False, data={
    'grant_type':'password',
    'username':args.username,
    'password':args.password})
access_token = response.json()['access_token']

# Add the access_token to the header.
headers = {'Authorization':  'Bearer ' + access_token, 'Accept' : 'application/vnd.simplivity.v1+json'}

# Issue a GET request: GET /hosts.
response = requests.get(url+'hosts', verify=False, headers=headers)

# Get hostId

for host in response.json()['hosts']:
    if  host['management_ip'] == args.host:
        hostId = host['id']

# Shut VC down

body = '{"ha_wait":"True"}'
headers['Content-Type'] = 'application/vnd.simplivity.v1+json'

response = requests.post(
    url + 'hosts/{hostId}/shutdown_virtual_controller'.format(hostId=hostId),
        verify=False,
        data=body,
        headers=headers
)

status = response.json()['shutdown_status']['status']

print(status)
"""
while status.endswith('IN_PROGRESS'):
    time.sleep(1)
    response = requests.get(
        url + '/hosts/{hostId}/virtual_controller_shutdown_status'.format(hostId=hostId),
        verify=False,
        headers=headers
    )
    print(status)
print(status)
"""
