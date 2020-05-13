# Form implementation generated from reading ui file 'nGUI2.ui'
#
# Created: Fri Oct 19 17:46:26 2018
#      by: PyQt4 UI code generator 4.10.4
#
# Authors: Kushagra Shah, Ayush Mall

# Baseline Wandering Removal (HPF) -> Signal Conditioning (BPF) -> Signal Normalisation (Homomorphic Filtering) 
# Can plot spectrogram after every step. FFT and spectrogram plots more user friendly. 
# This is for the newer approach. 

#NEW start################################################################################################################
# Libraries included
from scipy.signal import butter,filtfilt
import matplotlib.pyplot as plt
import numpy as np
plt.ioff()
from Tkinter import *
import tkFileDialog
#NEW end##################################################################################################################
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(998, 501)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(380, 10, 301, 231))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 121, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 30, 113, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 110, 121, 31))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 70, 113, 31))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 110, 113, 31))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(250, 110, 31, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(250, 70, 31, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 150, 151, 31))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 190, 121, 34))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_8.setGeometry(QtCore.QRect(160, 150, 121, 34))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_10 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 190, 121, 34))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 250, 301, 181))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 191, 31))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(10, 100, 141, 31))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.pushButton_12 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_12.setGeometry(QtCore.QRect(160, 140, 121, 34))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_11 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_11.setGeometry(QtCore.QRect(160, 100, 121, 34))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_13 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_13.setGeometry(QtCore.QRect(30, 140, 121, 34))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.groupBox_6 = QtGui.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(690, 170, 301, 321))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_20 = QtGui.QLabel(self.groupBox_6)
        self.label_20.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_6)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 30, 161, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_21 = QtGui.QLabel(self.groupBox_6)
        self.label_21.setGeometry(QtCore.QRect(10, 70, 171, 31))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.groupBox_6)
        self.label_22.setGeometry(QtCore.QRect(10, 110, 171, 31))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_11.setGeometry(QtCore.QRect(190, 70, 91, 31))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_12.setGeometry(QtCore.QRect(190, 110, 91, 31))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.label_23 = QtGui.QLabel(self.groupBox_6)
        self.label_23.setGeometry(QtCore.QRect(10, 150, 171, 31))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_13.setGeometry(QtCore.QRect(190, 150, 91, 31))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.label_27 = QtGui.QLabel(self.groupBox_6)
        self.label_27.setGeometry(QtCore.QRect(160, 250, 61, 31))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.lineEdit_15 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_15.setGeometry(QtCore.QRect(162, 220, 131, 31))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_16.setGeometry(QtCore.QRect(10, 280, 131, 31))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.label_24 = QtGui.QLabel(self.groupBox_6)
        self.label_24.setGeometry(QtCore.QRect(10, 190, 61, 31))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_14.setGeometry(QtCore.QRect(10, 220, 131, 31))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.label_25 = QtGui.QLabel(self.groupBox_6)
        self.label_25.setGeometry(QtCore.QRect(160, 190, 61, 31))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.lineEdit_17 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_17.setGeometry(QtCore.QRect(160, 280, 131, 31))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.label_26 = QtGui.QLabel(self.groupBox_6)
        self.label_26.setGeometry(QtCore.QRect(10, 250, 61, 31))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(100, 440, 581, 51))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 200, 361, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(90, 30, 261, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 111, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 121, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 113, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 110, 113, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(250, 110, 31, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 190, 121, 34))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 190, 121, 34))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 121, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 150, 121, 34))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 361, 181))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 211, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 341, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(250, 20, 101, 34))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 100, 121, 34))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 140, 121, 34))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 140, 121, 34))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 121, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_28 = QtGui.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(20, 450, 70, 31))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(690, 10, 301, 161))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(160, 30, 61, 31))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(10, 90, 61, 31))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(160, 90, 61, 31))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_16 = QtGui.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(10, 30, 61, 31))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 120, 131, 31))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(162, 60, 131, 31))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_10.setGeometry(QtCore.QRect(160, 120, 131, 31))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

