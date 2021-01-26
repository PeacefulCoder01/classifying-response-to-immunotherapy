from os import listdir
from os.path import isfile, join
from DL.data_conversions.txt_to_python_structures import *


path = r'C:\Users\itay\Desktop\Technion studies\Keren Laboratory\python_playground\classifying-response-to-immunotherapy\Data\rna_seq200k\matlab_structures_4.11.20'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
directories = [os.path.join(path, f.replace(".mat", "")) for f in onlyfiles]
new_files = [os.path.join(path, f.replace(".mat", ""), f) for f in onlyfiles]
files = [os.path.join(path, f) for f in onlyfiles]

# create directories
for d in directories:
    os.mkdir(d)

for (file,  new_file) in zip(files, new_files):
    os.rename(file, new_file)
x = 4