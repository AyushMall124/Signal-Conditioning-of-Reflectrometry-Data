# Form implementation generated from reading ui file '0_GUIF1.ui'
#
# Created: Sat Sep 08 19:37:36 2018
#      by: PyQt4 UI code generator 4.10.4
#
# Authors: Kushagra Shah, Ayush Mall

# Baseline Wandering Removal (HPF) -> Signal Normalisation (Threshold/Inverting) -> Signal Conditioning (BPF/WD/EMD)
# Has all the functionalities: default, load, save parameters. save graphs. 
# This is for the older approach. 

#NEW start################################################################################################################
# Libraries included
from scipy.signal import butter,filtfilt,lfilter,freqz
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
import pywt
import math
plt.ioff()  
#
from PyEMD import EMD
from Tkinter import *
import Tkconstants,tkFileDialog,tkMessageBox
import csv
import os
import time
import sys
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
        Dialog.resize(791, 879)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 751, 41))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_1 = QtGui.QGroupBox(Dialog)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 60, 361, 191))
        self.groupBox_1.setObjectName(_fromUtf8("groupBox_1"))
        self.label_1 = QtGui.QLabel(self.groupBox_1)
        self.label_1.setGeometry(QtCore.QRect(10, 30, 211, 31))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_1)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 341, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_1 = QtGui.QPushButton(self.groupBox_1)
        self.pushButton_1.setGeometry(QtCore.QRect(250, 20, 101, 34))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_1)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 141, 34))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_1)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 100, 191, 34))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_1)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 140, 191, 34))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 260, 361, 211))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox_1 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_1.setGeometry(QtCore.QRect(90, 30, 261, 31))
        self.comboBox_1.setObjectName(_fromUtf8("comboBox_1"))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 111, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_1 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 100, 113, 31))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 170, 113, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(130, 170, 31, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 80, 191, 34))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 120, 191, 34))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 480, 361, 331))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 30, 211, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 280, 161, 34))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 280, 161, 34))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 90, 113, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_23 = QtGui.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(10, 130, 131, 31))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(140, 130, 113, 31))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.lineEdit_15 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(140, 170, 113, 31))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.label_24 = QtGui.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(10, 170, 131, 31))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.groupBox_6 = QtGui.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(380, 60, 401, 561))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_8 = QtGui.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 70, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_6)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 30, 251, 31))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 70, 381, 151))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.label_9 = QtGui.QLabel(self.groupBox_7)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_7)
        self.label_10.setGeometry(QtCore.QRect(10, 70, 121, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 100, 113, 31))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 30, 113, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_11 = QtGui.QLabel(self.groupBox_7)
        self.label_11.setGeometry(QtCore.QRect(130, 100, 31, 31))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 100, 113, 31))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_12 = QtGui.QLabel(self.groupBox_7)
        self.label_12.setGeometry(QtCore.QRect(170, 70, 121, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_7)
        self.label_13.setGeometry(QtCore.QRect(290, 100, 31, 31))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 230, 381, 151))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.label_14 = QtGui.QLabel(self.groupBox_8)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_8)
        self.label_15.setGeometry(QtCore.QRect(210, 30, 111, 31))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_8)
        self.label_16.setGeometry(QtCore.QRect(10, 100, 61, 31))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 60, 113, 31))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_8.setGeometry(QtCore.QRect(210, 60, 113, 31))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 100, 211, 31))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.label = QtGui.QLabel(self.groupBox_8)
        self.label.setGeometry(QtCore.QRect(100, 30, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 390, 381, 111))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.label_18 = QtGui.QLabel(self.groupBox_9)
        self.label_18.setGeometry(QtCore.QRect(10, 70, 61, 31))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_11.setGeometry(QtCore.QRect(80, 70, 211, 31))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_10.setGeometry(QtCore.QRect(110, 30, 113, 31))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_17 = QtGui.QLabel(self.groupBox_9)
        self.label_17.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 510, 191, 34))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 510, 181, 34))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.groupBox_10 = QtGui.QGroupBox(Dialog)
        self.groupBox_10.setGeometry(QtCore.QRect(380, 630, 401, 181))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.label_19 = QtGui.QLabel(self.groupBox_10)
        self.label_19.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_10)
        self.comboBox_4.setGeometry(QtCore.QRect(120, 30, 141, 31))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.label_20 = QtGui.QLabel(self.groupBox_10)
        self.label_20.setGeometry(QtCore.QRect(10, 70, 141, 31))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.groupBox_10)
        self.label_21.setGeometry(QtCore.QRect(170, 70, 191, 31))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_12.setGeometry(QtCore.QRect(10, 100, 131, 31))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_13.setGeometry(QtCore.QRect(170, 100, 131, 31))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.pushButton_11 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 140, 161, 34))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_12.setGeometry(QtCore.QRect(180, 140, 211, 34))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.label_25 = QtGui.QLabel(self.groupBox_10)
        self.label_25.setGeometry(QtCore.QRect(290, 20, 70, 21))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_16.setGeometry(QtCore.QRect(270, 40, 121, 31))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(80, 820, 701, 51))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_22 = QtGui.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(10, 830, 71, 31))
        self.label_22.setObjectName(_fromUtf8("label_22"))
#NEW start################################################################################################################
# Menu Bar
        self.mainMenu = QtGui.QMenuBar(self.groupBox)
        self.mainMenu.setGeometry(QtCore.QRect(2, 2, 50, 30))
        self.mainMenu.setObjectName(_fromUtf8("mainmenu"))
        self.mainMenu = self.mainMenu.addMenu('File')
        self.mainMenu.addAction('Save parameters',self.Save_parameters,QtGui.QKeySequence("Ctrl+S"))
        self.mainMenu.addAction('Load parameters',self.Load_parameters,QtGui.QKeySequence("Ctrl+L"))
        self.mainMenu.addAction('Default parameters',self.Default_parameters,QtGui.QKeySequence("Ctrl+D"))
        self.mainMenu.addSeparator()
        self.mainMenu.addAction('Save all graphs',self.Save_all_graphs,QtGui.QKeySequence("Ctrl+G"))
        self.mainMenu.addAction('Exit',self.Exit)
#NEW end##################################################################################################################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

#NEW start################################################################################################################
# Initialising line edits and push buttons        
        global fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b
        global wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding
        global agc_type,peak_type,cond_type,win_type
        #fname='tIQdata_t57_1.txt'|order_hl=2|cutoff_hl=1000000|peak_inv_lim=100|order_b=1|lowcut_b=1000000|highcut_b=1600000
        #wavelet_no=4|no_of_lvls=10|add_wvlt='3,4,5'|no_of_imfs=10|add_emd='3,4,5'|...left...
        self.lineEdit.setText(str(fname))
        self.lineEdit_1.setText(str(order_hl))
        self.lineEdit_2.setText(str(cutoff_hl))
        self.lineEdit_3.setText(str(peak_inv_lim))
        self.lineEdit_4.setText(str(order_b))
        self.lineEdit_5.setText(str(lowcut_b))
        self.lineEdit_6.setText(str(highcut_b))
        self.lineEdit_7.setText(str(wavelet_no))
        self.lineEdit_8.setText(str(no_of_lvls))
        self.lineEdit_9.setText(str(add_wvlt))
        self.lineEdit_10.setText(str(no_of_imfs))
        self.lineEdit_11.setText(str(add_emd))
        self.lineEdit_12.setText(str(nfft))
        self.lineEdit_13.setText(str(noverlap))
        self.lineEdit_14.setText(str(max_thres))
        self.lineEdit_15.setText(str(min_thres))
        self.lineEdit_16.setText(str(padding))
        self.comboBox_1.setCurrentIndex(self.comboBox_1.findText(agc_type, QtCore.Qt.MatchFixedString))
        self.comboBox_2.setCurrentIndex(self.comboBox_2.findText(peak_type, QtCore.Qt.MatchFixedString))
        self.comboBox_3.setCurrentIndex(self.comboBox_3.findText(cond_type, QtCore.Qt.MatchFixedString))
        self.comboBox_4.setCurrentIndex(self.comboBox_4.findText(win_type, QtCore.Qt.MatchFixedString))
        self.pushButton_1.clicked.connect(self.Browse)
        self.pushButton_2.clicked.connect(self.IQ_time)
        self.pushButton_3.clicked.connect(self.Signal_time)
        self.pushButton_4.clicked.connect(self.Signal_fft)
        self.pushButton_5.clicked.connect(self.HLpass_time)
        self.pushButton_6.clicked.connect(self.HLpass_fft)
        self.pushButton_7.clicked.connect(self.AGC_time)
        self.pushButton_8.clicked.connect(self.AGC_fft)
        self.pushButton_9.clicked.connect(self.Reconstructed_time)
        self.pushButton_10.clicked.connect(self.Reconstructed_fft)
        self.pushButton_11.clicked.connect(self.Spectogram_signal)
        self.pushButton_12.clicked.connect(self.Spectogram_cond)
