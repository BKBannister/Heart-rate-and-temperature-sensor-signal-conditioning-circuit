import numpy as np

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    ######################################
    time_stamp = 0
    t = 0
    avg_bpm = 0
    #steps = int(float(len(time))
    for i in range(len(time)):
        
        if(amplitude[i] > 4):
            avg_bpm +=  amplitude[i]
            t += 1
            time_stamp += 1
    time = time_stamp*0.001
    avg_bpm = avg_bpm*time
    bpm = (7.5188)*(avg_bpm) - 89.1
    bpm = round(bpm, 0)
        
    ######################################
        
    return t
        
