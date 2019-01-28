
# -*- coding: UTF-8 -*-
import chardet
import csv
import pandas
import codecs
import numpy as np




dir="000380.txt"
text=''
label=[]
with codecs.open(dir, 'rb') as f:
	for line in f.readlines(): 
		#remove meaningless characters
		line=line.decode('cp1252')
		line=line.replace('ÿþ','')
		line=line.strip(chr(0))
		n=1
		#Because every two characters hava a 0x00 in middle,remove it  
		#n is used to record how many lines and to determine which one is valid
		for i in line:
			if n%2!=0:
				text=text+i
			n=n+1

sentence=text.split('\r')
n=1
sentence2=[]
for i in sentence:
	if n%2==1:
		sentence2.append(i)
	n=n+1

dir="temp.csv"
with open(dir,"w") as csvfile: 
	writer = csv.writer(csvfile) 
	writer.writerow(["wav_filename","transcript"]) #columns_name 

	for i in sentence2:
		il=[]
		il=i.split('\t')
		print(i)
		print(il)
		writer.writerow([str(il[0]).strip()+'.wav',il[1].strip()])#save into csv file
name='000380.csv'
with open(dir) as input, open(name, 'w') as output: 
    non_blank = (line for line in input if line.strip()) 
    output.writelines(non_blank) 


	
