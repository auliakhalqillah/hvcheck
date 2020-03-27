# HVSR CHECK FOR RELIABLE AND CLEAR PEAK OF H/V CURVE
This is a program to check reliable and clear peak of H/V curve from Geopsy file (.hv) called `hvsrcheck`.<br>
The program has been written based on information from [**GUIDELINES FOR THE IMPLEMENTATION OF THE H/V SPECTRAL RATIO TECHNIQUE ON AMBIENT VIBRATIONS MEASUREMENTS,SESAME 2004**](http://sesame.geopsy.org/SES_Reports.htm)
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
if the modules has been successfully installed, the information of reliable and clear peak will show up, like this:
```
-----------------------------------------------------------------------
OUTPUT INFORMATION OF H/V
-----------------------------------------------------------------------
      Frequency   Average       Min       Max
0      0.100000  0.022280  0.010910  0.045499
1      0.100451  0.022281  0.010922  0.045456
2      0.100904  0.022280  0.010931  0.045411
3      0.101360  0.022277  0.010939  0.045366
4      0.101817  0.022272  0.010945  0.045321
...         ...       ...       ...       ...
1019   9.821550  0.201675  0.167110  0.243391
1020   9.865860  0.194437  0.161490  0.234105
1021   9.910370  0.187867  0.156366  0.225713
1022   9.955080  0.181955  0.151724  0.218209
1023  10.000000  0.176691  0.147554  0.211581

[1024 rows x 4 columns]
A0		: 1.0481
F0		: 7.25987 Hz
KG		: 0.15131312406420502
MIN F0		: 6.744 Hz
MAXF0		: 7.77574 Hz
WINDOW		: 58
WINDOW LENGTH	: 25.0 second
-----------------------------------------------------------------------
File Name		: 3636_new.hv
-----------------------------------------------------------------------
CRITERIA FOR A RELIABLE H/V CURVE
-----------------------------------------------------------------------
RELIABLE 1 - OK		:f0 > 10/lw	= 7.259870 > 0.400000
RELIABLE 2 - OK		:nc(f0) > 200	= 10526.811500 > 200
RELIABLE 3 - OK		:Std H/V(f) < 2	= 7.259870 > 0.5Hz
-----------------------------------------------------------------------
CLEAR PEAK FOR H/V CURVE
-----------------------------------------------------------------------
CLEAR PEAK 1 - OK	:∃ f- ∈ [f0/4,f0] ∣ A(f-) < A0/2
CLEAR PEAK 2 - OK	:∃ f+ ∈ [f0,4f0] ∣ A(f+) < A0/2
CLEAR PEAK 3 - NO	:A0 < 2 | 1.0481 < 2
CLEAR PEAK 4 - OK	:Fpeak [A(f) ± stdA(f) = f0 ± 5%]
CLEAR PEAK 5 - NO	:σf > ε(F0) | 0.5158700000000005 > 0.3629935
CLEAR PEAK 6 - OK	:σA(F0) < θ (F0)

CLEAR PEAK SUMMARY	: 4 out of 6 criteria fulfilled
CLEAR PEAK SUMMARY	: H/V IS NOT CLEAR PEAK [at least 5 out of 6 criteria fulfilled]
```
To run with your Geopsy files, you just need change the file name and log name in `geopsy_hvsrcheck.py` file.
# NOTE
The file of `geopsy_hvsrcheck.py` will read if the line of header of Geopsy file (.hv) has 6 lines header, for an example:
```
0 # GEOPSY output version 1.1
1 # Number of windows = 58
2 # f0 from average	7.59876
3 # Number of windows for f0 = 58
4 # f0 from windows	7.25987	6.744	7.77574
5 # Peak amplitude	1.0481
6 # Frequency	Average	Min	Max
7 0.1	0.0222796	0.0109096	0.0454994 <<< start the first data at 7th line
```
so, if you want to extract the data based on this example, you have to put the `index` equal to 7 at 43th line of `geopsy_hvsrcheck.py`, because the first data of H/V at 7th line. Remember, in Python the index is started from 0!
If you have the line of header of Geopsy file (.hv) more than 6 line, you just need readjust the `index` number where the index first data is.
# CONTACT
This code has been written by Aulia Khalqillah,S.Si.,M.Si (2020)<br>
Email: auliakhalqillah.mail@gmail.com 
