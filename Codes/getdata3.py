# os.listdir() will get you everything that's in a directory in the form of list
import os
import sys
from nltk import ngrams
from operator import itemgetter
import time

def create_35_tup(arg):
	temp=1
	list1=[]
	while temp<=4:
		list1.append(arg[temp:temp+3])
		temp+=1
	temp=1
	while temp<=2:
		list1.append(arg[temp:temp+5])
		temp+=1
	return list1

def get_Training_Data_Master_files():
	path_to_folder = "ADFA-LD/Training_Data_Master/"
	list_of_files_in_folder = sorted(os.listdir(path_to_folder))
	for dataset_file in list_of_files_in_folder:
		path_to_dataset_file = path_to_folder + dataset_file
		file_object = open(path_to_dataset_file, "r")
		file_data = file_object.read()
		file_object.close()
		yield file_data

def get_Validation_Data_Master_files():
	path_to_folder = "ADFA-LD/Validation_Data_Master/"
	list_of_files_in_folder = sorted(os.listdir(path_to_folder))
	for dataset_file in list_of_files_in_folder:
		path_to_dataset_file = path_to_folder + dataset_file
		file_object = open(path_to_dataset_file, "r")
		file_data = file_object.read()
		file_object.close()
		yield file_data

def length(di1, di2, di3, x):
	print(x + '-7: ' + str(len(di1)))
	print(x + '-5: ' + str(len(di2)))
	print(x + '-3: ' + str(len(di3)))

def unify(specific_string):
	dictionary_7 = {}
	dictionary_5 = {}
	dictionary_3 = {}
	list_of_text_files = get_Attack_Data_Master_files(specific_string)
	for text_file in list_of_text_files:
		grams_7_list = list(ngrams(text_file.split(), 7))
		for item_gram in grams_7_list:
			if item_gram in dictionary_7:
				dictionary_7[item_gram] = dictionary_7[item_gram] + 1
			else:
				dictionary_7[item_gram] = 1
		Three_Five_list = list(create_35_tup(grams_7_list[len(grams_7_list)-1]))
		for i in range(0,4,1):
			if Three_Five_list[i] in dictionary_3:
				dictionary_3[Three_Five_list[i]] += 1
			else:
				dictionary_3[Three_Five_list[i]] = 1
		for i in range(4,6,1):
			if Three_Five_list[i] in dictionary_5:
				dictionary_5[Three_Five_list[i]] += 1
			else:
				dictionary_5[Three_Five_list[i]] = 1
	for f in dictionary_7:
		if f[0:5] in dictionary_5:
			dictionary_5[f[0:5]] += dictionary_7[f]
		else:
			dictionary_5[f[0:5]] = dictionary_7[f]
	for f in dictionary_7:
		if f[0:3] in dictionary_3:
			dictionary_3[f[0:3]] += dictionary_7[f]
		else:
			dictionary_3[f[0:3]] = dictionary_7[f]
	length(dictionary_7, dictionary_5, dictionary_3, specific_string)
	return dictionary_7, dictionary_5, dictionary_3


def get_Attack_Data_Master_files(folder_type):
	path_to_folders = []
	
	path_to_folders.append("ADFA-LD/Attack_Data_Master/" + folder_type + "_1/")
	path_to_folders.append("ADFA-LD/Attack_Data_Master/" + folder_type + "_2/")
	path_to_folders.append("ADFA-LD/Attack_Data_Master/" + folder_type + "_3/")
	path_to_folders.append("ADFA-LD/Attack_Data_Master/" + folder_type + "_4/")
	path_to_folders.append("ADFA-LD/Attack_Data_Master/" + folder_type + "_5/")
	path_to_folders.append("ADFA-LD/Attack_Data_Master/" + folder_type + "_6/")
	path_to_folders.append("ADFA-LD/Attack_Data_Master/" + folder_type + "_7/")

	for path_to_folder in path_to_folders:
		list_of_files_in_folder = sorted(os.listdir(path_to_folder))
		for dataset_file in list_of_files_in_folder:
			path_to_dataset_file = path_to_folder + dataset_file
			file_object = open(path_to_dataset_file, "r")
			file_data = file_object.read()
			file_object.close()
			yield file_data

