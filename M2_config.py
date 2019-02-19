import requests

requests.packages.urllib3.disable_warnings()

ip_address = '10.222.14.15'

# Authenticate

url = 'https://{host}/rest/mbdetnrs/1.0/oauth2/token'.format(host=ip_address)

json = {'username':'admin','password':'reallysecurepassword','grant_type':'password','scope':'GUIAccess'}

response = requests.post(url, verify=False, json=json)
print(response)
access_token = response.json()['access_token']

print(access_token)

# Get power distribution ids, typically this will be 1 for the 5P
url = 'http://{host}/rest/mbdetnrs/1.0/powerDistributions'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.text)

# Update global UPS settings
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/actions/restoreSettings'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

json = """{
	"version": "1.0",
	"features": {
		"accountService": {
			"data": {
				"version": "1.0",
				"dmeData": {
					"passwordRules": {
						"strength": {
							"minLength": 6,
							"minUpperCase": 0,
							"minLowerCase": 1,
							"minDigit": 1,
							"minSpecialCharacter": 0
						},
						"expiration": {
							"enabled": false,
							"afterDays": 90,
							"defaultAccountNeverExpires": true
						}
					},
					"lockoutRules": {
						"enabled": false,
						"threshold": 4,
						"defaultAccountNeverBlocks": true
					}
				}
			}
		},
		"card": {
			"data": {
				"version": "1.0",
				"dmeData": {
					"identification": {
						"name": "",
						"contact": "",
						"location": ""
					}
				}
			}
		},
		"date": {
			"data": {
				"version": "1.0",
				"dmeData": {
					"ntp": {
						"enabled": false,
						"getServersFromDhcp": false,
						"servers": {
							"preferredServer": "",
							"alternateServer": ""
						}
					},
					"timeZone": "Europe/Paris"
				}
			}
		},
		"email": {
			"data": {
				"version": "1.0",
				"dmeData": []
			}
		},
		"ldap": {
			"data": {
				"version": "1.1",
				"certificateData": [],
				"dmeData": {
					"enabled": false,
					"baseAccess": {
						"security": {
							"ssl": 3,
							"verifyTlsCert": true
						},
						"primary": {
							"name": "Primary",
							"hostname": "",
							"port": 636
						},
						"secondary": {
							"name": "",
							"hostname": "",
							"port": 0
						},
						"credentials": {
							"anonymousSearchBind": false,
							"searchUserDN": ""
						},
						"searchBase": {
							"searchBaseDN": "dc=example,dc=com"
						}
					},
					"requestParameters": {
						"userBaseDN": "ou=people,dc=example,dc=com",
						"userNameAttribute": "uid",
						"uidAttribute": "uidNumber",
						"groupBaseDN": "ou=group,dc=example,dc=com",
						"groupNameAttribute": "gid",
						"gidAttribute": "gidNumber"
					},
					"profileMapping": [
						{
							"remoteGroup": "",
							"profile": 0
						},
						{
							"remoteGroup": "",
							"profile": 0
						},
						{
							"remoteGroup": "",
							"profile": 0
						},
						{
							"remoteGroup": "",
							"profile": 0
						},
						{
							"remoteGroup": "",
							"profile": 0
						}
					]
				}
			}
		},
		"measure": {
			"data": {
				"version": "1.0",
				"dmeData": {
					"periodicity": 60
				}
			}
		},
		"mqtt": {
			"data": {
				"version": "1.1",
				"certificateData": []
			}
		},
		"network": {
			"data": {
				"version": "1.0",
				"dmeData": {
					"link": {
						"config": 0
					},
					"domain": {
						"settings": {
							"hostname": "ups-00-20-85-E9-69-6B",
							"mode": 1,
							"manual": {
								"domainName": "",
								"dns": {
									"preferredServer": "192.168.1.1",
									"alternateServer": "FD00::1"
								}
							}
						}
					},
					"ipv4": {
						"settings": {
							"enabled": true,
							"dhcpEnabled": true,
							"manual": {
								"address": "192.168.1.2",
								"subnetMask": "255.255.255.0",
								"gateway": "192.168.1.1"
							}
						}
					},
					"ipv6": {
						"settings": {
							"enabled": true,
							"addressing": {
								"mode": 1,
								"manual": {
									"address": "FD00::2",
									"prefixLength": 64,
									"gateway": "FD00::1"
								}
							}
						}
					}
				}
			}
		},
		"powerOutagePolicy": {
			"data": {
				"version": "1.0",
				"dmeData": [
					{
						"id": "eF1DIGKHWIeyKQuktyTOjg",
						"settings": {
							"localShutdownDuration": 120,
							"shutdownTriggers": {
								"powerOutage": {
									"enabled": false,
									"capacityLessThan": 0,
									"afterBackupTime": 300,
									"startShutdownBeforeEndOfBackup": 0,
									"endShutdownBeforeEndOfBackup": 30
								}
							},
							"restartTriggers": {
								"powerOutage": {
									"enabled": true,
									"minBatteryCapacity": 0
								}
							}
						}
					},
					{
						"id": "VWyNvTp3VPa6TvcRr9qhcg",
						"settings": {
							"localShutdownDuration": 120,
							"shutdownTriggers": {
								"powerOutage": {
									"enabled": false,
									"capacityLessThan": 0,
									"afterBackupTime": 300,
									"startShutdownBeforeEndOfBackup": 0,
									"endShutdownBeforeEndOfBackup": 30
								}
							},
							"restartTriggers": {
								"powerOutage": {
									"after": 3
								}
							}
						}
					},
					{
						"id": "tcnXWoxzWvOnTKpxpdUHvg",
						"settings": {
							"localShutdownDuration": 120,
							"shutdownTriggers": {
								"powerOutage": {
									"enabled": false,
									"capacityLessThan": 0,
									"afterBackupTime": 300,
									"startShutdownBeforeEndOfBackup": 0,
									"endShutdownBeforeEndOfBackup": 30
								}
							},
							"restartTriggers": {
								"powerOutage": {
									"after": 6
								}
							}
						}
					}
				]
			}
		},
		"remoteuser": {
			"data": {
				"version": "1.0",
				"dmeData": {
					"preferences": {
						"language": "en",
						"dateFormat": "m/d/Y",
						"timeFormat": 1,
						"temperatureUnit": 1
					}
				}
			}
		},
		"schedule": {
			"data": {
				"version": "1.0",
				"dmeData": []
			}
		},
		"smtp": {
			"data": {
				"version": "1.1",
				"certificateData": [],
				"dmeData": {
					"port": 25,
					"enabled": true,
					"server": "",
					"requireAuth": false,
					"user": "",
					"fromAddress": "ups@networkcard.com",
					"requireTls": true,
					"verifyTlsCert": false
				}
			}
		},
		"snmp": {
			"data": {
				"version": "1.0",
				"dmeData": {
					"enabled": false,
					"port": 161,
					"v1": {
						"enabled": false,
						"communities": {
							"readOnly": {
								"name": "public",
								"enabled": false
							},
							"readWrite": {
								"name": "private",
								"enabled": false
							}
						}
					},
					"v3": {
						"enabled": true,
						"users": [
							{
								"name": "readonly",
								"allowWrite": false,
								"enabled": false,
								"auth": {
									"enabled": true
								},
								"priv": {
									"enabled": true
								}
							},
							{
								"name": "readwrite",
								"allowWrite": true,
								"enabled": false,
								"auth": {
									"enabled": true
								},
								"priv": {
									"enabled": true
								}
							}
						]
					},
					"traps": {
						"receivers": []
					}
				}
			}
		},
		"webserver": {
			"data": {
				"version": "1.0",
				"dmeData": {
					"https": {
						"enabled": true,
						"port": 443
					}
				}
			}
		}
	},
	"firmwareVersion": "1.5.1"
}"""