##########################################################################################################################
# Added functionalities. Does not have the signal processing algorithms    
    def Status_Bar(self,string):
        styledString="<span style=\" font-size:10pt; font-weight:400; color:#000000;\" > "
        styledString+=string
        styledString+="</span>"
        self.textBrowser.setHtml(styledString)
##########################################################################################################################
    def Exit(self):
    	global fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b
        global wavelet_no,no_of_lvlvs,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding
        global agc_type,peak_type,cond_type,win_type
        fname=str(self.lineEdit.text())
    	order_hl=str(self.lineEdit_1.text())
        cutoff_hl=str(self.lineEdit_2.text())
        peak_inv_lim=str(self.lineEdit_3.text())
        order_b=str(self.lineEdit_4.text())
        lowcut_b=str(self.lineEdit_5.text())
        highcut_b=str(self.lineEdit_6.text())
        wavelet_no=str(self.lineEdit_7.text())
        no_of_lvls=str(self.lineEdit_8.text())
        add_wvlt=str(self.lineEdit_9.text())
        no_of_imfs=str(self.lineEdit_10.text())
        add_emd=str(self.lineEdit_11.text())
        nfft=str(self.lineEdit_12.text())
        noverlap=str(self.lineEdit_13.text())
        max_thres=str(self.lineEdit_14.text())
        min_thres=str(self.lineEdit_15.text())
        padding=str(self.lineEdit_16.text())
        agc_type=str((self.comboBox_1.currentText()))
        peak_type=str((self.comboBox_2.currentText()))
        cond_type=str((self.comboBox_3.currentText()))
        win_type=str((self.comboBox_4.currentText()))      
        outputFile_d = open('F_Default_parameters.csv', 'w')
        with outputFile_d:
            outputWriter_d = csv.writer(outputFile_d)
            outputWriter_d.writerow([fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b,wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding,agc_type,peak_type,cond_type,win_type])
        outputFile_d.close()
        sys.exit()
##########################################################################################################################
    def Save_parameters(self):
    	global fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b
        global wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding
        global agc_type,peak_type,cond_type,win_type
        fname=str(self.lineEdit.text())
    	order_hl=str(self.lineEdit_1.text())
        cutoff_hl=str(self.lineEdit_2.text())
        peak_inv_lim=str(self.lineEdit_3.text())
        order_b=str(self.lineEdit_4.text())
        lowcut_b=str(self.lineEdit_5.text())
        highcut_b=str(self.lineEdit_6.text())
        wavelet_no=str(self.lineEdit_7.text())
        no_of_lvls=str(self.lineEdit_8.text())
        add_wvlt=str(self.lineEdit_9.text())
        no_of_imfs=str(self.lineEdit_10.text())
        add_emd=str(self.lineEdit_11.text())
        nfft=str(self.lineEdit_12.text())
        noverlap=str(self.lineEdit_13.text())
        max_thres=str(self.lineEdit_14.text())
        min_thres=str(self.lineEdit_15.text())
        padding=str(self.lineEdit_16.text())
        agc_type=str((self.comboBox_1.currentText()))
        peak_type=str((self.comboBox_2.currentText()))
        cond_type=str((self.comboBox_3.currentText()))
        win_type=str((self.comboBox_4.currentText()))
        root = Tk()
        root.filename = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt file","*.csv"),("all files","*.*")))
        file_parameter = root.filename
        outputFile = open(file_parameter+'.csv', 'w')
        with outputFile:
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow([fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b,wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding,agc_type,peak_type,cond_type,win_type])
        outputFile.close()
        root.destroy()
        root.mainloop()
        outputFile_d = open('F_Default_parameters.csv', 'w')
        with outputFile_d:
            outputWriter_d = csv.writer(outputFile_d)
            outputWriter_d.writerow([fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b,wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding,agc_type,peak_type,cond_type,win_type])
        outputFile_d.close()
        self.Status_Bar('Parameters saved')
##########################################################################################################################
    def Load_parameters(self):
    	global fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b
        global wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding
        global agc_type,peak_type,cond_type,win_type
        root = Tk()
        root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt file","*.csv"),("all files","*.*")))
        file_parameter = root.filename
        root.destroy()
        root.mainloop()
        loadFile = open(file_parameter)
        loadReader = csv.reader(loadFile)
        loadData = list(loadReader)
        fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b,wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding,agc_type,peak_type,cond_type,win_type=loadData[0]
        self.lineEdit.setText(str(fname))
        self.lineEdit_1.setText(str(order_hl))
        self.lineEdit_2.setText(str(cutoff_hl))
        self.lineEdit_3.setText(str(peak_inv_lim))
        self.lineEdit_4.setText(str(order_b))
        self.lineEdit_5.setText(str(lowcut_b))
        self.lineEdit_6.setText(str(highcut_b))
        self.lineEdit_7.setText(str(wavelet_no))
        self.lineEdit_8.setText(str(no_of_lvls))
        self.lineEdit_9.setText(str(add_wvlt))
        self.lineEdit_10.setText(str(no_of_imfs))
        self.lineEdit_11.setText(str(add_emd))
        self.lineEdit_12.setText(str(nfft))
        self.lineEdit_13.setText(str(noverlap))
        self.lineEdit_14.setText(str(max_thres))
        self.lineEdit_15.setText(str(min_thres))
        self.lineEdit_16.setText(str(padding))
        self.comboBox_1.setCurrentIndex(self.comboBox_1.findText(agc_type, QtCore.Qt.MatchFixedString))
        self.comboBox_2.setCurrentIndex(self.comboBox_2.findText(peak_type, QtCore.Qt.MatchFixedString))
        self.comboBox_3.setCurrentIndex(self.comboBox_3.findText(cond_type, QtCore.Qt.MatchFixedString))
        self.comboBox_4.setCurrentIndex(self.comboBox_4.findText(win_type, QtCore.Qt.MatchFixedString))
        loadFile.close()
        self.Status_Bar('Parameters loaded')
