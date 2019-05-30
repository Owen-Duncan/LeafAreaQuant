import os
import glob
import subprocess
import pandas as pd
import PIL

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]


os.chdir('/media/anon/19c1f66f-aa32-4812-9377-1a8cf36493bd/TIFF')
cwd = os.getcwd()

files = glob.glob('*.tif')
for files in files


for i in range(len(files)):
    files[i] = files[i].split(".", 1)[0]

str1 = "convert "
str2 = ".tif -crop 1728x1152 +repage "
str3 = "_%d.tif"


for i in range(len(files)):
    tfiles = str1 + files[i] + str2 + files[i] + str3
    subprocess.run(tfiles, shell=True)

subfiles = glob.glob('*_[0-9].tif')
subfiles = sorted(subfiles)
str4 = " -fuzz 11% -fill black +opaque 'rgb(162, 159, 10)' -fuzz 11% -fill white -opaque 'rgb(162, 159, 10)' -print \"%[fx:w*h*mean]\" "

tl = ["t"] * len(subfiles)
namestamps = ["t"] * len(subfiles)

col_names =  ['Timestamp', 'Pixels']
my_df  = pd.DataFrame(columns = col_names)
my_df

for i in range(len(subfiles)):
    tsfiles = "\n" +str1 +subfiles[i] + str4 + "res" + subfiles[i]
    print(tsfiles)
    tl[i] = subprocess.run(tsfiles, shell=True, capture_output=True).stdout
    tl[i] = tl[i].decode('utf-8')
    namestamps[i] = subfiles[i].split(".", 1)[0]

my_df["Timestamp"] = namestamps
my_df["Pixels"] = tl