response = requests.post(url, verify=False, headers=headers, json=json)
print(response.status_code,response.headers)

# Update UPS identification
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/identification'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

json = {"location":"location","contact":"contact","name":"name"}
# single parameter json is allowed at each endpoint
#json = {"location":"location1"}

response = requests.put(url, verify=False, headers=headers, json=json)
print(response)

# Get UPS identification
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/identification'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.text)

# Get UPS network parameters
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/networkService/networkInterfaces/1/'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.text)

# Get UPS network protocol parameters
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/networkService/protocols/'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.text)

# Get UPS time parameters
url = 'https://{host}/rest/mbdetnrs/1.0/managers/1/timeService/'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.text)

# Get UPS account parameters
url = 'https://{host}/rest/mbdetnrs/1.0/accountsService/accounts/1/'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
print(response.text)

# Get system logs
url = 'https://{host}/logs/system-logs-system.csv'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

response = requests.get(url, verify=False, headers=headers)
open('system-logs-system.csv', 'wb').write(response.content)
print(response.text)

# Change Admin password
url = 'https://{host}/rest/mbdetnrs/1.0/accountsService/accounts/1/'.format(host=ip_address)

headers = {'Authorization':  'Bearer ' + access_token}

json = {"credentials": {"password": "reallysecurepassword"}}

response = requests.put(url, verify=False, headers=headers, json=json)
print(response)