##########################################################################################################################
    def Default_parameters(self):
    	global fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b
        global wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding
        global agc_type,peak_type,cond_type,win_type
        fname='tIQdata_t57_1.txt'
        order_hl=2
        cutoff_hl=1000000
        peak_inv_lim=100
        order_b=1
        lowcut_b=1000000
        highcut_b=1600000
        wavelet_no=4
        no_of_lvls=10
        add_wvlt='3,4,5'
        no_of_imfs=10
        add_emd='3,4,5'
        nfft=3993
        noverlap=128
        max_thres=0.02
        min_thres=-0.02
        padding=3993
        agc_type='Signal - LowPass Filtered Signal'
        peak_type='With Threshold (Our Method)'
        cond_type='BandPass Filter'
        win_type='Hanning'
        self.lineEdit.setText(str(fname))
        self.lineEdit_1.setText(str(order_hl))
        self.lineEdit_2.setText(str(cutoff_hl))
        self.lineEdit_3.setText(str(peak_inv_lim))
        self.lineEdit_4.setText(str(order_b))
        self.lineEdit_5.setText(str(lowcut_b))
        self.lineEdit_6.setText(str(highcut_b))
        self.lineEdit_7.setText(str(wavelet_no))
        self.lineEdit_8.setText(str(no_of_lvls))
        self.lineEdit_9.setText(str(add_wvlt))
        self.lineEdit_10.setText(str(no_of_imfs))
        self.lineEdit_11.setText(str(add_emd))
        self.lineEdit_12.setText(str(nfft))
        self.lineEdit_13.setText(str(noverlap))
        self.lineEdit_14.setText(str(max_thres))
        self.lineEdit_15.setText(str(min_thres))
        self.lineEdit_16.setText(str(padding))
        self.comboBox_1.setCurrentIndex(self.comboBox_1.findText('Signal - LowPass Filtered Signal', QtCore.Qt.MatchFixedString))
        self.comboBox_2.setCurrentIndex(self.comboBox_2.findText('With Threshold (Our Method)', QtCore.Qt.MatchFixedString))
        self.comboBox_3.setCurrentIndex(self.comboBox_3.findText('BandPass Filter', QtCore.Qt.MatchFixedString))
        self.comboBox_4.setCurrentIndex(self.comboBox_4.findText('Hanning', QtCore.Qt.MatchFixedString))
        self.Status_Bar('Default Parameters loaded')
##########################################################################################################################
    def Save_all_graphs(self):
    	global fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b
        global wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding
        global agc_type,peak_type,cond_type,win_type
        global flag
        localtime = time.strftime("%d.%m.%Y-%H.%M.%S")
        if not os.path.exists(localtime):
            os.makedirs(localtime)
        flag=0
        self.IQ_time().savefig(localtime+"/IQ_time.png")
        self.Signal_time().savefig(localtime+"/Signal_time.png")
        self.Signal_fft().savefig(localtime+"/Signal_fft.png")
        self.HLpass_time().savefig(localtime+"/HLpass_time.png")
        self.HLpass_fft().savefig(localtime+"/HLpass_fft.png")
        self.AGC_time().savefig(localtime+"/AGC_time.png")
        self.AGC_fft().savefig(localtime+"/AGC_fft.png")
        self.Reconstructed_time().savefig(localtime+"/Reconstructed_time.png")
        self.Reconstructed_fft().savefig(localtime+"/Reconstructed_fft.png")
        self.Spectogram_signal().savefig(localtime+"/Spectogram_signal.png")
        self.Spectogram_cond().savefig(localtime+"/Spectogram_cond.png")
        plt.close('all')
        flag=1
        fname=str(self.lineEdit.text())
    	order_hl=str(self.lineEdit_1.text())
        cutoff_hl=str(self.lineEdit_2.text())
        peak_inv_lim=str(self.lineEdit_3.text())
        order_b=str(self.lineEdit_4.text())
        lowcut_b=str(self.lineEdit_5.text())
        highcut_b=str(self.lineEdit_6.text())
        wavelet_no=str(self.lineEdit_7.text())
        no_of_lvls=str(self.lineEdit_8.text())
        add_wvlt=str(self.lineEdit_9.text())
        no_of_imfs=str(self.lineEdit_10.text())
        add_emd=str(self.lineEdit_11.text())
        nfft=str(self.lineEdit_12.text())
        noverlap=str(self.lineEdit_13.text())
        max_thres=str(self.lineEdit_14.text())
        min_thres=str(self.lineEdit_15.text())
        padding=str(self.lineEdit_16.text())
        agc_type=str((self.comboBox_1.currentText()))
        peak_type=str((self.comboBox_2.currentText()))
        cond_type=str((self.comboBox_3.currentText()))
        win_type=str((self.comboBox_4.currentText()))
        outputFile = open(localtime+"/parameters.csv", 'w')
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow(['fname','order_hl','cutoff_hl','peak_inv_lim','order_b','lowcut_b','highcut_b','wavelet_no','no_of_lvls','add_wvlt','no_of_imfs','add_emd','nfft','noverlap','max_thres','min_thres','padding','agc_type','peak_type','cond_type','win_type'])
        outputWriter.writerow([fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b,wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding,agc_type,peak_type,cond_type,win_type])
        outputFile.close() 
        self.Status_Bar('All graphs saved')
##########################################################################################################################
    def Plot_time(self,x_var,y_var,plot_label,graph_title):
    	self.Status_Bar('Do not press another button before closing the graph')
    	fig = plt.figure(figsize=(10, 8))
        plt.plot(x_var, y_var, label=plot_label)
        plt.xlabel('Time', fontsize=14)
        plt.ylabel('Amplitude', fontsize=14)
        plt.title(graph_title)
        plt.grid()
        plt.legend()
        if(flag==1):
        	plt.show()
        	self.Status_Bar('Another button can be pressed now')
        return fig
##########################################################################################################################
    def Plot_fft(self,n,fs,y_var,plot_label,graph_title):
    	self.Status_Bar('Do not press another button before closing the graph')
    	fft  = np.fft.fftshift(np.fft.fft((y_var), n))
        fftf = np.fft.fftshift(np.fft.fftfreq(n, 1./fs))
        scale = 1e3
        fftf = fftf/scale
        xlim = 5000
    	fig = plt.figure(figsize=(10, 8))
        plt.plot(fftf, np.abs(fft), label=plot_label)
        plt.xlim(0, xlim)
        plt.xticks(np.arange(0, xlim+1, xlim/5))
        plt.xlabel('Frequency (KHz)', fontsize=14)
        plt.ylabel('Amplitude', fontsize=14)
        plt.title(graph_title)
        plt.grid()
        plt.legend()
        if(flag==1):
        	plt.show()
        	self.Status_Bar('Another button can be pressed now')
        return fig
#NEW end##################################################################################################################
#NEW start################################################################################################################
# Functions linked to push buttons. Contains all the signal processig algorithms.  
    def Browse(self):
    	root = Tk()
        root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt file","*.txt"),("all files","*.*")))
        fname = root.filename
        self.lineEdit.setText(str(fname))
        root.destroy()
        root.mainloop()
        self.Status_Bar('Browse window closed')