#NEW start################################################################################################################
# Initialising line edits and push buttons        
        global fname,order_hl,cutoff_hl,order_b,lowcut_b,highcut_b,nfft,noverlap,padding,filt_type,win_type
        global fftXmin,fftXmax,fftYmin,fftYmax,spXmin,spXmax,spYmin,spYmax
        fname='tIQdata_t57_1.txt'
        order_hl=2
        cutoff_hl=1000000
        order_b=1
        lowcut_b=1000000
        highcut_b=1600000
        nfft=3993
        noverlap=128
        padding=3993
        fftXmin=0
        fftXmax=5000000
        fftYmin='~'
        fftYmax='~'
        spXmin='~'
        spXmax='~'
        spYmin=-5000000
        spYmax=5000000
        filt_type='HighPass Filtered Signal'
        win_type='Hanning'
        self.lineEdit.setText(str(fname))
        self.lineEdit_2.setText(str(order_hl))
        self.lineEdit_3.setText(str(cutoff_hl))
        self.lineEdit_4.setText(str(order_b))
        self.lineEdit_5.setText(str(lowcut_b))
        self.lineEdit_6.setText(str(highcut_b))
        self.lineEdit_7.setText(str(fftXmin))
        self.lineEdit_8.setText(str(fftXmax))
        self.lineEdit_9.setText(str(fftYmin))
        self.lineEdit_10.setText(str(fftYmax))
        self.lineEdit_11.setText(str(nfft))
        self.lineEdit_12.setText(str(noverlap))
        self.lineEdit_13.setText(str(padding))
        self.lineEdit_14.setText(str(spXmin))
        self.lineEdit_15.setText(str(spXmax))
        self.lineEdit_16.setText(str(spYmin))
        self.lineEdit_17.setText(str(spYmax))
        self.comboBox.setCurrentIndex(self.comboBox.findText(filt_type, QtCore.Qt.MatchFixedString))
        self.comboBox_2.setCurrentIndex(self.comboBox_2.findText(win_type, QtCore.Qt.MatchFixedString))
        self.pushButton.clicked.connect(self.Browse)
        self.pushButton_2.clicked.connect(self.Original_time)
        self.pushButton_3.clicked.connect(self.Original_fft)
        self.pushButton_4.clicked.connect(self.Original_spec)
        self.pushButton_5.clicked.connect(self.Filtered_time)
        self.pushButton_6.clicked.connect(self.Filtered_fft)
        self.pushButton_7.clicked.connect(self.Filtered_spec)
        self.pushButton_8.clicked.connect(self.Conditioned_time)
        self.pushButton_9.clicked.connect(self.Conditioned_fft)
        self.pushButton_10.clicked.connect(self.Conditioned_spec)
        self.pushButton_11.clicked.connect(self.Normalised_time)
        self.pushButton_12.clicked.connect(self.Normalised_fft)
        self.pushButton_13.clicked.connect(self.Normalised_spec)

#NEW end##################################################################################################################
#NEW start################################################################################################################
# Functions linked to push buttons. Contains all the signal proceesing algorithms. 
# Most of the functions are derived from the older GUI. Few changes have been made in terms of variable and function names.    
    def Status_Bar(self,string):
        styledString="<span style=\" font-size:10pt; font-weight:400; color:#000000;\" > "
        styledString+=string
        styledString+="</span>"
        self.textBrowser.setHtml(styledString)
##########################################################################################################################
    def isnum(self,numstr):
        if(numstr.isdigit()):
            return float(numstr)
        elif((numstr.lstrip('+-')).isdigit()):
            return (-1)*float(numstr.lstrip('+-'))
        else:
            return -1
##########################################################################################################################
    def Browse(self):
        root = Tk()
        root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt file","*.txt"),("all files","*.*")))
        fname = root.filename
        self.lineEdit.setText(str(fname))
        root.destroy()
        root.mainloop()
        self.Status_Bar('Browse window closed')
