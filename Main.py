import os
import glob
import subprocess
import pandas as pd
from PIL import Image
import datetime


datetime.timedelta.min
def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

#enter in the directory of your images in the line below
os.chdir('D:/mgickdemo/images')
cwd = os.getcwd()

files = glob.glob('*.jpg')

for i in range(len(files)):
    files[i] = files[i].split(".", 1)[0]

#If you're on a nix based system this needs to be changed from 'magick' to 'convert'
str1 = "magick "
str2 = ".jpg -crop 1728x1152 +repage "
str3 = "_%d.jpg"

for i in range(len(files)):
    tfiles = str1 + files[i] + str2 + files[i] + str3
    subprocess.run(tfiles, shell=True)

subfiles = glob.glob('*_[0-9].jpg')
subfiles = sorted(subfiles)
str4 = " -fuzz 15% -fill black +opaque \"rgb(210,210,20)\" -fuzz 15% -fill white -opaque \"rgb(210,210,20)\" -print \"%[fx:w*h*mean]\" "
#the above line probably needs to be adjusted to capture an appropriate 'green'. Ive been doing this by using the colour picker in photoshop to get RGB
#colourspace values for just one image of the set. both instances of the rgb(x,x,x) need to be changed

      #" -fuzz 11% -fill black +opaque \"rgb(162,159,10)\" -fuzz 11% -fill white -opaque \"rgb(162,159,10)\" -print \"%[fx:w*h*mean]\" "

tl = ["t"] * len(subfiles)
namestamps = ["t"] * len(subfiles)
potnumber = ["t"] * len(subfiles)

col_names = ['Timestamp', 'Pixels']
my_df = pd.DataFrame(columns = col_names)
my_df

#get the first time to subtract from subsequent ones using time delta

for i in range(len(subfiles)):
    tsfiles = str1 + subfiles[i] + str4 + "res" + subfiles[i]
    print(tsfiles)
    tl[i] = subprocess.run(tsfiles, shell=True, capture_output=True).stdout
    tl[i] = tl[i].decode('utf-8')
    namestamps[i] = get_date_taken(subfiles[i])
    temp = get_date_taken(subfiles[i])
    potnumber[i] = subfiles[i].split("_")[2].split(".")[0]

out = pd.DataFrame(list(zip(tl, namestamps, potnumber)))
out.to_csv("out.csv")
print(tl)
print(namestamps)
print(potnumber)
print(out)
