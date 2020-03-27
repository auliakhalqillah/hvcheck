# File name     : geopsy_hvsrcheck.py
# Info          : Program to check reliable and clear peak of H/V curve from Geopsy file (.hv)
# Update        : 26th March 2020
# Written by    : Aulia Khalqillah,S.Si.,M.Si
# Email         : auliakhalqillah.mail@gmail.com
# Source        : GUIDELINES FOR THE IMPLEMENTATION OF THE H/V SPECTRAL RATIO TECHNIQUE ON AMBIENT VIBRATIONS
#                 MEASUREMENTS, PROCESSING AND INTERPRETATION, SESAME European research project
#                 WP12 – Deliverable D23.12 [ftp://ftp.geo.uib.no/pub/seismo/SOFTWARE/SESAME/USER-GUIDELINES/SESAME-HV-User-Guidelines.pdf]
#
# USAGE         : Using hvsrcheck.py as modules file
#                 example: hvsrcheck(input)
#                 input is dictionary type.
#                 "You just need to add the .hv and .log files in filename and logname variable that you have"
# TESTED        : Python >= 3.7
# ------------------------------------------------------------------------------------------------------------------------------------------
from numpy import *
import pandas as pd
from hvcheck import hvsrcheck

filename = '3636_new.hv'
logname = '3636_new.log'
data = open(filename,"r")
logfile = open(logname,"r")
# Read .hv file
index = 0
frequency = []
amplification = []
minamplification = []
maxamplification = []
for line in data:
    # Take Dominant Frequency (f0)
    if (index == 4):
        fr0 = line.strip().split("\t")
        domfreq = float(fr0[1])
        mindomfreq = float(fr0[2])
        maxdomfreq = float(fr0[3])
    # Take Amplification
    if (index == 5):
        hv = line.strip().split("\t")
        hv = float(hv[1])
    
    # Take the data
    if index >= 7:
        field = line.strip().split("\t")
        freq = float(field[0])
        amp = float(field[1])
        minamp = float(field[2])
        maxamp = float(field[3])
        frequency.append(freq)
        amplification.append(amp)
        minamplification.append(minamp)
        maxamplification.append(maxamp)
    index = index + 1

frequency = array(frequency)
amplification = array(amplification)
minamplification = array(minamplification)
maxamplification = array(maxamplification)
KG = ((hv**2)/domfreq)
idmaxamp = argmax(amplification)
stddivA = divide(maxamplification,amplification)
stdA = stddivA[idmaxamp]
stdf0 = domfreq-mindomfreq
stdhv = subtract(amplification,minamplification)
minstdA0 = minamplification[argmax(minamplification)]
maxstdA0 = maxamplification[argmax(maxamplification)]
collect = [frequency,amplification,minamplification,maxamplification]
store_data = pd.DataFrame(collect,index=['Frequency','Average','Min','Max']).T
print("-----------------------------------------------------------------------")
print("OUTPUT INFORMATION OF H/V")
print("-----------------------------------------------------------------------")
print(store_data)
print("A0\t\t:",hv)
print("F0\t\t:",domfreq,"Hz")
print("KG\t\t:",KG)
print("MIN F0\t\t:",mindomfreq,"Hz")
print("MAXF0\t\t:",maxdomfreq,"Hz")
data.close()

# Read log file
index = 0
for line in logfile:
    # Find window Number
    if (index == 111):
        win = line.strip().split("\t")
        window = int(win[0][-2:])

    # Find window length
    if (index == 113):
        winl = line.strip().split("\t")
        winlength = float(winl[2])
    index = index + 1

print("WINDOW\t\t:",window)
print("WINDOW LENGTH\t:",winlength,"second")
logfile.close()

# HVSR CHECK
# Store output information to dictionary
input = {
            'filename':filename,
            'maxfreq':max(frequency),
            'winlength':winlength,
            'window':window,
            'frhv':frequency,
            'hvsr':amplification,
            'A0':hv,
            'F0':domfreq,
            'KG':KG,
            'stdA':stdA,
            'stdf0':stdf0,
            'stdhv':stdhv,
            'f0min':mindomfreq,
            'f0max':maxdomfreq,
            'minstdhv':minamplification,
            'maxstdhv':maxamplification,
            'minstdA0':minstdA0,
            'maxstdA0':maxstdA0,
            'lengthhv':len(amplification),
            }

hvsrcheck(input)