##########################################################################################################################
    def Original_time(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Time plot
        self.Status_Bar('Do not press another button before closing the graph')
        plt.figure()
        plt.subplot(211)
        plt.plot(t,I,linewidth=0.6)
        plt.grid()
        plt.subplot(212)
        plt.plot(t,Q,linewidth=0.6)
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Original_fft(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #FFT Plot
        self.Status_Bar('Do not press another button before closing the graph')
        xmin = self.isnum((str(self.lineEdit_7.text())))
        xmax = self.isnum((str(self.lineEdit_8.text())))
        ymin = self.isnum((str(self.lineEdit_9.text())))
        ymax = self.isnum((str(self.lineEdit_10.text())))
        fft  = np.fft.fftshift(np.fft.fft((signal), n))
        fftf = np.fft.fftshift(np.fft.fftfreq(n, 1./fs))
        plt.figure()
        plt.plot(fftf, np.abs(fft),linewidth=0.6)
        if((xmin!=-1) and (xmax!=-1)):
            plt.xlim(float(xmin),float(xmax))
        if((ymin!=-1) and (ymax!=-1)):
            plt.ylim(float(ymin),float(ymax))
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Original_spec(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)

        #Spectrogram
        self.Status_Bar('Do not press another button before closing the graph')
        fft_pts = (int(self.lineEdit_11.text()))
        overlap_pts = (int(self.lineEdit_12.text()))
        pad = (int(self.lineEdit_13.text()))
        if(str(self.comboBox_2.currentText())=='Hanning'):
            windfn=np.hanning(fft_pts)
        if(str(self.comboBox_2.currentText())=='Blackman'):
            windfn=np.blackman(fft_pts)
        if(str(self.comboBox_2.currentText())=='Hamming'):
            windfn=np.hamming(fft_pts)
        if(str(self.comboBox_2.currentText())=='Bartlett'):
            windfn=np.bartlett(fft_pts)
        xmin = self.isnum((str(self.lineEdit_14.text())))
        xmax = self.isnum((str(self.lineEdit_15.text())))
        ymin = self.isnum((str(self.lineEdit_16.text())))
        ymax = self.isnum((str(self.lineEdit_17.text())))
        plt.figure()
        plt.specgram(signal,NFFT=fft_pts,Fs=fs,window=windfn,noverlap=overlap_pts,pad_to=pad,scale ='linear')
        if((xmin!=-1) and (xmax!=-1)):
            plt.xlim(float(xmin),float(xmax))
        if((ymin!=-1) and (ymax!=-1)):
            plt.ylim(float(ymin),float(ymax))
        plt.colorbar()
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Filtered_time(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #signal = signal - np.mean(signal)  

        #Filter: high and low
        order = (float(self.lineEdit_2.text()))  
        cutoff = (float(self.lineEdit_3.text()))
        if(str(self.comboBox.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low
        if(str(self.comboBox.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)

        #Time plot
        self.Status_Bar('Do not press another button before closing the graph')
        plt.figure()
        plt.subplot(211)
        plt.plot(t,filt_signal.real,linewidth=0.6)
        plt.grid()
        plt.subplot(212)
        plt.plot(t,filt_signal.imag,linewidth=0.6)
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Filtered_fft(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #signal = signal - np.mean(signal)  

        #Filter: high and low
        order = (float(self.lineEdit_2.text()))  
        cutoff = (float(self.lineEdit_3.text()))
        if(str(self.comboBox.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low
        if(str(self.comboBox.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)

        #FFT Plot
        self.Status_Bar('Do not press another button before closing the graph')
        xmin = self.isnum((str(self.lineEdit_7.text())))
        xmax = self.isnum((str(self.lineEdit_8.text())))
        ymin = self.isnum((str(self.lineEdit_9.text())))
        ymax = self.isnum((str(self.lineEdit_10.text())))
        fft  = np.fft.fftshift(np.fft.fft((filt_signal), n))
        fftf = np.fft.fftshift(np.fft.fftfreq(n, 1./fs))
        plt.figure()
        plt.plot(fftf, np.abs(fft),linewidth=0.6)
        if((xmin!=-1) and (xmax!=-1)):
            plt.xlim(float(xmin),float(xmax))
        if((ymin!=-1) and (ymax!=-1)):
            plt.ylim(float(ymin),float(ymax))
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Filtered_spec(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #signal = signal - np.mean(signal)  

        #Filter: high and low
        order = (float(self.lineEdit_2.text()))  
        cutoff = (float(self.lineEdit_3.text()))
        if(str(self.comboBox.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low
        if(str(self.comboBox.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)

        #Spectrogram
        self.Status_Bar('Do not press another button before closing the graph')
        fft_pts = (int(self.lineEdit_11.text()))
        overlap_pts = (int(self.lineEdit_12.text()))
        pad = (int(self.lineEdit_13.text()))
        if(str(self.comboBox_2.currentText())=='Hanning'):
            windfn=np.hanning(fft_pts)
        if(str(self.comboBox_2.currentText())=='Blackman'):
            windfn=np.blackman(fft_pts)
        if(str(self.comboBox_2.currentText())=='Hamming'):
            windfn=np.hamming(fft_pts)
        if(str(self.comboBox_2.currentText())=='Bartlett'):
            windfn=np.bartlett(fft_pts)
        xmin = self.isnum((str(self.lineEdit_14.text())))
        xmax = self.isnum((str(self.lineEdit_15.text())))
        ymin = self.isnum((str(self.lineEdit_16.text())))
        ymax = self.isnum((str(self.lineEdit_17.text())))
        plt.figure()
        plt.specgram(filt_signal,NFFT=fft_pts,Fs=fs,window=windfn,noverlap=overlap_pts,pad_to=pad,scale ='linear')
        if((xmin!=-1) and (xmax!=-1)):
            plt.xlim(float(xmin),float(xmax))
        if((ymin!=-1) and (ymax!=-1)):
            plt.ylim(float(ymin),float(ymax))
        plt.colorbar()
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Conditioned_time(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #signal = signal - np.mean(signal)  

        #Filter: high and low
        order = (float(self.lineEdit_2.text()))  
        cutoff = (float(self.lineEdit_3.text()))
        if(str(self.comboBox.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low
        if(str(self.comboBox.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)

        order = (float(self.lineEdit_4.text()))  
        fcutlow = (float(self.lineEdit_5.text()))
        fcuthigh = (float(self.lineEdit_6.text()))
        b,a = butter(order,[2*fcutlow,2*fcuthigh]/fs,'bandpass')
        cond_signal = filtfilt(b,a,filt_signal) 

        #Time plot
        self.Status_Bar('Do not press another button before closing the graph')
        plt.figure()
        plt.subplot(211)
        plt.plot(t,cond_signal.real,linewidth=0.6)
        plt.grid()
        plt.subplot(212)
        plt.plot(t,cond_signal.imag,linewidth=0.6)
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Conditioned_fft(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #signal = signal - np.mean(signal)  

        #Filter: high and low
        order = (float(self.lineEdit_2.text()))  
        cutoff = (float(self.lineEdit_3.text()))
        if(str(self.comboBox.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low
        if(str(self.comboBox.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)

        order = (float(self.lineEdit_4.text()))  
        fcutlow = (float(self.lineEdit_5.text()))
        fcuthigh = (float(self.lineEdit_6.text()))
        b,a = butter(order,[2*fcutlow,2*fcuthigh]/fs,'bandpass')
        cond_signal = filtfilt(b,a,filt_signal)

        #FFT Plot
        self.Status_Bar('Do not press another button before closing the graph')
        xmin = self.isnum((str(self.lineEdit_7.text())))
        xmax = self.isnum((str(self.lineEdit_8.text())))
        ymin = self.isnum((str(self.lineEdit_9.text())))
        ymax = self.isnum((str(self.lineEdit_10.text())))
        fft  = np.fft.fftshift(np.fft.fft((cond_signal), n))
        fftf = np.fft.fftshift(np.fft.fftfreq(n, 1./fs))
        plt.figure()
        plt.plot(fftf, np.abs(fft),linewidth=0.6)
        if((xmin!=-1) and (xmax!=-1)):
            plt.xlim(float(xmin),float(xmax))
        if((ymin!=-1) and (ymax!=-1)):
            plt.ylim(float(ymin),float(ymax))
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Conditioned_spec(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #signal = signal - np.mean(signal)  

        #Filter: high and low
        order = (float(self.lineEdit_2.text()))  
        cutoff = (float(self.lineEdit_3.text()))
        if(str(self.comboBox.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low
        if(str(self.comboBox.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)

        order = (float(self.lineEdit_4.text()))  
        fcutlow = (float(self.lineEdit_5.text()))
        fcuthigh = (float(self.lineEdit_6.text()))
        b,a = butter(order,[2*fcutlow,2*fcuthigh]/fs,'bandpass')
        cond_signal = filtfilt(b,a,filt_signal)

        #Spectrogram
        self.Status_Bar('Do not press another button before closing the graph')
        fft_pts = (int(self.lineEdit_11.text()))
        overlap_pts = (int(self.lineEdit_12.text()))
        pad = (int(self.lineEdit_13.text()))
        if(str(self.comboBox_2.currentText())=='Hanning'):
            windfn=np.hanning(fft_pts)
        if(str(self.comboBox_2.currentText())=='Blackman'):
            windfn=np.blackman(fft_pts)
        if(str(self.comboBox_2.currentText())=='Hamming'):
            windfn=np.hamming(fft_pts)
        if(str(self.comboBox_2.currentText())=='Bartlett'):
            windfn=np.bartlett(fft_pts)
        xmin = self.isnum((str(self.lineEdit_14.text())))
        xmax = self.isnum((str(self.lineEdit_15.text())))
        ymin = self.isnum((str(self.lineEdit_16.text())))
        ymax = self.isnum((str(self.lineEdit_17.text())))
        plt.figure()
        plt.specgram(cond_signal,NFFT=fft_pts,Fs=fs,window=windfn,noverlap=overlap_pts,pad_to=pad,scale ='linear')
        if((xmin!=-1) and (xmax!=-1)):
            plt.xlim(float(xmin),float(xmax))
        if((ymin!=-1) and (ymax!=-1)):
            plt.ylim(float(ymin),float(ymax))
        plt.colorbar()
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Normalised_time(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #signal = signal - np.mean(signal)  

        #Filter: high and low
        order = (float(self.lineEdit_2.text()))  
        cutoff = (float(self.lineEdit_3.text()))
        if(str(self.comboBox.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low
        if(str(self.comboBox.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)

        order = (float(self.lineEdit_4.text()))  
        fcutlow = (float(self.lineEdit_5.text()))
        fcuthigh = (float(self.lineEdit_6.text()))
        b,a = butter(order,[2*fcutlow,2*fcuthigh]/fs,'bandpass')
        cond_signal = filtfilt(b,a,filt_signal)

        #inst_amplitude = np.abs(cond_signal)
        inst_phase = np.unwrap(np.angle(cond_signal))
        #inst_freq = np.diff(inst_phase)/(2*np.pi)*fs
        #norm_signal = np.cos(inst_phase)
        norm_signal = np.cos(inst_phase) + 1j*np.sin(inst_phase)

        #Write data into file
        text_file = 'GoodM_py.txt'
        np.savetxt(text_file,(t,norm_signal.imag,norm_signal.real))

        #Time plot
        self.Status_Bar('Do not press another button before closing the graph')
        plt.figure()
        plt.subplot(211)
        plt.plot(t,norm_signal.real,linewidth=0.6)
        plt.grid()
        plt.subplot(212)
        plt.plot(t,norm_signal.imag,linewidth=0.6)
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Normalised_fft(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #signal = signal - np.mean(signal)  

        #Filter: high and low
        order = (float(self.lineEdit_2.text()))  
        cutoff = (float(self.lineEdit_3.text()))
        if(str(self.comboBox.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low
        if(str(self.comboBox.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)

        order = (float(self.lineEdit_4.text()))  
        fcutlow = (float(self.lineEdit_5.text()))
        fcuthigh = (float(self.lineEdit_6.text()))
        b,a = butter(order,[2*fcutlow,2*fcuthigh]/fs,'bandpass')
        cond_signal = filtfilt(b,a,filt_signal)

        #inst_amplitude = np.abs(cond_signal)
        inst_phase = np.unwrap(np.angle(cond_signal))
        #inst_freq = np.diff(inst_phase)/(2*np.pi)*fs
        #norm_signal = np.cos(inst_phase)
        norm_signal = np.cos(inst_phase) + 1j*np.sin(inst_phase)

        #FFT Plot
        self.Status_Bar('Do not press another button before closing the graph')
        xmin = self.isnum((str(self.lineEdit_7.text())))
        xmax = self.isnum((str(self.lineEdit_8.text())))
        ymin = self.isnum((str(self.lineEdit_9.text())))
        ymax = self.isnum((str(self.lineEdit_10.text())))
        fft  = np.fft.fftshift(np.fft.fft((norm_signal), n))
        fftf = np.fft.fftshift(np.fft.fftfreq(n, 1./fs))
        plt.figure()
        plt.plot(fftf, np.abs(fft),linewidth=0.6)
        if((xmin!=-1) and (xmax!=-1)):
            plt.xlim(float(xmin),float(xmax))
        if((ymin!=-1) and (ymax!=-1)):
            plt.ylim(float(ymin),float(ymax))
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
##########################################################################################################################
    def Normalised_spec(self):
        datafile = (str(self.lineEdit.text()))
        t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        #fs = np.round(10e6, -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #signal = signal - np.mean(signal)  

        #Filter: high and low
        order = (float(self.lineEdit_2.text()))  
        cutoff = (float(self.lineEdit_3.text()))
        if(str(self.comboBox.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low
        if(str(self.comboBox.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)

        order = (float(self.lineEdit_4.text()))  
        fcutlow = (float(self.lineEdit_5.text()))
        fcuthigh = (float(self.lineEdit_6.text()))
        b,a = butter(order,[2*fcutlow,2*fcuthigh]/fs,'bandpass')
        cond_signal = filtfilt(b,a,filt_signal)

        #inst_amplitude = np.abs(cond_signal)
        inst_phase = np.unwrap(np.angle(cond_signal))
        #inst_freq = np.diff(inst_phase)/(2*np.pi)*fs
        #norm_signal = np.cos(inst_phase)
        norm_signal = np.cos(inst_phase) + 1j*np.sin(inst_phase)

        #Spectrogram
        self.Status_Bar('Do not press another button before closing the graph')
        fft_pts = (int(self.lineEdit_11.text()))
        overlap_pts = (int(self.lineEdit_12.text()))
        pad = (int(self.lineEdit_13.text()))
        if(str(self.comboBox_2.currentText())=='Hanning'):
            windfn=np.hanning(fft_pts)
        if(str(self.comboBox_2.currentText())=='Blackman'):
            windfn=np.blackman(fft_pts)
        if(str(self.comboBox_2.currentText())=='Hamming'):
            windfn=np.hamming(fft_pts)
        if(str(self.comboBox_2.currentText())=='Bartlett'):
            windfn=np.bartlett(fft_pts)
        xmin = self.isnum((str(self.lineEdit_14.text())))
        xmax = self.isnum((str(self.lineEdit_15.text())))
        ymin = self.isnum((str(self.lineEdit_16.text())))
        ymax = self.isnum((str(self.lineEdit_17.text())))
        plt.figure()
        plt.specgram(norm_signal,NFFT=fft_pts,Fs=fs,window=windfn,noverlap=overlap_pts,pad_to=pad,scale ='linear')
        if((xmin!=-1) and (xmax!=-1)):
            plt.xlim(float(xmin),float(xmax))
        if((ymin!=-1) and (ymax!=-1)):
            plt.ylim(float(ymin),float(ymax))
        plt.colorbar()
        plt.grid()
        plt.show()
        self.Status_Bar('Another button can be pressed now')
#NEW_end##################################################################################################################


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.textBrowser.setHtml(_translate("Dialog", " Welcome", None)) 
        self.groupBox_3.setTitle(_translate("Dialog", "3 - Signal Conditioning", None))
        self.label_8.setText(_translate("Dialog", "Order (BP):", None))
        self.label_9.setText(_translate("Dialog", "Low-Cut (BP):", None))
        self.lineEdit_4.setText(_translate("Dialog", "1", None))
        self.label_11.setText(_translate("Dialog", "High-Cut (BP):", None))
        self.lineEdit_5.setText(_translate("Dialog", "1000000", None))
        self.lineEdit_6.setText(_translate("Dialog", "1600000", None))
        self.label_12.setText(_translate("Dialog", "Hz", None))
        self.label_10.setText(_translate("Dialog", "Hz", None))
        self.label_13.setText(_translate("Dialog", "Conditioned Signal:", None))
        self.pushButton_9.setText(_translate("Dialog", "FFT plot", None))
        self.pushButton_8.setText(_translate("Dialog", "Time plot", None))
        self.pushButton_10.setText(_translate("Dialog", "Spectrogram ", None))
        self.groupBox_4.setTitle(_translate("Dialog", "4 - Signal Normalisation", None))
        self.label_14.setText(_translate("Dialog", "Using the \'Good Method\'", None))
        self.label_15.setText(_translate("Dialog", "Normalised Signal:", None))
        self.pushButton_12.setText(_translate("Dialog", "FFT plot", None))
        self.pushButton_11.setText(_translate("Dialog", "Time plot", None))
        self.pushButton_13.setText(_translate("Dialog", "Spectrogram ", None))
        self.groupBox_6.setTitle(_translate("Dialog", "Spectogram Parameters", None))
        self.label_20.setText(_translate("Dialog", "Window Type:", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Hanning", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Blackman", None))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Hamming", None))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Bartlett", None))
        self.label_21.setText(_translate("Dialog", "No of FFT pts:", None))
        self.label_22.setText(_translate("Dialog", "No of overlapping pts:", None))
        self.lineEdit_11.setText(_translate("Dialog", "3993", None))
        self.lineEdit_12.setText(_translate("Dialog", "128", None))
        self.label_23.setText(_translate("Dialog", "No of padded pts:", None))
        self.lineEdit_13.setText(_translate("Dialog", "3993", None))
        self.label_27.setText(_translate("Dialog", "Y max:", None))
        self.lineEdit_15.setText(_translate("Dialog", "~", None))
        self.lineEdit_16.setText(_translate("Dialog", "-5000000", None))
        self.label_24.setText(_translate("Dialog", "X min:", None))
        self.lineEdit_14.setText(_translate("Dialog", "~", None))
        self.label_25.setText(_translate("Dialog", "X max:", None))
        self.lineEdit_17.setText(_translate("Dialog", "5000000", None))
        self.label_26.setText(_translate("Dialog", "Y min:", None))
        self.groupBox_2.setTitle(_translate("Dialog", "2 - Baseline Wandering Removal", None))
        self.label_3.setText(_translate("Dialog", "Filter: ", None))
        self.comboBox.setItemText(0, _translate("Dialog", "HighPass Filtered Signal", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Signal - LowPass Filtered Signal", None))
        self.label_4.setText(_translate("Dialog", "Order (LP/HP):", None))
        self.label_5.setText(_translate("Dialog", "Cutoff (LP/HP):", None))
        self.lineEdit_2.setText(_translate("Dialog", "2", None))
        self.lineEdit_3.setText(_translate("Dialog", "1000000", None))
        self.label_6.setText(_translate("Dialog", "Hz", None))
        self.pushButton_6.setText(_translate("Dialog", "FFT plot", None))
        self.pushButton_7.setText(_translate("Dialog", "Spectrogram ", None))
        self.label_7.setText(_translate("Dialog", "Filtered Signal:", None))
        self.pushButton_5.setText(_translate("Dialog", "Time plot", None))
        self.groupBox.setTitle(_translate("Dialog", "1 - Original Data", None))
        self.label.setText(_translate("Dialog", "Enter the data file address:", None))
        self.lineEdit.setText(_translate("Dialog", "tIQdata_t57_1.txt", None))
        self.pushButton.setText(_translate("Dialog", "Browse", None))
        self.pushButton_2.setText(_translate("Dialog", "Time plot", None))
        self.pushButton_3.setText(_translate("Dialog", "FFT plot", None))
        self.pushButton_4.setText(_translate("Dialog", "Spectrogram ", None))
        self.label_2.setText(_translate("Dialog", "Original Signal: ", None))
        self.label_28.setText(_translate("Dialog", "STATUS:", None))
        self.groupBox_5.setTitle(_translate("Dialog", "FFT Plot Parameters", None))
        self.label_17.setText(_translate("Dialog", "X max:", None))
        self.label_18.setText(_translate("Dialog", "Y min:", None))
        self.label_19.setText(_translate("Dialog", "Y max:", None))
        self.label_16.setText(_translate("Dialog", "X min:", None))
        self.lineEdit_9.setText(_translate("Dialog", "~", None))
        self.lineEdit_7.setText(_translate("Dialog", "0", None))
        self.lineEdit_8.setText(_translate("Dialog", "5000000", None))
        self.lineEdit_10.setText(_translate("Dialog", "~", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
