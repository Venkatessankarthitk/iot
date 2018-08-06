import obd
import subprocess
import json

obd.logger.setLevel(obd.logging.DEBUG)


connection = obd.OBD(fast=False)
while True:
    rpmcmd = obd.commands.RPM
    speedcmd = obd.commands.SPEED
    rpmresponse = connection.query(rpmcmd)
    speedresponse = connection.query(speedcmd)
    # content_type = "Content-Type: application/json"
    rpm_speed = {}
    rpm_speed['rpm']=str(rpmresponse.value.to("rpm"))
    rpm_speed['speed']=str(speedresponse.value.to("mph"))
    # rpm_speed = '"rpm":{0},"speed":{1}'.format(rpmresponse.value, speedresponse.value)
    cmdcurl = "curl -v -H 'Content-Type: application/json' -X POST -d '{0}' http://127.0.0.1:8000/api/data".format(json.load(rpm_speed))
    print(cmdcurl)
    uploading  = subprocess.Popen(cmdcurl, shell=True, stderr=subprocess.PIPE)
    # curl -v -H "Content-Type: application/json" -X POST -d '{"rpm":"24","speed":"25"}' http://127.0.0.1:8000/api/data
    print(rpmresponse.value)
    print(rpmresponse.value.to("rpm"))
    break
