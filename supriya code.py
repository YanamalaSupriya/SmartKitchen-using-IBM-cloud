import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
#Provide your IBM Watson Device Credentials
organization = "985bj1"
deviceType = "ibmiot"
deviceId = "1001"
authMethod = "token"
authToken = "1234567890"
def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()
deviceCli.connect()
while True:
        length1=random.randint(0, 100)
        length2=random.randint(0, 100)
        length3=random.randint(0, 100)
        leakage=random.randint(0,30)
        data = { 'Jar1' : length1, 'Jar2': length2, 'Jar3': length3, 'Leakage': leakage }
        #notification alerts-----------------------------------------------------------
        
        if length1<=25:
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"W6zXBDk7wCu90PghITyr15YnHlKpaLbo3txQ8JVvR2djqeNmAc1ogy0ztbx76P8uTCDfrakjnshpGNcK","sender_id":"FSTSMS","message":"Jar1 is empty","language":"english","route":"p","numbers":"7993778964"}
                headers = {
                        'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        if length2<=25:
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"W6zXBDk7wCu90PghITyr15YnHlKpaLbo3txQ8JVvR2djqeNmAc1ogy0ztbx76P8uTCDfrakjnshpGNcK","sender_id":"FSTSMS","message":"Jar2 is empty","language":"english","route":"p","numbers":"7993778964"}
                headers = {
                        'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        if length3<=25:
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"W6zXBDk7wCu90PghITyr15YnHlKpaLbo3txQ8JVvR2djqeNmAc1ogy0ztbx76P8uTCDfrakjnshpGNcK","sender_id":"FSTSMS","message":"Jar3 is empty","language":"english","route":"p","numbers":"7993778964"}
                headers = {
                        'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        Exhaust_fan=0
        if leakage>=15:
                Exhaust_fan = 1
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"W6zXBDk7wCu90PghITyr15YnHlKpaLbo3txQ8JVvR2djqeNmAc1ogy0ztbx76P8uTCDfrakjnshpGNcK","sender_id":"FSTSMS","message":"Cylinder is leaking and Exhaust fan is ON","language":"english","route":"p","numbers":"7993778964"}
                headers = {
                        'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        
        #------------------------------------------------------------------------------
        def myOnPublishCallback():
            print ("Jar1 = %s m" % length1, "and Jar2 = %s m" % length2, "and Jar3 = %s m" % length3, "and Leakage = %s" % leakage )
        success = deviceCli.publishEvent("Parking", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        deviceCli.commandCallback = myCommandCallback
deviceCli.disconnect()








