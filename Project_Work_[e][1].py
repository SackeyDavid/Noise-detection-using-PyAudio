#import statements, 
from __future__ import print_function         #this one isnt that important.Will explain latter
import numpy as np
        

#Function for generating the Vector Frequency
def generateVectorFrequency(rowFreq,colFreq):
    fs =32768   #Sampline rate
    t= 0.25     #time
    
    x_variables = np.linspace(0,t,t*fs)
    
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
    
#Creating a temporay array to store all the button vectors
button = np.zeros((12),np.ndarray)
#Storing all the vector frequency inside the temporary array
button[0] = generateVectorFrequency(200,900)
button[1] = generateVectorFrequency(200,1100)
button[2] = generateVectorFrequency(200,1300)
button[3] = generateVectorFrequency(400,900)
button[4] = generateVectorFrequency(400,1100)
button[5] = generateVectorFrequency(400,1300)
button[6] = generateVectorFrequency(600,900)
button[7] = generateVectorFrequency(600,1100)
button[8] = generateVectorFrequency(600,1300)
button[9] = generateVectorFrequency(800,900)
button[10]= generateVectorFrequency(800,1100)
button[11] = generateVectorFrequency(800,1300)

#creating a 12 by 12 array to store all the pairwise correlation
correlationTable =np.zeros((12,12))
#Filling the correlation Table
for row in xrange(12):
    for col in xrange(12):
        correlationTable[row][col] = cosXY(button[row],button[col])

#Displaying the correlation table
for row in xrange(12):
    for col in xrange(12):
        print("%.4f\t"% correlationTable[row][col],end ='')
    print("\n")