start_time = time.time()

dictionary_Adduser, dictionary_Adduser_5tuple, dictionary_Adduser_3tuple = unify("Adduser")
'''
List_Of_Text_File_Objects_Adduser = get_Attack_Data_Master_files("Adduser")
dictionary_Adduser={}
dictionary_Adduser_5tuple={}
dictionary_Adduser_3tuple={}
for Text_File_Object in List_Of_Text_File_Objects_Adduser:
	seven_grams_list = list(ngrams(Text_File_Object.split(), 7))
	for f in seven_grams_list:
		if f in dictionary_Adduser:
			dictionary_Adduser[f] = dictionary_Adduser[f] + 1
		else:
			dictionary_Adduser[f] = 1
	Three_Five_list = list(create_35_tup(seven_grams_list[len(seven_grams_list)-1]))
	for i in range(0,4,1):
		if Three_Five_list[i] in dictionary_Adduser_3tuple:
			dictionary_Adduser_3tuple[Three_Five_list[i]] += 1
		else:
			dictionary_Adduser_3tuple[Three_Five_list[i]] = 1
	for i in range(4,6,1):
		if Three_Five_list[i] in dictionary_Adduser_5tuple:
			dictionary_Adduser_5tuple[Three_Five_list[i]] += 1
		else:
			dictionary_Adduser_5tuple[Three_Five_list[i]] = 1
for f in dictionary_Adduser:
	if f[0:5] in dictionary_Adduser_5tuple:
		dictionary_Adduser_5tuple[f[0:5]] += dictionary_Adduser[f]
	else:
		dictionary_Adduser_5tuple[f[0:5]] = dictionary_Adduser[f]
for f in dictionary_Adduser:
	if f[0:3] in dictionary_Adduser_3tuple:
		dictionary_Adduser_3tuple[f[0:3]] += dictionary_Adduser[f]
	else:
		dictionary_Adduser_3tuple[f[0:3]] = dictionary_Adduser[f]
'''
dictionary_HydraFTP, dictionary_HydraFTP_5tuple, dictionary_HydraFTP_3tuple = unify("Hydra_FTP")
'''
List_Of_Text_File_Objects_HydraFTP = get_Attack_Data_Master_files("Hydra_FTP")
dictionary_HydraFTP={}
dictionary_HydraFTP_5tuple={}
dictionary_HydraFTP_3tuple={}
for Text_File_Object in List_Of_Text_File_Objects_HydraFTP:
	seven_grams_list = list(ngrams(Text_File_Object.split(), 7))
	for f in seven_grams_list:
		if f in dictionary_HydraFTP:
			dictionary_HydraFTP[f] = dictionary_HydraFTP[f] + 1
		else:
			dictionary_HydraFTP[f] = 1
	Three_Five_list = list(create_35_tup(seven_grams_list[len(seven_grams_list)-1]))
	for i in range(0,4,1):
		if Three_Five_list[i] in dictionary_HydraFTP_3tuple:
			dictionary_HydraFTP_3tuple[Three_Five_list[i]] += 1
		else:
			dictionary_HydraFTP_3tuple[Three_Five_list[i]] = 1
	for i in range(4,6,1):
		if Three_Five_list[i] in dictionary_HydraFTP_5tuple:
			dictionary_HydraFTP_5tuple[Three_Five_list[i]] += 1
		else:
			dictionary_HydraFTP_5tuple[Three_Five_list[i]] = 1
for f in dictionary_HydraFTP:
	if f[0:5] in dictionary_HydraFTP_5tuple:
		dictionary_HydraFTP_5tuple[f[0:5]] += dictionary_HydraFTP[f]
	else:
		dictionary_HydraFTP_5tuple[f[0:5]] = dictionary_HydraFTP[f]
for f in dictionary_HydraFTP:
	if f[0:3] in dictionary_HydraFTP_3tuple:
		dictionary_HydraFTP_3tuple[f[0:3]] += dictionary_HydraFTP[f]
	else:
		dictionary_HydraFTP_3tuple[f[0:3]] = dictionary_HydraFTP[f]
'''
dictionary_HydraSSH, dictionary_HydraSSH_5tuple, dictionary_HydraSSH_3tuple = unify("Hydra_SSH")
'''
List_Of_Text_File_Objects_HydraSSH = get_Attack_Data_Master_files("Hydra_SSH")
dictionary_HydraSSH={}
dictionary_HydraSSH_5tuple={}
dictionary_HydraSSH_3tuple={}
for Text_File_Object in List_Of_Text_File_Objects_HydraSSH:
	seven_grams_list = list(ngrams(Text_File_Object.split(), 7))
	for f in seven_grams_list:
		if f in dictionary_HydraSSH:
			dictionary_HydraSSH[f] = dictionary_HydraSSH[f] + 1
		else:
			dictionary_HydraSSH[f] = 1
	Three_Five_list = list(create_35_tup(seven_grams_list[len(seven_grams_list)-1]))
	for i in range(0,4,1):
		if Three_Five_list[i] in dictionary_HydraSSH_3tuple:
			dictionary_HydraSSH_3tuple[Three_Five_list[i]] += 1
		else:
			dictionary_HydraSSH_3tuple[Three_Five_list[i]] = 1
	for i in range(4,6,1):
		if Three_Five_list[i] in dictionary_HydraSSH_5tuple:
			dictionary_HydraSSH_5tuple[Three_Five_list[i]] += 1
		else:
			dictionary_HydraSSH_5tuple[Three_Five_list[i]] = 1
for f in dictionary_HydraSSH:
	if f[0:5] in dictionary_HydraSSH_5tuple:
		dictionary_HydraSSH_5tuple[f[0:5]] += dictionary_HydraSSH[f]
	else:
		dictionary_HydraSSH_5tuple[f[0:5]] = dictionary_HydraSSH[f]
for f in dictionary_HydraSSH:
	if f[0:3] in dictionary_HydraSSH_3tuple:
		dictionary_HydraSSH_3tuple[f[0:3]] += dictionary_HydraSSH[f]
	else:
		dictionary_HydraSSH_3tuple[f[0:3]] = dictionary_HydraSSH[f]
'''
dictionary_JavaMeterpreter, dictionary_JavaMeterpreter_5tuple, dictionary_JavaMeterpreter_3tuple = unify("Java_Meterpreter")
'''
List_Of_Text_File_Objects_Java_Meterpreter = get_Attack_Data_Master_files("Java_Meterpreter")
dictionary_JavaMeterpreter={}
dictionary_JavaMeterpreter_5tuple={}
dictionary_JavaMeterpreter_3tuple={}
for Text_File_Object in List_Of_Text_File_Objects_Java_Meterpreter:
	seven_grams_list = list(ngrams(Text_File_Object.split(), 7))
	for f in seven_grams_list:
		if f in dictionary_JavaMeterpreter:
			dictionary_JavaMeterpreter[f] = dictionary_JavaMeterpreter[f] + 1
		else:
			dictionary_JavaMeterpreter[f] = 1
	Three_Five_list = list(create_35_tup(seven_grams_list[len(seven_grams_list)-1]))
	for i in range(0,4,1):
		if Three_Five_list[i] in dictionary_JavaMeterpreter_3tuple:
			dictionary_JavaMeterpreter_3tuple[Three_Five_list[i]] += 1
		else:
			dictionary_JavaMeterpreter_3tuple[Three_Five_list[i]] = 1
	for i in range(4,6,1):
		if Three_Five_list[i] in dictionary_JavaMeterpreter_5tuple:
			dictionary_JavaMeterpreter_5tuple[Three_Five_list[i]] += 1
		else:
			dictionary_JavaMeterpreter_5tuple[Three_Five_list[i]] = 1
for f in dictionary_JavaMeterpreter:
	if f[0:5] in dictionary_JavaMeterpreter_5tuple:
		dictionary_JavaMeterpreter_5tuple[f[0:5]] += dictionary_JavaMeterpreter[f]
	else:
		dictionary_JavaMeterpreter_5tuple[f[0:5]] = dictionary_JavaMeterpreter[f]
for f in dictionary_JavaMeterpreter:
	if f[0:3] in dictionary_JavaMeterpreter_3tuple:
		dictionary_JavaMeterpreter_3tuple[f[0:3]] += dictionary_JavaMeterpreter[f]
	else:
		dictionary_JavaMeterpreter_3tuple[f[0:3]] = dictionary_JavaMeterpreter[f]
'''
dictionary_Meterpreter, dictionary_Meterpreter_5tuple, dictionary_Meterpreter_3tuple = unify("Meterpreter")
'''
List_Of_Text_File_Objects_Meterpreter = get_Attack_Data_Master_files("Meterpreter")
dictionary_Meterpreter={}
dictionary_Meterpreter_5tuple={}
dictionary_Meterpreter_3tuple={}
for Text_File_Object in List_Of_Text_File_Objects_Meterpreter:
	seven_grams_list = list(ngrams(Text_File_Object.split(), 7))
	for f in seven_grams_list:
		if f in dictionary_Meterpreter:
			dictionary_Meterpreter[f] = dictionary_Meterpreter[f] + 1
		else:
			dictionary_Meterpreter[f] = 1
	Three_Five_list = list(create_35_tup(seven_grams_list[len(seven_grams_list)-1]))
	for i in range(0,4,1):
		if Three_Five_list[i] in dictionary_Meterpreter_3tuple:
			dictionary_Meterpreter_3tuple[Three_Five_list[i]] += 1
		else:
			dictionary_Meterpreter_3tuple[Three_Five_list[i]] = 1
	for i in range(4,6,1):
		if Three_Five_list[i] in dictionary_Meterpreter_5tuple:
			dictionary_Meterpreter_5tuple[Three_Five_list[i]] += 1
		else:
			dictionary_Meterpreter_5tuple[Three_Five_list[i]] = 1
for f in dictionary_Meterpreter:
	if f[0:5] in dictionary_Meterpreter_5tuple:
		dictionary_Meterpreter_5tuple[f[0:5]] += dictionary_Meterpreter[f]
	else:
		dictionary_Meterpreter_5tuple[f[0:5]] = dictionary_Meterpreter[f]
for f in dictionary_Meterpreter:
	if f[0:3] in dictionary_Meterpreter_3tuple:
		dictionary_Meterpreter_3tuple[f[0:3]] += dictionary_Meterpreter[f]
	else:
		dictionary_Meterpreter_3tuple[f[0:3]] = dictionary_Meterpreter[f]
'''
dictionary_WebShell, dictionary_WebShell_5tuple, dictionary_WebShell_3tuple = unify("Web_Shell")
'''
List_Of_Text_File_Objects_Web_Shell = get_Attack_Data_Master_files("Web_Shell")
dictionary_WebShell={}
dictionary_WebShell_5tuple={}
dictionary_WebShell_3tuple={}
for Text_File_Object in List_Of_Text_File_Objects_Web_Shell:
	seven_grams_list = list(ngrams(Text_File_Object.split(), 7))
	for f in seven_grams_list:
		if f in dictionary_WebShell:
			dictionary_WebShell[f] = dictionary_WebShell[f] + 1
		else:
			dictionary_WebShell[f] = 1
	Three_Five_list = list(create_35_tup(seven_grams_list[len(seven_grams_list)-1]))
	for i in range(0,4,1):
		if Three_Five_list[i] in dictionary_WebShell_3tuple:
			dictionary_WebShell_3tuple[Three_Five_list[i]] += 1
		else:
			dictionary_WebShell_3tuple[Three_Five_list[i]] = 1
	for i in range(4,6,1):
		if Three_Five_list[i] in dictionary_WebShell_5tuple:
			dictionary_WebShell_5tuple[Three_Five_list[i]] += 1
		else:
			dictionary_WebShell_5tuple[Three_Five_list[i]] = 1
for f in dictionary_WebShell:
	if f[0:5] in dictionary_WebShell_5tuple:
		dictionary_WebShell_5tuple[f[0:5]] += dictionary_WebShell[f]
	else:
		dictionary_WebShell_5tuple[f[0:5]] = dictionary_WebShell[f]
for f in dictionary_WebShell:
	if f[0:3] in dictionary_WebShell_3tuple:
		dictionary_WebShell_3tuple[f[0:3]] += dictionary_WebShell[f]
	else:
		dictionary_WebShell_3tuple[f[0:3]] = dictionary_WebShell[f]
'''
List_Of_Text_File_Objects_Training = get_Training_Data_Master_files()

