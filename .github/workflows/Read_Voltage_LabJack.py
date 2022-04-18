from labjack import ljm
import statistics
from statistics import mean
import time
def read_voltage(Channel):
    handle = ljm.openS("ANY", "ANY", "ANY")  # Any device, Any connection, Any identifier
    info = ljm.getHandleInfo(handle)
    '''
    print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
      "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
      (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))
      '''
    result =[]
    name = "AIN"+str(Channel) 
    for i in range(10):
        res = ljm.eReadName(handle, name)
        result.append(res)
    ljm.close(handle)
    
    return( (name, mean(result),statistics.pstdev(result)))
    