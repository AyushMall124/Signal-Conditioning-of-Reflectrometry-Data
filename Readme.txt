# Following is a readme file for the software implementation of FMCW Radar Project. 
# The project was done by Ayush Mall and Kushagra Shah under the guidance of Prof. Amalin Prince.

1. The project is shared on google drive with the concerned parties. Anyhow, following is the drive link:
   https://drive.google.com/drive/folders/1PpqOVgem24lEsXIFBhltZTclOvsvwyfc?usp=sharing

2. The files have been arranged in subfolders for convenience. This readme file can be found in the "Supportin files" folder. It is recommended that the python file be kept in a seperate folder after downloading.

3. The python codes are in the "GUI Python codes" folder. They were coded on Python 2.7, and require the installation of certain libraries.
   For running the code 'pip' has to be downloaded first.Then the libraries (found in the beginning of the code) can be installed using the 'pip install' command.
   A custom library is used for which the "PyEMD" folder from the "Supporting files" folder has to be downloaded. It has to be kept in the same folder as the python file.

4. The F_Default_parameters.csv files contains the default input parameters for the GUI_EMD_WD.py file. It has to be downloaded from the "Supporting files" folder and kept in the same folder as the python file.
   Other csv files will also be created when the python code is run and input parameters are saved/loaded in the GUI. They will automatically be created in the same folder as the python file.

5. GUI_EMD_WD.py contains the python code for the older approach: 
   Baseline Wandering Removal (HPF) -> Signal Normalisation (Threshold/Inverting) -> Signal Conditioning (BPF/WD/EMD)
    
6. GUI_GoodMethod.py contains the python code for the new approach:
   Baseline Wandering Removal (HPF) -> Signal Conditioning (BPF) -> Signal Normalisation (Homomorphic Filtering)

7. GoodMethod.m is the MATLAB code for the new approach. The codes for time and frequency plots can be accessed at every step by removing the comments disabling them.

8. The python and MATLAB codes use different data file formats. They also require different arrangement of t, I, Q data within the data files. Hence, there are two folders with the useful data available in both the formats.
   See "MATLAB Data files" and "Python Data files" as two seperate folders. Find MATLAB to Python data format converter as a MtoP_DataConverter.m file in the "Supporting files" folder. 

9. The python and MATLAB codes contain commented parts of code that store data in between the steps into data files. These can be compared for analysis purposes. 
   The 0_Correlation.py file in the "Supporting files" folder is used for finding the correlation between the data.

10. Any suggestions and requests on the code are welcome.