dictionary_Training =  {}
dictionary_Training_5tuple = {}
dictionary_Training_3tuple = {}

for Text_File_Object in List_Of_Text_File_Objects_Training:
	seven_grams_list = list(ngrams(Text_File_Object.split(), 7))
	for f in seven_grams_list:
		if f in dictionary_Training:
			dictionary_Training[f] = dictionary_Training[f] + 1
		else:
			dictionary_Training[f] = 1
	Three_Five_list = list(create_35_tup(seven_grams_list[len(seven_grams_list)-1]))
	for i in range(0,4,1):
		if Three_Five_list[i] in dictionary_Training_3tuple:
			dictionary_Training_3tuple[Three_Five_list[i]] += 1
		else:
			dictionary_Training_3tuple[Three_Five_list[i]] = 1
	for i in range(4,6,1):
		if Three_Five_list[i] in dictionary_Training_5tuple:
			dictionary_Training_5tuple[Three_Five_list[i]] += 1
		else:
			dictionary_Training_5tuple[Three_Five_list[i]] = 1

for f in dictionary_Training:
	if f[0:5] in dictionary_Training_5tuple:
		dictionary_Training_5tuple[f[0:5]] += dictionary_Training[f]
	else:
		dictionary_Training_5tuple[f[0:5]] = dictionary_Training[f]
