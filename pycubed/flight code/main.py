import time
import datetime
import board
import busio
import digitalio

from pycubed import cubesat
import testSD

class Satellite:
    states = ["start", "detumble", "normal", "lowPower", "criticallyLowPower"]

    def __init__(self):
        isDeployed = getDeployStatus()
        if (!isDeployed):
            deploy()
        self.currentState = "start"
        sd = SD()
        uart = busio.UART(board.TX, board.RX, baudrate=9600)

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
        if currentState == "normal":
            uart.write("START")
        elif currentState == "lowPower":
            uart.write("LOWPWR")
        elif currentState == "criticallyLowPower":
            uart.write("STOP")
        if uart.in_waiting:
            data = uart.read(32)
            data_string = "".join([chr(b) for b in data])
			return data_string

    def sendTelemetry(self, data):
        sd.save(data)

    def detumble(self):
        pass

    def isStable(self):
        pass

    def updateDeployStatus(self, status):
        save(['is_deployed:', status])

    def getDeployStatus(self)
        pass

    # Method associated with the 'start' state
    def deploy(self):
        delay(20 minutes)
        updateDeployStatus(status=1)
        detumble()

sat = Satellite()
while True:
    basicData = sat.collectBasicData()
    timestamp = datetime.datetime.now()
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
        sat.sendTelemetry([timestamp, basicData, payloadData])
    elif sat.currentState == "lowPower":
        payloadData = sat.collectPayload()
        sat.sendTelemetry([timestamp, payloadData])
    elif sat.currentState == "criticallyLowPower":
        sat.sendTelemetry([timestamp, basicData])
    delay(1)
