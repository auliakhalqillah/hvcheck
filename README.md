# HVSR CHECK: RELIABLE AND CLEAR PEAK OF H/V CURVE
This is a program to check reliable and clear peak of H/V curve from Geopsy file (.hv) called `hvsrcheck`.<br>
The program has been written based on information from [**GUIDELINES FOR THE IMPLEMENTATION OF THE H/V SPECTRAL RATIO TECHNIQUE ON AMBIENT VIBRATIONS MEASUREMENTS,SESAME 2004**](ftp://ftp.geo.uib.no/pub/seismo/SOFTWARE/SESAME/USER-GUIDELINES/SESAME-HV-User-Guidelines.pdf)
# REQUIRED
1. Numpy
2. Pandas
3. Python 3 (Recommended >=3.7)
# INSTALL
Type the following command to install the modules of `hvsrcheck`:
```
python3 setup.py install --record installpath.txt
```
# USAGE
Go to test folder and run the `geopsy_hvsrcheck.py` by following command:
```
python3 geopsy_hvsrcheck.py
```
if the modules has been successfully installed, the information of reliable and clear peak will show up.<br>
To run with your Geopsy files, you just need change the file name and log name in `geopsy_hvsrcheck.py` file.
# CONTACT
This code has been written by Aulia Khalqillah,S.Si.,M.Si (2020)<br>
Email: auliakhalqillah.mail@gmail.com 