for f in dictionary_Training:
	if f[0:3] in dictionary_Training_3tuple:
		dictionary_Training_3tuple[f[0:3]] += dictionary_Training[f]
	else:
		dictionary_Training_3tuple[f[0:3]] = dictionary_Training[f]

print("----------------------------------------------------------------------------------")
for s in dictionary_Adduser:
	print(s)
print("----------------------------------------------------------------------------------")
Sorted_List_Training = sorted(dictionary_Training, key=dictionary_Training.__getitem__, reverse = True)
Sorted_List_Adduser = sorted(dictionary_Adduser, key=dictionary_Adduser.__getitem__, reverse = True)
Sorted_List_HydraFTP = sorted(dictionary_HydraFTP, key=dictionary_HydraFTP.__getitem__, reverse = True)
Sorted_List_HydraSSH = sorted(dictionary_HydraSSH, key=dictionary_HydraSSH.__getitem__, reverse = True)
Sorted_List_JavaMeterpreter = sorted(dictionary_JavaMeterpreter, key=dictionary_JavaMeterpreter.__getitem__, reverse = True)
Sorted_List_Meterpreter = sorted(dictionary_Meterpreter, key=dictionary_Meterpreter.__getitem__, reverse = True)
Sorted_List_WebShell = sorted(dictionary_WebShell, key=dictionary_WebShell.__getitem__, reverse = True)

