#############################################################################################
#This code finds correlation between the data in two fixed files and appends it in a csv file 
#############################################################################################

#Import libraries
import numpy as np
import csv

#Load data from files
datafile1 = 'GoodM_mat.txt'
t1,Q1,I1 = np.loadtxt(datafile1)
datafile2 = 'GoodM_py.txt'
t2,Q2,I2 = np.loadtxt(datafile2)

#Store correlation values
corrt = np.corrcoef(t1,t2)
corrQ = np.corrcoef(Q1,Q2)
corrI = np.corrcoef(I1,I2)
q = corrQ[1,0]
i = corrI[1,0]

#Print correlation values
#print(corrt)
#print(corrQ)
#print(corrI)
print(q)
print(i)

'''
#Store correlation values
outputFile = open('correlation.csv', 'a')
with outputFile:
	outputWriter = csv.writer(outputFile)
	outputWriter.writerow(['linF-250us-5MSps-153p5cm',q,i])
outputFile.close()
'''