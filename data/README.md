Data files used in this project are already located within the main 'data' folder.  The original data sets can be downloaded off of the CRCNS website using the link https://crcns.org/data-sets/vc/v2-1/about-v2-1 given the user has undergone the necessary steps to receive access to data.

The data files that I used were "NR-z0131.ezrev4.001.p1.mat" for experiment 1 and "NR-z0126.ezrev4.002.p1.mat" for experiment 2.
These specific files can be downloaded directly from pulling from the 'data' directory on the GitHub page.

The data is in the for of .mat files intended to be used in MatLab.  For this project however, Python was used to read the data.  This was done in my script using a function called 'LoadMat' that was able to convert the .mat file into something that could be converted into python script.  For the statistical analyses section, I used Pandas to organize the data and later perform mathematical operations on.

I uploaded a module that is located within the main repository called "My Data Module".  This module takes one of the trials used within the experiement and more specifically takes two of the keys from within the dictionary, "SpikeTime" and "PhotoTime".
I was able to retrieve this data by downloading the MatLab file from CRCNS website and running the LoadMat funciton within the data loading module. 
