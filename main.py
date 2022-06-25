UPTIME_ROBOT_EXPORT_FILE = "./uptime-robot-export.csv"
UPTIME_KUMA_IMPORT_FILE = "./uptime-kuma.json"

import csv
import json

# change your default config here
kumaJSON = {
    "version": "1.17.1",
    "notificationList": [],
    "monitorList": [
    ]
}

with open(UPTIME_ROBOT_EXPORT_FILE, newline='') as uptimeRobotFile:
    websiteEntries = csv.reader(uptimeRobotFile, delimiter=',')

    for index, row in enumerate(websiteEntries):
       # change your default config here 
        website = {
            "id": index,
            "name": row[3],
            "url": row[4],
            "method": "GET",
            "hostname": None,
            "port": None,
            "maxretries": 2,
            "weight": 2000,
            "active": 1,
            "type": "http",
            "interval": 60,
            "retryInterval": 60,
            "keyword": None,
            "expiryNotification": False,
            "ignoreTls": False,
            "upsideDown": False,
            "maxredirects": 10,
            "accepted_statuscodes": [
                "200-299"
            ],
            "dns_resolve_type": "A",
            "dns_resolve_server": "1.1.1.1",
            "dns_last_result": None,
            "proxyId": None,
            "notificationIDList": {},
            "tags": [],
            "mqttUsername": "",
            "mqttPassword": "",
            "mqttTopic": "",
            "mqttSuccessMessage": "",
            "databaseConnectionString": "Server=<hostname>,<port>;Database=<your database>;User Id=<your user id>;Password=<your password>;Encrypt=<true/false>;TrustServerCertificate=<Yes/No>;Connection Timeout=<int>",
            "databaseQuery": None,
            "authMethod": None,
            "authWorkstation": None,
            "authDomain": None,
            "headers": None,
            "body": None,
            "basic_auth_user": None,
            "basic_auth_pass": None,
            "pushToken": None
        }
        kumaJSON['monitorList'].append(website);

exportFile = open(UPTIME_KUMA_IMPORT_FILE, 'w+')
exportFile.write(json.dumps(kumaJSON))
exportFile.close()
