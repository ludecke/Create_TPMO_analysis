import os
import operator
import re
import sys

sys.argv  #sys.argv[1] is the file to upload

output_file = 0
output_file_name = "TPMO_analysis.txt"

#for filename in os.listdir(os.getcwd()+"/tpmo"):
#	with open("tpmo/"+filename) as f:
#		counter = 0
#		for line in f:
#			if counter <= 10:
#				head.append(line)
#			counter+=1


with open(sys.argv[1]) as f:
	username = 0
	copybp = 0
	createbp = 0
	changebp = 0
	otherprop = 0
	correcttr = 0
	negline = 0
	for line in f:
		if line.startswith("|*  "):
			username = repr(re.sub(r'\s', '', (re.sub(r'\|', '', line[11:23]))))
			copybp = int(re.sub(r'\,', '', (re.sub(r'\s', '', (re.sub(r'\.', '', (re.sub(r'\|', '', (line[32:41])))))))))
			createbp = int(re.sub(r'\,', '', (re.sub(r'\s', '', (re.sub(r'\.', '', (re.sub(r'\|', '', (line[42:51])))))))))
			changebp = int(re.sub(r'\,', '', (re.sub(r'\s', '', (re.sub(r'\.', '', (re.sub(r'\|', '', (line[53:60])))))))))
			otherprop = int(re.sub(r'\,', '', (re.sub(r'\s', '', (re.sub(r'\.', '', (re.sub(r'\|', '', (line[63:72])))))))))
			correcttr = int(re.sub(r'\,', '', (re.sub(r'\s', '', (re.sub(r'\.', '', (re.sub(r'\|', '', (line[74:83])))))))))
			tpmolines = int(round(copybp*0.2+createbp+changebp*0.85+otherprop*0.85+correcttr*0.85))
			#print username 
			#print copybp 
			#print createbp
			#print changebp
			#print otherprop
			#print correcttr
			#print negline
			with open(output_file_name, 'a') as g:
				g.write ("{}:\nCopy Best Proposal: {}, Create Best Proposal: {}, Change Best Proposal: {}, Other Proposal: {}, Correct Translation: {}\nEffective TPMO lines: {}\n\n".format(username, copybp, createbp, changebp, otherprop, correcttr, tpmolines))
		if line.startswith("|***  "):
			copybp = int(re.sub(r'\,', '', (re.sub(r'\s', '', (re.sub(r'\.', '', (re.sub(r'\|', '', (line[32:41])))))))))
			createbp = int(re.sub(r'\,', '', (re.sub(r'\s', '', (re.sub(r'\.', '', (re.sub(r'\|', '', (line[42:51])))))))))
			changebp = int(re.sub(r'\,', '', (re.sub(r'\s', '', (re.sub(r'\.', '', (re.sub(r'\|', '', (line[53:60])))))))))
			otherprop = int(re.sub(r'\,', '', (re.sub(r'\s', '', (re.sub(r'\.', '', (re.sub(r'\|', '', (line[63:72])))))))))
			correcttr = int(re.sub(r'\,', '', (re.sub(r'\s', '', (re.sub(r'\.', '', (re.sub(r'\|', '', (line[74:83])))))))))
			tpmolines = int(round(copybp*0.2+createbp+changebp*0.85+otherprop*0.85+correcttr*0.85))
			#print username 
			#print copybp 
			#print createbp
			#print changebp
			#print otherprop
			#print correcttr
			#print negline
			with open(output_file_name, 'a') as g:
				g.write ("Agency Totals:\nCopy Best Proposal: {}, Create Best Proposal: {}, Change Best Proposal: {}, Other Proposal: {}, Correct Translation: {}\nEffective TPMO lines: {}\n\n".format(copybp, createbp, changebp, otherprop, correcttr, tpmolines))		
	



#python 3 auf mac installieren, aufruf mit "python3"
#utf-8 ausgeben




#for string, repetitions in result:

#hausaufgabe: sort dictionary by value
			
#if line.startswith("--"):