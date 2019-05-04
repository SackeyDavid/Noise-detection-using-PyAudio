
from __future__ import print_function
import numpy as np

#the function that adds noise to a particular sound vector
def addNoise(soundVector):
    length =len(soundVector)
    
    return soundVector + np.random.randn(length).astype(np.float32)
#End of function 'addNoise'
    
#Function for generating the Vector Frequency
def generateVectorFrequency(rowFreq,colFreq):
    fs =8192#32768   #Sampline rate
    t= (6800-1)*(1./fs)    #time
    
    x_variables = np.linspace(0,t,6800)
    
    #The sine function (that long function in the question)
    y_temp = [(0.5*np.sin(2*np.pi*rowFreq*time)+0.5*np.sin(2*np.pi*colFreq*time)) for time in x_variables]
    #Just converting y_temp, which is a list into array
    y_variable = np.array(y_temp).astype(np.float32)
    return y_variable
    
    
#Function for calculating the correlation
def cosXY(vectorX,vectorY):
    numerator = 0
    denominator = 0
    Xsquared=0
    Ysquared = 0
    cosXY=0
    
    for i in xrange(0,len(vectorX)):
        numerator+=  (vectorX[i]*vectorY[i])
        Xsquared += vectorX[i]*vectorX[i]
        Ysquared += vectorY[i]*vectorY[i]
    denominator =np.sqrt(Xsquared)*np.sqrt(Ysquared)
    
    cosXY =abs(numerator)/(denominator)
    return cosXY

#loading the given assumed frequecy(file) from the computer
Given_frequency = np.load("phone.npy")

#Creating an 11 vectors to store each row vector from the file given
vector = np.zeros(11,np.ndarray)

#Extracting the 11 vectors from the file into individual vectors
for row in xrange(11):
    temp = []
    for col in xrange(6800):
        temp.append(Given_frequency[row][col])
    vector[row] = np.array(temp).astype(np.float32)   
    
    
#Adding noise to the 11 vectors
for i in xrange(11):
    vector[i] = addNoise(vector[i])
    
#Creating a temporay array to store all the button vectors
button = np.zeros((12),np.ndarray)
#Storing all the vector frequency inside the temporary array
button[0] = generateVectorFrequency(697,1209)
button[1] = generateVectorFrequency(697,1336)
button[2] = generateVectorFrequency(697,1477)
button[3] = generateVectorFrequency(770,1209)
button[4] = generateVectorFrequency(770,1336)
button[5] = generateVectorFrequency(770,1477)
button[6] = generateVectorFrequency(852,1209)
button[7] = generateVectorFrequency(852,1336)
button[8] = generateVectorFrequency(852,1477)
button[9] = generateVectorFrequency(941,1209)
button[10]= generateVectorFrequency(941,1336)
button[11] = generateVectorFrequency(941,1477)

#creating a 11 by 12 array to store all the pairwise correlation
correlationTable =np.zeros((11,12))
#Filling the correlation Table
for row in xrange(11):
    for col in xrange(12):
        correlationTable[row][col] = cosXY(vector[row],button[col])

#Displaying the correlation table
for row in xrange(11):
    for col in xrange(12):
        print("%.4f\t"% correlationTable[row][col],end ='')
    print("\n")