print(len(Sorted_List_Adduser))
print(len(Sorted_List_HydraFTP))
print(len(Sorted_List_HydraSSH))
print(len(Sorted_List_JavaMeterpreter))
print(len(Sorted_List_Meterpreter))
print(len(Sorted_List_WebShell))
print(len(Sorted_List_Training))

Sorted_List_All_Top30={}
for s in Sorted_List_Adduser[:int(0.3*len(Sorted_List_Adduser))]:
	if s in Sorted_List_All_Top30:
		continue
	else:
		Sorted_List_All_Top30[s] = 1
for s in Sorted_List_HydraFTP[:int(0.3*len(Sorted_List_HydraFTP))]:
	if s in Sorted_List_All_Top30:
		continue
	else:
		Sorted_List_All_Top30[s] = 1
for s in Sorted_List_HydraSSH[:int(0.3*len(Sorted_List_HydraSSH))]:
	if s in Sorted_List_All_Top30:
		continue
	else:
		Sorted_List_All_Top30[s] = 1
for s in Sorted_List_JavaMeterpreter[:int(0.3*len(Sorted_List_JavaMeterpreter))]:
	if s in Sorted_List_All_Top30:
		continue
	else:
		Sorted_List_All_Top30[s] = 1
for s in Sorted_List_Meterpreter[:int(0.3*len(Sorted_List_Meterpreter))]:
	if s in Sorted_List_All_Top30:
		continue
	else:
		Sorted_List_All_Top30[s] = 1