##########################################################################################################################
    def IQ_time(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        #I = I/np.max(I)
        #Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Time plot
        self.Status_Bar('Do not press another button before closing the graph')
        fig = plt.figure(figsize=(10, 8))
        plt.subplot(211)
        plt.plot(t, I,'b', label='I')
        plt.xlabel('Time', fontsize=14)
        plt.ylabel('Amplitude', fontsize=14)
        plt.title('I vs time')
        plt.grid()
        plt.legend()
        plt.subplot(212)
        plt.plot(t, Q,'g', label='Q')
        plt.xlabel('Time', fontsize=14)
        plt.ylabel('Amplitude', fontsize=14)
        plt.title('Q vs time')
        plt.grid()
        plt.legend()
        if(flag==1):
        	plt.show()
        	self.Status_Bar('Another button can be pressed now')
        return fig
##########################################################################################################################
    def Signal_time(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        I = I/np.max(I)
        Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #Time Plot
        fig = self.Plot_time(t,signal,'Original Signal','Signal time plot')
        return fig
##########################################################################################################################
    def Signal_fft(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        I = I/np.max(I)
        Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        #FFT Plot
        fig = self.Plot_fft(n,fs,signal,'Original Signal','Signal fft plot')
        return fig
##########################################################################################################################
    def HLpass_time(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        I = I/np.max(I)
        Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        signal = signal - np.mean(signal)  # DC removal
        
        #Filter: high and low
        order = (float(self.lineEdit_1.text()))  
        cutoff = (float(self.lineEdit_2.text()))
        if(str(self.comboBox_1.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)
        if(str(self.comboBox_1.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low

        #Time Plot
        fig = self.Plot_time(t,filt_signal,'Filtered Data','Filtered Data time plot')
        return fig
##########################################################################################################################
    def HLpass_fft(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        I = I/np.max(I)
        Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        signal = signal - np.mean(signal)  # DC removal

        #Filter: high and low
        order = (float(self.lineEdit_1.text()))  
        cutoff = (float(self.lineEdit_2.text()))
        if(str(self.comboBox_1.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)
        if(str(self.comboBox_1.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low

        #FFT Plot
        fig = self.Plot_fft(n,fs,filt_signal,'Highpass Filtered Data','Filtered Data FFT plot')
        return fig
##########################################################################################################################
    def AGC_time(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        I = I/np.max(I)
        Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        signal = signal - np.mean(signal)  # DC removal

        #Filter: high and low
        order = (float(self.lineEdit_1.text()))  
        cutoff = (float(self.lineEdit_2.text()))
        if(str(self.comboBox_1.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)
        if(str(self.comboBox_1.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low

        if(str(self.comboBox_2.currentText())=='With Threshold (Our Method)'):
        	threshold1 = (float(self.lineEdit_14.text()))
        	threshold2 = (float(self.lineEdit_15.text()))
        	maxpeak = []
        	time_maxpeak = []
        	minpeak = []
        	time_minpeak = []
        	x=filt_signal
        	
        	for i in range(1,len(x)-1):
        		if((x[i]>x[i-1]) and (x[i]>x[i+1]) and (x[i]>threshold1) and (x[i]>threshold2)):
        			maxpeak = np.append(maxpeak,x[i])
        			time_maxpeak = np.append(time_maxpeak,i)

        		if((x[i]<x[i-1]) and (x[i]<x[i+1]) and (x[i]<threshold1) and (x[i]<threshold2)):
        			minpeak = np.append(minpeak,x[i])
        			time_minpeak = np.append(time_minpeak,i)

        	yy1 = CubicSpline(time_maxpeak,maxpeak)
        	yy2 = CubicSpline(time_minpeak,minpeak)
        	z1=[]
        	z2=[]
	        for xx in range(0,n):
	            zi = yy1(xx)
	            z1 = np.append(z1,zi)
	        for xx in range(0,n):
	            zi = yy2(xx)
	            z2 = np.append(z2,zi)

        	for i in range(0,len(z1)):
        		if((x[i]>threshold1) and (x[i]>threshold2)):
        			x[i]=x[i]/z1[i]
        		if((x[i]<threshold1) and (x[i]<threshold2)):
        			x[i]=-x[i]/z2[i]

       	if(str(self.comboBox_2.currentText())=='Inverting values'):
       		last=0
	        prev=0
	        curr=0
	        time_peak = []
	        peak = []
	        x=filt_signal
        
	        for i in range (1,n):
	            if (x[i] < 0):
	                curr = -x[i]
	            else:
	                curr = x[i]
	            if(i > 1):
	                if (x[i-1] < 0):
	                    prev = -x[i-1]
	                else:
	                    prev = x[i-1]
	            if (last >= 0):
	                if((curr - prev) <= 0 ):
	                    time_peak = np.append(time_peak,i-1)
	                    peak = np.append(peak,prev)
	            last = curr - prev

	        yy = CubicSpline(time_peak,peak)
	        z=[]
	        for xx in range(0,n):
	            zi = yy(xx)
	            z = np.append(z,zi)

	        #inverse of the cubic spline interpolated values variable gain for input signal
	        peak_inv_limit = (float(self.lineEdit_3.text()))
	        g = np.zeros(n)

	        for i in range (1,n):
	            if (z[i] == 0):
	                g[i] = peak_inv_limit
	            else:
	                if(1/z[i] > peak_inv_limit):
	                    g[i] = peak_inv_limit
	                else:
	                    g[i] = 1/z[i]

	        #removing amplitude variations
	        for i in range (1,n):
	            x[i] = x[i]*g[i]

	    #Time plot
        fig = self.Plot_time(t,x,'AGC Data','AGC Data time plot')
        return fig
##########################################################################################################################
    def AGC_fft(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        I = I/np.max(I)
        Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        signal = signal - np.mean(signal)  # DC removal

        #Filter: high and low
        order = (float(self.lineEdit_1.text()))  
        cutoff = (float(self.lineEdit_2.text()))
        if(str(self.comboBox_1.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)
        if(str(self.comboBox_1.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low

        if(str(self.comboBox_2.currentText())=='With Threshold (Our Method)'):
        	threshold1 = (float(self.lineEdit_14.text()))
        	threshold2 = (float(self.lineEdit_15.text()))
        	maxpeak = []
        	time_maxpeak = []
        	minpeak = []
        	time_minpeak = []
        	x=filt_signal
        	
        	for i in range(1,len(x)-1):
        		if((x[i]>x[i-1]) and (x[i]>x[i+1]) and (x[i]>threshold1) and (x[i]>threshold2)):
        			maxpeak = np.append(maxpeak,x[i])
        			time_maxpeak = np.append(time_maxpeak,i)

        		if((x[i]<x[i-1]) and (x[i]<x[i+1]) and (x[i]<threshold1) and (x[i]<threshold2)):
        			minpeak = np.append(minpeak,x[i])
        			time_minpeak = np.append(time_minpeak,i)

        	yy1 = CubicSpline(time_maxpeak,maxpeak)
        	yy2 = CubicSpline(time_minpeak,minpeak)
        	z1=[]
        	z2=[]
	        for xx in range(0,n):
	            zi = yy1(xx)
	            z1 = np.append(z1,zi)
	        for xx in range(0,n):
	            zi = yy2(xx)
	            z2 = np.append(z2,zi)

        	for i in range(0,len(z1)):
        		if((x[i]>threshold1) and (x[i]>threshold2)):
        			x[i]=x[i]/z1[i]
        		if((x[i]<threshold1) and (x[i]<threshold2)):
        			x[i]=-x[i]/z2[i]

       	if(str(self.comboBox_2.currentText())=='Inverting values'):
       		last=0
	        prev=0
	        curr=0
	        time_peak = []
	        peak = []
	        x=filt_signal
        
	        for i in range (1,n):
	            if (x[i] < 0):
	                curr = -x[i]
	            else:
	                curr = x[i]
	            if(i > 1):
	                if (x[i-1] < 0):
	                    prev = -x[i-1]
	                else:
	                    prev = x[i-1]
	            if (last >= 0):
	                if((curr - prev) <= 0 ):
	                    time_peak = np.append(time_peak,i-1)
	                    peak = np.append(peak,prev)
	            last = curr - prev

	        yy = CubicSpline(time_peak,peak)
	        z=[]
	        for xx in range(0,n):
	            zi = yy(xx)
	            z = np.append(z,zi)

	        #inverse of the cubic spline interpolated values variable gain for input signal
	        peak_inv_limit = (float(self.lineEdit_3.text()))
	        g = np.zeros(n)

	        for i in range (1,n):
	            if (z[i] == 0):
	                g[i] = peak_inv_limit
	            else:
	                if(1/z[i] > peak_inv_limit):
	                    g[i] = peak_inv_limit
	                else:
	                    g[i] = 1/z[i]

	        #removing amplitude variations
	        for i in range (1,n):
	            x[i] = x[i]*g[i]

	    #Time plot
        fig = self.Plot_fft(n,fs,x,'AGC Data','AGC Data FFT plot')
        return fig
##########################################################################################################################
    def Reconstructed_time(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        I = I/np.max(I)
        Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        signal = signal - np.mean(signal)  # DC removal

        #Filter: high and low
        order = (float(self.lineEdit_1.text()))  
        cutoff = (float(self.lineEdit_2.text()))
        if(str(self.comboBox_1.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)
        if(str(self.comboBox_1.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low

        if(str(self.comboBox_2.currentText())=='With Threshold (Our Method)'):
        	threshold1 = (float(self.lineEdit_14.text()))
        	threshold2 = (float(self.lineEdit_15.text()))
        	maxpeak = []
        	time_maxpeak = []
        	minpeak = []
        	time_minpeak = []
        	x=filt_signal
        	
        	for i in range(1,len(x)-1):
        		if((x[i]>x[i-1]) and (x[i]>x[i+1]) and (x[i]>threshold1) and (x[i]>threshold2)):
        			maxpeak = np.append(maxpeak,x[i])
        			time_maxpeak = np.append(time_maxpeak,i)

        		if((x[i]<x[i-1]) and (x[i]<x[i+1]) and (x[i]<threshold1) and (x[i]<threshold2)):
        			minpeak = np.append(minpeak,x[i])
        			time_minpeak = np.append(time_minpeak,i)

        	yy1 = CubicSpline(time_maxpeak,maxpeak)
        	yy2 = CubicSpline(time_minpeak,minpeak)
        	z1=[]
        	z2=[]
	        for xx in range(0,n):
	            zi = yy1(xx)
	            z1 = np.append(z1,zi)
	        for xx in range(0,n):
	            zi = yy2(xx)
	            z2 = np.append(z2,zi)

        	for i in range(0,len(z1)):
        		if((x[i]>threshold1) and (x[i]>threshold2)):
        			x[i]=x[i]/z1[i]
        		if((x[i]<threshold1) and (x[i]<threshold2)):
        			x[i]=-x[i]/z2[i]

       	if(str(self.comboBox_2.currentText())=='Inverting values'):
       		last=0
	        prev=0
	        curr=0
	        time_peak = []
	        peak = []
	        x=filt_signal
        
	        for i in range (1,n):
	            if (x[i] < 0):
	                curr = -x[i]
	            else:
	                curr = x[i]
	            if(i > 1):
	                if (x[i-1] < 0):
	                    prev = -x[i-1]
	                else:
	                    prev = x[i-1]
	            if (last >= 0):
	                if((curr - prev) <= 0 ):
	                    time_peak = np.append(time_peak,i-1)
	                    peak = np.append(peak,prev)
	            last = curr - prev

	        yy = CubicSpline(time_peak,peak)
	        z=[]
	        for xx in range(0,n):
	            zi = yy(xx)
	            z = np.append(z,zi)

	        #inverse of the cubic spline interpolated values variable gain for input signal
	        peak_inv_limit = (float(self.lineEdit_3.text()))
	        g = np.zeros(n)

	        for i in range (1,n):
	            if (z[i] == 0):
	                g[i] = peak_inv_limit
	            else:
	                if(1/z[i] > peak_inv_limit):
	                    g[i] = peak_inv_limit
	                else:
	                    g[i] = 1/z[i]

	        #removing amplitude variations
	        for i in range (1,n):
	            x[i] = x[i]*g[i]

	    #Non-Stationary Signal Conditioning
        if(str(self.comboBox_3.currentText())=='BandPass Filter'):
            #Bandpass Filter
            order = (float(self.lineEdit_4.text()))
            fcutlow  = (float(self.lineEdit_5.text()))
            fcuthigh = (float(self.lineEdit_6.text()))

            b,a = butter(order,[2*fcutlow,2*fcuthigh]/fs, 'bandpass')
            cond_signal = filtfilt(b,a,x)

        if(str(self.comboBox_3.currentText())=='Wavelet Decomposition'):
            #Wavelet Decomposition and Reconstruction
            dbval = 'db'+str((int(self.lineEdit_7.text())))
            wavelet=pywt.Wavelet(dbval)
            lvl=(int(self.lineEdit_8.text()))
            coeffs = pywt.wavedec(x,wavelet,level=lvl)     

            def wrcoef(X, coef_type, coeffs, wavename, level):
                N = np.array(X).size
                a, ds = coeffs[0], list(reversed(coeffs[1:]))
                if coef_type =='a':
                    return pywt.upcoef('a', a, wavename, level=level)[:N]
                elif coef_type == 'd':
                    return pywt.upcoef('d', ds[level-1], wavename, level=level)[:N]
                else:
                    raise ValueError("Invalid coefficient type: {}".format(coef_type))

            cA = wrcoef(x, 'a', coeffs, wavelet, lvl)
            cD = []
            #cD[0]=cD10|cD[1]=cD9|...|cD[9]=cD1 (for lvl=10)
            for i in range (0,lvl):    
                cD.append(wrcoef(x, 'd', coeffs, wavelet, lvl-i))

            ind = (str(self.lineEdit_9.text()))
            ind = ind.split(',')
            ind = [int(s) for s in ind if s.isdigit()]
            new_sig = np.zeros(len(cA),dtype=np.complex_)

            #cA10=0|cD10=1|cD9=2|cD8=3|...|cD1=10 (for lvl=10)
            for i in range(0,len(ind)):
            	if(ind[i]==0):
            		val=cA
            	elif(ind[i]>0 and ind[i]<=lvl):
            		val=cD[ind[i]-1]
            	else:
            		val=np.zeros(len(cA))
            	new_sig += val

            cond_signal=new_sig

        if(str(self.comboBox_3.currentText())=='Empirical Mode Decomposition'):
            #Empirical Mode Decomposition and Reconstruction
            max_imf= str((int(self.lineEdit_10.text())))
            #Prepare and run EMD
            emd = EMD()
            #emd.FIXE_H = 5
            #emd.nbsym = 2
            emd.spline_kind = 'cubic'
            #emd.DTYPE = DTYPE

            nIMF = emd.emd(x, t, max_imf)
            imfNo = nIMF.shape[0]

            # Plot results
            r = np.ceil((imfNo+1))

            plt.ioff()
            plt.subplot(r,c,1)
            plt.plot(t, Q, 'r')
            #plt.xlim((tMin, tMax))
            plt.title("Original signal")
            
            for num in range(imfNo):
                plt.subplot(r,c,num+2)
                plt.plot(t, nIMF[num],'g')
                # plt.xlim((tMin, tMax))
                plt.ylabel("Imf "+str(num+1))

            imf = (str(self.lineEdit_11.text()))
            imf = imf.split(',')
            imf = [int(s) for s in imf if s.isdigit()]

            recon_signal= np.zeros(len(x))

            for i in range(0,len(ind)):       
                recon_signal += np.array(imf[i])

            cond_signal=recon_signal

        #Time Plot
        fig = self.Plot_time(t,cond_signal,'Conditioned Data','Conditioned Data Time Plot')
        return fig
##########################################################################################################################
    def Reconstructed_fft(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        I = I/np.max(I)
        Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        signal = signal - np.mean(signal)  # DC removal

        #Filter: high and low
        order = (float(self.lineEdit_1.text()))  
        cutoff = (float(self.lineEdit_2.text()))
        if(str(self.comboBox_1.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)
        if(str(self.comboBox_1.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low

        if(str(self.comboBox_2.currentText())=='With Threshold (Our Method)'):
        	threshold1 = (float(self.lineEdit_14.text()))
        	threshold2 = (float(self.lineEdit_15.text()))
        	maxpeak = []
        	time_maxpeak = []
        	minpeak = []
        	time_minpeak = []
        	x=filt_signal
        	
        	for i in range(1,len(x)-1):
        		if((x[i]>x[i-1]) and (x[i]>x[i+1]) and (x[i]>threshold1) and (x[i]>threshold2)):
        			maxpeak = np.append(maxpeak,x[i])
        			time_maxpeak = np.append(time_maxpeak,i)

        		if((x[i]<x[i-1]) and (x[i]<x[i+1]) and (x[i]<threshold1) and (x[i]<threshold2)):
        			minpeak = np.append(minpeak,x[i])
        			time_minpeak = np.append(time_minpeak,i)

        	yy1 = CubicSpline(time_maxpeak,maxpeak)
        	yy2 = CubicSpline(time_minpeak,minpeak)
        	z1=[]
        	z2=[]
	        for xx in range(0,n):
	            zi = yy1(xx)
	            z1 = np.append(z1,zi)
	        for xx in range(0,n):
	            zi = yy2(xx)
	            z2 = np.append(z2,zi)

        	for i in range(0,len(z1)):
        		if((x[i]>threshold1) and (x[i]>threshold2)):
        			x[i]=x[i]/z1[i]
        		if((x[i]<threshold1) and (x[i]<threshold2)):
        			x[i]=-x[i]/z2[i]

       	if(str(self.comboBox_2.currentText())=='Inverting values'):
       		last=0
	        prev=0
	        curr=0
	        time_peak = []
	        peak = []
	        x=filt_signal
        
	        for i in range (1,n):
	            if (x[i] < 0):
	                curr = -x[i]
	            else:
	                curr = x[i]
	            if(i > 1):
	                if (x[i-1] < 0):
	                    prev = -x[i-1]
	                else:
	                    prev = x[i-1]
	            if (last >= 0):
	                if((curr - prev) <= 0 ):
	                    time_peak = np.append(time_peak,i-1)
	                    peak = np.append(peak,prev)
	            last = curr - prev

	        yy = CubicSpline(time_peak,peak)
	        z=[]
	        for xx in range(0,n):
	            zi = yy(xx)
	            z = np.append(z,zi)

	        #inverse of the cubic spline interpolated values variable gain for input signal
	        peak_inv_limit = (float(self.lineEdit_3.text()))
	        g = np.zeros(n)

	        for i in range (1,n):
	            if (z[i] == 0):
	                g[i] = peak_inv_limit
	            else:
	                if(1/z[i] > peak_inv_limit):
	                    g[i] = peak_inv_limit
	                else:
	                    g[i] = 1/z[i]

	        #removing amplitude variations
	        for i in range (1,n):
	            x[i] = x[i]*g[i]

	    #Non-Stationary Signal Conditioning
        if(str(self.comboBox_3.currentText())=='BandPass Filter'):
            #Bandpass Filter
            order = (float(self.lineEdit_4.text()))
            fcutlow  = (float(self.lineEdit_5.text()))
            fcuthigh = (float(self.lineEdit_6.text()))

            b,a = butter(order,[2*fcutlow,2*fcuthigh]/fs, 'bandpass')
            cond_signal = filtfilt(b,a,x)

        if(str(self.comboBox_3.currentText())=='Wavelet Decomposition'):
            #Wavelet Decomposition and Reconstruction
            dbval = 'db'+str((int(self.lineEdit_7.text())))
            wavelet=pywt.Wavelet(dbval)
            lvl=(int(self.lineEdit_8.text()))
            coeffs = pywt.wavedec(x,wavelet,level=lvl)     

            def wrcoef(X, coef_type, coeffs, wavename, level):
                N = np.array(X).size
                a, ds = coeffs[0], list(reversed(coeffs[1:]))
                if coef_type =='a':
                    return pywt.upcoef('a', a, wavename, level=level)[:N]
                elif coef_type == 'd':
                    return pywt.upcoef('d', ds[level-1], wavename, level=level)[:N]
                else:
                    raise ValueError("Invalid coefficient type: {}".format(coef_type))

            cA = wrcoef(x, 'a', coeffs, wavelet, lvl)
            cD = []
            #cD[0]=cD10|cD[1]=cD9|...|cD[9]=cD1 (for lvl=10)
            for i in range (0,lvl):    
                cD.append(wrcoef(x, 'd', coeffs, wavelet, lvl-i))

            ind = (str(self.lineEdit_9.text()))
            ind = ind.split(',')
            ind = [int(s) for s in ind if s.isdigit()]
            new_sig = np.zeros(len(cA),dtype=np.complex_)

            #cA10=0|cD10=1|cD9=2|cD8=3|...|cD1=10 (for lvl=10)
            for i in range(0,len(ind)):
            	if(ind[i]==0):
            		val=cA
            	elif(ind[i]>0 and ind[i]<=lvl):
            		val=cD[ind[i]-1]
            	else:
            		val=np.zeros(len(cA))
            	new_sig += val

            cond_signal=new_sig

        if(str(self.comboBox_3.currentText())=='Empirical Mode Decomposition'):
            #Empirical Mode Decomposition and Reconstruction
            max_imf= str((int(self.lineEdit_10.text())))
            #Prepare and run EMD
            emd = EMD()
            #emd.FIXE_H = 5
            #emd.nbsym = 2
            emd.spline_kind = 'cubic'
            #emd.DTYPE = DTYPE

            nIMF = emd.emd(x, t, max_imf)
            imfNo = nIMF.shape[0]

            # Plot results
            r = np.ceil((imfNo+1))

            plt.ioff()
            plt.subplot(r,c,1)
            plt.plot(t, Q, 'r')
            #plt.xlim((tMin, tMax))
            plt.title("Original signal")
            
            for num in range(imfNo):
                plt.subplot(r,c,num+2)
                plt.plot(t, nIMF[num],'g')
                # plt.xlim((tMin, tMax))
                plt.ylabel("Imf "+str(num+1))

            imf = (str(self.lineEdit_11.text()))
            imf = imf.split(',')
            imf = [int(s) for s in imf if s.isdigit()]

            recon_signal= np.zeros(len(x))

            for i in range(0,len(ind)):       
                recon_signal += np.array(imf[i])

            cond_signal=recon_signal

        #FFT Plot
        self.Status_Bar('Do not press another button before closing the graph')
        fft  = np.fft.fftshift(np.fft.fft((cond_signal), n))
        fftf = np.fft.fftshift(np.fft.fftfreq(n, 1./fs))
        scale = 1e3
        fftf = fftf/scale
        xlim = 5000
    	fig = plt.figure(figsize=(10, 8))
        plt.plot(fftf, 20*np.log10(np.abs(fft)), label='Conditioned Data')
        plt.xlim(0, xlim)
        plt.xticks(np.arange(0, xlim+1, xlim/5))
        plt.xlabel('Frequency (KHz)', fontsize=14)
        plt.ylabel('Amplitude', fontsize=14)
        plt.title('Conditioned Data FFT plot')
        plt.grid()
        plt.legend()
        if(flag==1):
        	plt.show()
        	self.Status_Bar('Another button can be pressed now')
        return fig
##########################################################################################################################
    def Spectogram_signal(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        I = I/np.max(I)
        Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        signal = signal - np.mean(signal)  # DC removal

        #Specgram parameters
        fft_pts = (int(self.lineEdit_12.text()))
        overlap_pts = (int(self.lineEdit_13.text()))
        pad = (int(self.lineEdit_16.text()))

        if(str(self.comboBox_4.currentText())=='Hanning'):
        	windfn=np.hanning(fft_pts)
        if(str(self.comboBox_4.currentText())=='Blackman'):
        	windfn=np.blackman(fft_pts)
        if(str(self.comboBox_4.currentText())=='Hamming'):
        	windfn=np.hamming(fft_pts)
        if(str(self.comboBox_4.currentText())=='Bartlett'):
        	windfn=np.bartlett(fft_pts)

        #Spectogram of signal
        self.Status_Bar('Do not press another button before closing the graph')
        fig = plt.figure(figsize=(10, 8))
        plt.specgram(signal,NFFT=fft_pts,Fs=fs,window=windfn,noverlap=overlap_pts,pad_to=pad,scale ='linear',label='Signal')
        plt.title('Spectrogram of Signal')
        plt.ylim(-0.2e7,0.4e7)
        plt.colorbar()
        plt.grid()
        plt.legend()
        if(flag==1):
        	plt.show()
        	self.Status_Bar('Another button can be pressed now')
        return fig
##########################################################################################################################
    def Spectogram_cond(self):
    	datafile = (str(self.lineEdit.text()))
     	t, Q, I = np.loadtxt(datafile)
        I = I/np.max(I)
        Q = Q/np.max(Q)
        fs = np.round(1/(t[1]-t[0]), -3)
        phase = np.unwrap(np.arctan2(Q,I))
        #Original Signal using I and Q Data
        signal = I  + 1j*Q
        n = len(I)
        signal = signal - np.mean(signal)  # DC removal

        #Filter: high and low
        order = (float(self.lineEdit_1.text()))  
        cutoff = (float(self.lineEdit_2.text()))
        if(str(self.comboBox_1.currentText())=='HighPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'high')
            filt_signal = filtfilt(b,a,signal)
        if(str(self.comboBox_1.currentText())=='Signal - LowPass Filtered Signal'):
            b,a = butter(order,2*cutoff/fs,'low')
            signal_low  = filtfilt(b,a,signal)
            filt_signal = signal - signal_low

        if(str(self.comboBox_2.currentText())=='With Threshold (Our Method)'):
        	threshold1 = (float(self.lineEdit_14.text()))
        	threshold2 = (float(self.lineEdit_15.text()))
        	maxpeak = []
        	time_maxpeak = []
        	minpeak = []
        	time_minpeak = []
        	x=filt_signal
        	
        	for i in range(1,len(x)-1):
        		if((x[i]>x[i-1]) and (x[i]>x[i+1]) and (x[i]>threshold1) and (x[i]>threshold2)):
        			maxpeak = np.append(maxpeak,x[i])
        			time_maxpeak = np.append(time_maxpeak,i)

        		if((x[i]<x[i-1]) and (x[i]<x[i+1]) and (x[i]<threshold1) and (x[i]<threshold2)):
        			minpeak = np.append(minpeak,x[i])
        			time_minpeak = np.append(time_minpeak,i)

        	yy1 = CubicSpline(time_maxpeak,maxpeak)
        	yy2 = CubicSpline(time_minpeak,minpeak)
        	z1=[]
        	z2=[]
	        for xx in range(0,n):
	            zi = yy1(xx)
	            z1 = np.append(z1,zi)
	        for xx in range(0,n):
	            zi = yy2(xx)
	            z2 = np.append(z2,zi)

        	for i in range(0,len(z1)):
        		if((x[i]>threshold1) and (x[i]>threshold2)):
        			x[i]=x[i]/z1[i]
        		if((x[i]<threshold1) and (x[i]<threshold2)):
        			x[i]=-x[i]/z2[i]

       	if(str(self.comboBox_2.currentText())=='Inverting values'):
       		last=0
	        prev=0
	        curr=0
	        time_peak = []
	        peak = []
	        x=filt_signal
        
	        for i in range (1,n):
	            if (x[i] < 0):
	                curr = -x[i]
	            else:
	                curr = x[i]
	            if(i > 1):
	                if (x[i-1] < 0):
	                    prev = -x[i-1]
	                else:
	                    prev = x[i-1]
	            if (last >= 0):
	                if((curr - prev) <= 0 ):
	                    time_peak = np.append(time_peak,i-1)
	                    peak = np.append(peak,prev)
	            last = curr - prev

	        yy = CubicSpline(time_peak,peak)
	        z=[]
	        for xx in range(0,n):
	            zi = yy(xx)
	            z = np.append(z,zi)

	        #inverse of the cubic spline interpolated values variable gain for input signal
	        peak_inv_limit = (float(self.lineEdit_3.text()))
	        g = np.zeros(n)

	        for i in range (1,n):
	            if (z[i] == 0):
	                g[i] = peak_inv_limit
	            else:
	                if(1/z[i] > peak_inv_limit):
	                    g[i] = peak_inv_limit
	                else:
	                    g[i] = 1/z[i]

	        #removing amplitude variations
	        for i in range (1,n):
	            x[i] = x[i]*g[i]

	    #Non-Stationary Signal Conditioning
        if(str(self.comboBox_3.currentText())=='BandPass Filter'):
            #Bandpass Filter
            order = (float(self.lineEdit_4.text()))
            fcutlow  = (float(self.lineEdit_5.text()))
            fcuthigh = (float(self.lineEdit_6.text()))

            b,a = butter(order,[2*fcutlow,2*fcuthigh]/fs, 'bandpass')
            cond_signal = filtfilt(b,a,x)

        if(str(self.comboBox_3.currentText())=='Wavelet Decomposition'):
            #Wavelet Decomposition and Reconstruction
            dbval = 'db'+str((int(self.lineEdit_7.text())))
            wavelet=pywt.Wavelet(dbval)
            lvl=(int(self.lineEdit_8.text()))
            coeffs = pywt.wavedec(x,wavelet,level=lvl)     

            def wrcoef(X, coef_type, coeffs, wavename, level):
                N = np.array(X).size
                a, ds = coeffs[0], list(reversed(coeffs[1:]))
                if coef_type =='a':
                    return pywt.upcoef('a', a, wavename, level=level)[:N]
                elif coef_type == 'd':
                    return pywt.upcoef('d', ds[level-1], wavename, level=level)[:N]
                else:
                    raise ValueError("Invalid coefficient type: {}".format(coef_type))

            cA = wrcoef(x, 'a', coeffs, wavelet, lvl)
            cD = []
            #cD[0]=cD10|cD[1]=cD9|...|cD[9]=cD1 (for lvl=10)
            for i in range (0,lvl):    
                cD.append(wrcoef(x, 'd', coeffs, wavelet, lvl-i))

            ind = (str(self.lineEdit_9.text()))
            ind = ind.split(',')
            ind = [int(s) for s in ind if s.isdigit()]
            new_sig = np.zeros(len(cA),dtype=np.complex_)

            #cA10=0|cD10=1|cD9=2|cD8=3|...|cD1=10 (for lvl=10)
            for i in range(0,len(ind)):
            	if(ind[i]==0):
            		val=cA
            	elif(ind[i]>0 and ind[i]<=lvl):
            		val=cD[ind[i]-1]
            	else:
            		val=np.zeros(len(cA))
            	new_sig += val

            cond_signal=new_sig

        if(str(self.comboBox_3.currentText())=='Empirical Mode Decomposition'):
            #Empirical Mode Decomposition and Reconstruction

            cond_signal=np.zeros(len(t))

        #Specgram parameters
        fft_pts = (int(self.lineEdit_12.text()))
        overlap_pts = (int(self.lineEdit_13.text()))
        pad = (int(self.lineEdit_16.text()))

        if(str(self.comboBox_4.currentText())=='Hanning'):
        	windfn=np.hanning(fft_pts)
        if(str(self.comboBox_4.currentText())=='Blackman'):
        	windfn=np.blackman(fft_pts)
        if(str(self.comboBox_4.currentText())=='Hamming'):
        	windfn=np.hamming(fft_pts)
        if(str(self.comboBox_4.currentText())=='Bartlett'):
        	windfn=np.bartlett(fft_pts)

        #Spectogram after AGC
        self.Status_Bar('Do not press another button before closing the graph')
        fig = plt.figure(figsize=(10, 8))
        plt.specgram(cond_signal,NFFT=fft_pts,Fs=fs,window=windfn,noverlap=overlap_pts,pad_to=pad,scale ='linear',label='Cond Signal')
        plt.title('Spectrogram of Cond Signal')
        plt.ylim(-0.2e7,0.4e7)
        plt.colorbar()
        plt.grid()
        plt.legend()
        if(flag==1):
        	plt.show()
        	self.Status_Bar('Another button can be pressed now')
        return fig      
##########################################################################################################################
#NEW end##################################################################################################################

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox_1.setTitle(_translate("Dialog", "1 - Original Data", None))
        self.label_1.setText(_translate("Dialog", "Enter the data file address:", None))
        self.lineEdit.setText(_translate("Dialog", "tIQdata_t57_1.txt", None))
        self.pushButton_1.setText(_translate("Dialog", "Browse", None))
        self.pushButton_2.setText(_translate("Dialog", "I and Q time plot", None))
        self.pushButton_3.setText(_translate("Dialog", "Original Signal time plot", None))
        self.pushButton_4.setText(_translate("Dialog", "Original Signal FFT plot", None))
        self.groupBox_2.setTitle(_translate("Dialog", "2 - Baseline Wandering", None))
        self.label_2.setText(_translate("Dialog", "AGC Type: ", None))
        self.comboBox_1.setItemText(0, _translate("Dialog", "Signal - LowPass Filtered Signal", None))
        self.comboBox_1.setItemText(1, _translate("Dialog", "HighPass Filtered Signal", None))
        self.label_3.setText(_translate("Dialog", "Order (LP/HP):", None))
        self.label_4.setText(_translate("Dialog", "Cutoff (LP/HP):", None))
        self.lineEdit_1.setText(_translate("Dialog", "2", None))
        self.lineEdit_2.setText(_translate("Dialog", "1000000", None))
        self.label_5.setText(_translate("Dialog", "Hz", None))
        self.pushButton_5.setText(_translate("Dialog", "Filtered Signal time plot", None))
        self.pushButton_6.setText(_translate("Dialog", "Filtered Signal FFT plot", None))
        self.groupBox_3.setTitle(_translate("Dialog", "3 - Signal Normalisation", None))
        self.label_6.setText(_translate("Dialog", "Peak Detection:", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "With Threshold (Our Method)", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Inverting values", None))
        self.pushButton_7.setText(_translate("Dialog", "AGC Data time plot", None))
        self.pushButton_8.setText(_translate("Dialog", "AGC FFT time plot", None))
        self.lineEdit_3.setText(_translate("Dialog", "100", None))
        self.label_7.setText(_translate("Dialog", "Peak Inversion Limit:", None))
        self.label_23.setText(_translate("Dialog", "Max Threshold:", None))
        self.lineEdit_14.setText(_translate("Dialog", "0.02", None))
        self.lineEdit_15.setText(_translate("Dialog", "-0.02", None))
        self.label_24.setText(_translate("Dialog", "Max Threshold:", None))
        self.groupBox_6.setTitle(_translate("Dialog", "4 - Signal Conditioning", None))
        self.label_8.setText(_translate("Dialog", "Method:", None))
        self.comboBox_3.setItemText(0, _translate("Dialog", "BandPass Filter", None))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Wavelet Decomposition", None))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Empirical Mode Decomposition", None))
        self.groupBox_7.setTitle(_translate("Dialog", "4a - BandPass Filter", None))
        self.label_9.setText(_translate("Dialog", "Order (BP):", None))
        self.label_10.setText(_translate("Dialog", "Low-Cut (BP):", None))
        self.lineEdit_5.setText(_translate("Dialog", "1000000", None))
        self.lineEdit_4.setText(_translate("Dialog", "1", None))
        self.label_11.setText(_translate("Dialog", "Hz", None))
        self.lineEdit_6.setText(_translate("Dialog", "1600000", None))
        self.label_12.setText(_translate("Dialog", "High-Cut (BP):", None))
        self.label_13.setText(_translate("Dialog", "Hz", None))
        self.groupBox_8.setTitle(_translate("Dialog", "4b - Wavelet Decomposition", None))
        self.label_14.setText(_translate("Dialog", "Wavelet No:", None))
        self.label_15.setText(_translate("Dialog", "No of Levels:", None))
        self.label_16.setText(_translate("Dialog", "To add:", None))
        self.lineEdit_7.setText(_translate("Dialog", "4", None))
        self.lineEdit_8.setText(_translate("Dialog", "10", None))
        self.lineEdit_9.setText(_translate("Dialog", "3,4,5", None))
        self.label.setText(_translate("Dialog", "(4 => db4)", None))
        self.groupBox_9.setTitle(_translate("Dialog", "4c - Empirical Mode Decomposition", None))
        self.label_18.setText(_translate("Dialog", "To add:", None))
        self.lineEdit_11.setText(_translate("Dialog", "3,4,5", None))
        self.lineEdit_10.setText(_translate("Dialog", "10", None))
        self.label_17.setText(_translate("Dialog", "No of IMFs:", None))
        self.pushButton_9.setText(_translate("Dialog", "Reconstructed time plot", None))
        self.pushButton_10.setText(_translate("Dialog", "Reconstructed FFT plot", None))
        self.groupBox_10.setTitle(_translate("Dialog", "5 - Spectogram", None))
        self.label_19.setText(_translate("Dialog", "Window Type:", None))
        self.comboBox_4.setItemText(0, _translate("Dialog", "Hanning", None))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Blackman", None))
        self.comboBox_4.setItemText(2, _translate("Dialog", "Hamming", None))
        self.comboBox_4.setItemText(3, _translate("Dialog", "Bartlett", None))
        self.label_20.setText(_translate("Dialog", "No of FFT points:", None))
        self.label_21.setText(_translate("Dialog", "No of overlapping points:", None))
        self.lineEdit_12.setText(_translate("Dialog", "3993", None))
        self.lineEdit_13.setText(_translate("Dialog", "128", None))
        self.pushButton_11.setText(_translate("Dialog", "Spectogram - Signal", None))
        self.pushButton_12.setText(_translate("Dialog", "Spectogram - Cond. Signal", None))
        self.label_25.setText(_translate("Dialog", "Padding:", None))
        self.lineEdit_16.setText(_translate("Dialog", "3993", None))
        self.label_22.setText(_translate("Dialog", "STATUS:", None))
#NEW start################################################################################################################
        self.textBrowser.setHtml('Last saved parameters loaded. Press "Ctrl+D" for default parameters')
#NEW end##################################################################################################################


if __name__ == "__main__":
    import sys
#NEW start################################################################################################################
    loadFile = open('F_Default_parameters.csv')
    loadReader = csv.reader(loadFile)
    loadData = list(loadReader)
    fname,order_hl,cutoff_hl,peak_inv_lim,order_b,lowcut_b,highcut_b,wavelet_no,no_of_lvls,add_wvlt,no_of_imfs,add_emd,nfft,noverlap,max_thres,min_thres,padding,agc_type,peak_type,cond_type,win_type=loadData[0]
    flag=1
#NEW end##################################################################################################################
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

