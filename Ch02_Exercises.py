Solutions
There will be many ways to solve these exercises which weren't covered in this chapter; however, the solutions below use only what has been introduced in chapter 2.

About the Data
In this notebook, we will be working with Earthquake data from September 18, 2018 - October 13, 2018 (obtained from the US Geological Survey (USGS) using the USGS API)

Setup
In [1]:
import pandas as pd

df = pd.read_csv('../../ch_02/data/parsed.csv')
Exercise 1
In [2]:
df[
    (df.parsed_place == 'Japan') & (df.magType == 'mb')
].mag.quantile(0.95)
Out[2]:
4.9
Exercise 2
In [3]:
f"{df[df.parsed_place == 'Indonesia'].tsunami.value_counts(normalize=True).iloc[1,]:.2%}"
Out[3]:
'23.13%'
Exercise 3
In [4]:
df[df.parsed_place == 'Nevada'].describe()
Out[4]:
cdi	dmin	felt	gap	mag	mmi	nst	rms	sig	time	tsunami	tz	updated
count	15.000000	681.000000	15.000000	681.000000	681.000000	1.00	681.000000	681.000000	681.000000	6.810000e+02	681.0	681.0	6.810000e+02
mean	2.440000	0.166199	2.400000	153.668120	0.500073	2.84	12.618209	0.151986	10.970631	1.538314e+12	0.0	-480.0	1.538402e+12
std	0.501142	0.166228	4.626013	68.735302	0.696710	NaN	9.866963	0.084662	19.607150	5.965637e+08	0.0	0.0	6.010951e+08
min	2.000000	0.001000	1.000000	29.140000	-0.500000	2.84	3.000000	0.000500	0.000000	1.537247e+12	0.0	-480.0	1.537307e+12
25%	2.000000	0.053000	1.000000	97.380000	-0.100000	2.84	6.000000	0.106900	0.000000	1.537854e+12	0.0	-480.0	1.537928e+12
50%	2.200000	0.112000	1.000000	149.140000	0.400000	2.84	10.000000	0.146300	2.000000	1.538280e+12	0.0	-480.0	1.538428e+12
75%	2.900000	0.233000	1.000000	199.720000	0.900000	2.84	16.000000	0.187100	12.000000	1.538821e+12	0.0	-480.0	1.538878e+12
max	3.300000	1.414000	19.000000	355.910000	2.900000	2.84	61.000000	0.863400	129.000000	1.539461e+12	0.0	-480.0	1.539483e+12
Exercise 4
Note we need to use ^Mexico to get Mexico, but not New Mexico.

In [5]:
df['ring_of_fire'] = df.parsed_place.str.contains(r'|'.join([
    'Alaska', 'Antarctic', 'Bolivia', 'California', 'Canada',
    'Chile', 'Costa Rica', 'Ecuador', 'Fiji', 'Guatemala',
    'Indonesia', 'Japan', 'Kermadec Islands', '^Mexico',
    'New Zealand', 'Peru', 'Philippines', 'Russia',
    'Taiwan', 'Tonga', 'Washington' 
]))
Exercise 5
In [6]:
df.ring_of_fire.value_counts()
Out[6]:
True     7188
False    2144
Name: ring_of_fire, dtype: int64
Exercise 6
In [7]:
df.loc[df.ring_of_fire, 'tsunami'].sum()
Out[7]:
45