for s in Sorted_List_WebShell[:int(0.3*len(Sorted_List_WebShell))]:
	if s in Sorted_List_All_Top30:
		continue
	else:
		Sorted_List_All_Top30[s] = 1
for s in Sorted_List_Training[:int(0.3*len(Sorted_List_Training))]:
	if s in Sorted_List_All_Top30:
		continue
	else:
		Sorted_List_All_Top30[s] = 1
Write_File_Object = open("Write_File.txt","w")
Write_File_Object.write("Adduser \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30 and Sorted_List_Adduser)))
Write_File_Object.write("\n Hydra_FTP \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30 and Sorted_List_HydraFTP)))
Write_File_Object.write("\n Hydra_SSH \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30 and Sorted_List_HydraSSH)))
Write_File_Object.write("\n Java_Meterpreter \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30 and Sorted_List_JavaMeterpreter)))
Write_File_Object.write("\n Meterpreter \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30 and Sorted_List_Meterpreter)))
Write_File_Object.write("\n Web_Shell \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30 and Sorted_List_WebShell)))

Write_File_Object_Freq = open("Write_File_Freq.txt","w")
Write_File_Object_Freq.write("Adduser \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_Adduser[s]), Sorted_List_All_Top30 and Sorted_List_Adduser)))
Write_File_Object_Freq.write("\n Hydra_FTP \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_HydraFTP[s]), Sorted_List_All_Top30 and Sorted_List_HydraFTP)))
Write_File_Object_Freq.write("\n Hydra_SSH \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_HydraSSH[s]), Sorted_List_All_Top30 and Sorted_List_HydraSSH)))
Write_File_Object_Freq.write("\n Java_Meterpreter \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_JavaMeterpreter[s]), Sorted_List_All_Top30 and Sorted_List_JavaMeterpreter)))
Write_File_Object_Freq.write("\n Meterpreter \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_Meterpreter[s]), Sorted_List_All_Top30 and Sorted_List_Meterpreter)))
Write_File_Object_Freq.write("\n Web_Shell \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_WebShell[s]), Sorted_List_All_Top30 and Sorted_List_WebShell)))

Sorted_List_Adduser_5tuple = sorted(dictionary_Adduser_5tuple, key=dictionary_Adduser_5tuple.__getitem__, reverse = True)
Sorted_List_HydraFTP_5tuple = sorted(dictionary_HydraFTP_5tuple, key=dictionary_HydraFTP_5tuple.__getitem__, reverse = True)
Sorted_List_HydraSSH_5tuple = sorted(dictionary_HydraSSH_5tuple, key=dictionary_HydraSSH_5tuple.__getitem__, reverse = True)
Sorted_List_JavaMeterpreter_5tuple = sorted(dictionary_JavaMeterpreter_5tuple, key=dictionary_JavaMeterpreter_5tuple.__getitem__, reverse = True)
Sorted_List_Meterpreter_5tuple = sorted(dictionary_Meterpreter_5tuple, key=dictionary_Meterpreter_5tuple.__getitem__, reverse = True)
Sorted_List_Webshell_5tuple = sorted(dictionary_WebShell_5tuple, key=dictionary_WebShell_5tuple.__getitem__, reverse = True)

Sorted_List_All_Top30_5tuple=[]
for s in Sorted_List_Adduser_5tuple[:int(0.3*len(Sorted_List_Adduser_5tuple))]:
	Sorted_List_All_Top30_5tuple.append(s)
for s in Sorted_List_HydraFTP_5tuple[:int(0.3*len(Sorted_List_HydraFTP_5tuple))]:
	Sorted_List_All_Top30_5tuple.append(s)
for s in Sorted_List_HydraSSH_5tuple[:int(0.3*len(Sorted_List_HydraSSH_5tuple))]:
	Sorted_List_All_Top30_5tuple.append(s)
for s in Sorted_List_JavaMeterpreter_5tuple[:int(0.3*len(Sorted_List_JavaMeterpreter_5tuple))]:
	Sorted_List_All_Top30_5tuple.append(s)
for s in Sorted_List_Meterpreter_5tuple[:int(0.3*len(Sorted_List_Meterpreter_5tuple))]:
	Sorted_List_All_Top30_5tuple.append(s)
for s in Sorted_List_Webshell_5tuple[:int(0.3*len(Sorted_List_Webshell_5tuple))]:
	Sorted_List_All_Top30_5tuple.append(s)

Write_File_Object = open("Write_File_5tuple.txt","w")
Write_File_Object.write("Adduser_5tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_5tuple and Sorted_List_Adduser_5tuple)))
Write_File_Object.write("\n Hydra_FTP_5tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_5tuple and Sorted_List_HydraFTP_5tuple)))
Write_File_Object.write("\n Hydra_SSH_5tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_5tuple and Sorted_List_HydraSSH_5tuple)))
Write_File_Object.write("\n Java_Meterpreter_5tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_5tuple and Sorted_List_JavaMeterpreter_5tuple)))
Write_File_Object.write("\n Meterpreter_5tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_5tuple and Sorted_List_Meterpreter_5tuple)))
Write_File_Object.write("\n Web_Shell_5tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_5tuple and Sorted_List_Webshell_5tuple)))

Write_File_Object_Freq = open("Write_File_Freq_5tuple.txt","w")
Write_File_Object_Freq.write("Adduser_5tuple \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_Adduser_5tuple[s]), Sorted_List_All_Top30_5tuple and Sorted_List_Adduser_5tuple)))
Write_File_Object_Freq.write("\n Hydra_FTP \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_HydraFTP_5tuple[s]), Sorted_List_All_Top30_5tuple and Sorted_List_HydraFTP_5tuple)))
Write_File_Object_Freq.write("\n Hydra_SSH_5tuple \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_HydraSSH_5tuple[s]), Sorted_List_All_Top30_5tuple and Sorted_List_HydraSSH_5tuple)))
Write_File_Object_Freq.write("\n Java_Meterpreter_5tuple \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_JavaMeterpreter_5tuple[s]), Sorted_List_All_Top30_5tuple and Sorted_List_JavaMeterpreter_5tuple)))
Write_File_Object_Freq.write("\n Meterpreter_5tuple \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_Meterpreter_5tuple[s]), Sorted_List_All_Top30_5tuple and Sorted_List_Meterpreter_5tuple)))
Write_File_Object_Freq.write("\n Web_Shell_5tuple \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_WebShell_5tuple[s]), Sorted_List_All_Top30_5tuple and Sorted_List_Webshell_5tuple)))

Sorted_List_Adduser_3tuple = sorted(dictionary_Adduser_3tuple, key=dictionary_Adduser_3tuple.__getitem__, reverse = True)
Sorted_List_HydraFTP_3tuple = sorted(dictionary_HydraFTP_3tuple, key=dictionary_HydraFTP_3tuple.__getitem__, reverse = True)
Sorted_List_HydraSSH_3tuple = sorted(dictionary_HydraSSH_3tuple, key=dictionary_HydraSSH_3tuple.__getitem__, reverse = True)
Sorted_List_JavaMeterpreter_3tuple = sorted(dictionary_JavaMeterpreter_3tuple, key=dictionary_JavaMeterpreter_3tuple.__getitem__, reverse = True)
Sorted_List_Meterpreter_3tuple = sorted(dictionary_Meterpreter_3tuple, key=dictionary_Meterpreter_3tuple.__getitem__, reverse = True)
Sorted_List_Webshell_3tuple = sorted(dictionary_WebShell_3tuple, key=dictionary_WebShell_3tuple.__getitem__, reverse = True)

Sorted_List_All_Top30_3tuple=[]
for s in Sorted_List_Adduser_3tuple[:int(0.3*len(Sorted_List_Adduser_3tuple))]:
	Sorted_List_All_Top30_3tuple.append(s)
for s in Sorted_List_HydraFTP_3tuple[:int(0.3*len(Sorted_List_HydraFTP_3tuple))]:
	Sorted_List_All_Top30_3tuple.append(s)
for s in Sorted_List_HydraSSH_3tuple[:int(0.3*len(Sorted_List_HydraSSH_3tuple))]:
	Sorted_List_All_Top30_3tuple.append(s)
for s in Sorted_List_JavaMeterpreter_3tuple[:int(0.3*len(Sorted_List_JavaMeterpreter_3tuple))]:
	Sorted_List_All_Top30_3tuple.append(s)
for s in Sorted_List_Meterpreter_3tuple[:int(0.3*len(Sorted_List_Meterpreter_3tuple))]:
	Sorted_List_All_Top30_3tuple.append(s)
for s in Sorted_List_Webshell_3tuple[:int(0.3*len(Sorted_List_Webshell_3tuple))]:
	Sorted_List_All_Top30_3tuple.append(s)

Write_File_Object = open("Write_File_3tuple.txt","w")
Write_File_Object.write("Adduser_3tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_3tuple and Sorted_List_Adduser_3tuple)))
Write_File_Object.write("\n Hydra_FTP_3tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_3tuple and Sorted_List_HydraFTP_3tuple)))
Write_File_Object.write("\n Hydra_SSH_3tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_3tuple and Sorted_List_HydraSSH_3tuple)))
Write_File_Object.write("\n Java_Meterpreter_3tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_3tuple and Sorted_List_JavaMeterpreter_3tuple)))
Write_File_Object.write("\n Meterpreter_3tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_3tuple and Sorted_List_Meterpreter_3tuple)))
Write_File_Object.write("\n Web_Shell_3tuple \n")
Write_File_Object.write("\n".join(map(lambda s: str(s), Sorted_List_All_Top30_3tuple and Sorted_List_Webshell_3tuple)))

Write_File_Object_Freq = open("Write_File_Freq_3tuple.txt","w")
Write_File_Object_Freq.write("Adduser_3tuple \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_Adduser_3tuple[s]), Sorted_List_All_Top30_3tuple and Sorted_List_Adduser_3tuple)))
Write_File_Object_Freq.write("\n Hydra_FTP \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_HydraFTP_3tuple[s]), Sorted_List_All_Top30_3tuple and Sorted_List_HydraFTP_3tuple)))
Write_File_Object_Freq.write("\n Hydra_SSH_3tuple \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_HydraSSH_3tuple[s]), Sorted_List_All_Top30_3tuple and Sorted_List_HydraSSH_3tuple)))
Write_File_Object_Freq.write("\n Java_Meterpreter_3tuple \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_JavaMeterpreter_3tuple[s]), Sorted_List_All_Top30_3tuple and Sorted_List_JavaMeterpreter_3tuple)))
Write_File_Object_Freq.write("\n Meterpreter_3tuple \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_Meterpreter_3tuple[s]), Sorted_List_All_Top30_3tuple and Sorted_List_Meterpreter_3tuple)))
Write_File_Object_Freq.write("\n Web_Shell_3tuple \n")
Write_File_Object_Freq.write("\n".join(map(lambda s: str(dictionary_WebShell_3tuple[s]), Sorted_List_All_Top30_3tuple and Sorted_List_Webshell_3tuple)))


print("--- %s seconds ---" % (time.time() - start_time))
print(len(Sorted_List_All_Top30))
print(len(Sorted_List_All_Top30_3tuple))
print(len(Sorted_List_All_Top30_5tuple))