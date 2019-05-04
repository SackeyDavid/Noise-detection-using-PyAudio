import matplotlib.pyplot as plt
import numpy as np
import pyaudio



def playSound(rowFreq,colFreq,time):
    fs = 32768
    
    x = np.linspace(0,time,time*fs)
    
    y_temp = [0.5*np.sin(2*np.pi*rowFreq*t)+0.5*np.sin(2*np.pi*colFreq*t) for t in x]
    y =np.array(y_temp,).astype(np.float32)

    p=pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paFloat32,channels =1,rate = 32768, output=True)
    
    stream.write(y)
    stream.close
    p.terminate
    
def plot(rowFreq,colFreq,time):
    fs = 32768
    x = np.linspace(0,time,time*fs)
    
    y_temp = [0.5*np.sin(2*np.pi*rowFreq*t)+0.5*np.sin(2*np.pi*colFreq*t) for t in x]
    y =np.array(y_temp,).astype(np.float32)
    
    plt.figure()
    plt.plot(x,y)
    plt.show
#END OF FUNCTIONS
    
#playing and ploting for each button:

#button 1
playSound(697,1209,0.25)
plot(697,1209,0.25)

#button 2
playSound(697,1336,0.25)
plot(697,1336,0.25)

#button 3
playSound(697,1477,0.25)
plot(697,1477,0.25)

#button 4
playSound(770,1209,0.25)
plot(770,1209,0.25)

#button 5
playSound(770,1336,0.25)
plot(770,1336,0.25)

#button 6
playSound(770,1477,0.25)
plot(770,1477,0.25)

#button 7
playSound(852,1209,0.25)
plot(852,1209,0.25)

#button 8
playSound(852,1336,0.25)
plot(852,1336,0.25)

#button 9
playSound(852,1477,0.25)
plot(852,1477,0.25)

#button *
playSound(941,1209,0.25)
plot(941,1209,0.25)

#button 0
playSound(941,1336,0.25)
plot(941,1336,0.25)

#button #
playSound(941,1477,0.25)
plot(941,1477,0.25)