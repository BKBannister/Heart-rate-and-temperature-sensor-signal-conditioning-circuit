import numpy as np

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    ######################################
    avg_temp = 0
    for i in range(len(time)):
        avg_temp +=  amplitude[i]
    avg_temp = avg_temp/len(time)
    temperature = (2.1108)*(avg_temp) + 31.8745 
    temperature = round(temperature, 0)
 
    ######################################
        
    return temperature
        
