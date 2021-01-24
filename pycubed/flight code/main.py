from pycubed import cubesat
import time
import testSD

class Satellite:
    states = ['start', 'detumble', 'normal', 'lowPower', 'criticallyLowPower']

    def __init__(self):
        self.currentState = 'start'

    # Returns readings from all of the sensors on PyCubed
    def collectBasicData(self):
        data = {
            "accel": cubesat.acceleration,
            "mag": cubesat.magnetic,
            "gyro": cubesat.gyro,
            "temp": cubesat.temperature,
            "vbatt": cubesat.battery_voltage,
            "ichrg": cubesat.charge_current,
            "vsys": cubesat.system_voltage,
            "isys": cubesat.current_draw
        }
        return data

    def collectPayload(self):
        pass

    def sendTelemetry(self, data):
        pass

    def deploy_antenna(self):
        pass

    def detumble(self):
        pass

    def isStable(self):
        pass

    # Method associated with the 'start' state
    def deploy(self):
        delay(20 minutes)
        deploy_antenna()
        detumble()

sat = Satellite()
while True:
    basicData = sat.collectBasicData()
    if !(sat.isStable()):
        sat.currentState = "detumble"
    elif basicData["vbatt"] > 3.7:
        sat.currentState = "normal"
    elif basicData["vbatt"] > 3.5:
        sat.currentState = "lowPower"
    elif basicData["vbatt"] < 3.3:
        sat.currentState = "criticallyLowPower"

    if sat.currentState == "detumble":
        sat.detumble()
    elif sat.currentState == "normal":
        payloadData = sat.collectPayload()
        sat.sendTelemetry(basicData)
        sat.sendTelemetry(payloadData)
    elif sat.currentState == "lowPower":
        payloadData = sat.collectPayload()
        sat.sendTelemetry(payloadData)
    elif sat.currentState == "criticallyLowPower":
        sat.sendTelemetry(basicData)
    delay(1)
