# os.listdir() will get you everything that's in a directory in the form of list
import os
import sys
from nltk import ngrams
from operator import itemgetter
import time
import collections

def get_new_file_ob(Text_File_Object, addition_string):
	text_file_path = Text_File_Object.name
	new_text_file_path = text_file_path[:-4]
	new_text_file_path = new_text_file_path + "_" + addition_string + ".txt"
	return new_text_file_path

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
	dictionary_7 = collections.OrderedDict()
	dictionary_5 = collections.OrderedDict()
	dictionary_3 = collections.OrderedDict()
	list_of_text_files = get_Attack_Data_Master_files(specific_string)
	for text_file in list_of_text_files:
		grams_7_list = list(ngrams(text_file.split(), 7))
		for item_gram in grams_7_list:
			if item_gram in dictionary_7:
				dictionary_7[item_gram] = dictionary_7[item_gram] + 1
			else:
				dictionary_7[item_gram] = 1
		grams_5_list = list(ngrams(text_file.split(), 5))
		for item_gram in grams_5_list:
			if item_gram in dictionary_5:
				dictionary_5[item_gram] = dictionary_5[item_gram] + 1
			else:
				dictionary_5[item_gram] = 1
		grams_3_list = list(ngrams(text_file.split(), 3))
		for item_gram in grams_3_list:
			if item_gram in dictionary_3:
				dictionary_3[item_gram] = dictionary_3[item_gram] + 1
			else:
				dictionary_3[item_gram] = 1
		
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

def sec_get_Attack_Data_Master_files(folder_type):
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
			yield file_object

start_time = time.time()

dictionary_Adduser, dictionary_Adduser_5tuple, dictionary_Adduser_3tuple = unify("Adduser")

dictionary_HydraFTP, dictionary_HydraFTP_5tuple, dictionary_HydraFTP_3tuple = unify("Hydra_FTP")

dictionary_HydraSSH, dictionary_HydraSSH_5tuple, dictionary_HydraSSH_3tuple = unify("Hydra_SSH")

dictionary_JavaMeterpreter, dictionary_JavaMeterpreter_5tuple, dictionary_JavaMeterpreter_3tuple = unify("Java_Meterpreter")

dictionary_Meterpreter, dictionary_Meterpreter_5tuple, dictionary_Meterpreter_3tuple = unify("Meterpreter")

dictionary_WebShell, dictionary_WebShell_5tuple, dictionary_WebShell_3tuple = unify("Web_Shell")

List_Of_Text_File_Objects_Training = get_Training_Data_Master_files()

dictionary_Training =  collections.OrderedDict()
dictionary_Training_5tuple = collections.OrderedDict()
dictionary_Training_3tuple = collections.OrderedDict()

for Text_File_Object in List_Of_Text_File_Objects_Training:
	seven_grams_list = list(ngrams(Text_File_Object.split(), 7))
	for f in seven_grams_list:
		if f in dictionary_Training:
			dictionary_Training[f] = dictionary_Training[f] + 1
		else:
			dictionary_Training[f] = 1
	five_grams_list = list(ngrams(Text_File_Object.split(), 5))
	for f in five_grams_list:
		if f in dictionary_Training_5tuple:
			dictionary_Training_5tuple[f] = dictionary_Training_5tuple[f] + 1
		else:
			dictionary_Training_5tuple[f] = 1
	three_grams_list = list(ngrams(Text_File_Object.split(), 3))
	for f in three_grams_list:
		if f in dictionary_Training_3tuple:
			dictionary_Training_3tuple[f] = dictionary_Training_3tuple[f] + 1
		else:
			dictionary_Training_3tuple[f] = 1


Sorted_List_Training = sorted(dictionary_Training, key=dictionary_Training.__getitem__, reverse = True)
Sorted_List_Adduser = sorted(dictionary_Adduser, key=dictionary_Adduser.__getitem__, reverse = True)
Sorted_List_HydraFTP = sorted(dictionary_HydraFTP, key=dictionary_HydraFTP.__getitem__, reverse = True)
Sorted_List_HydraSSH = sorted(dictionary_HydraSSH, key=dictionary_HydraSSH.__getitem__, reverse = True)
Sorted_List_JavaMeterpreter = sorted(dictionary_JavaMeterpreter, key=dictionary_JavaMeterpreter.__getitem__, reverse = True)
Sorted_List_Meterpreter = sorted(dictionary_Meterpreter, key=dictionary_Meterpreter.__getitem__, reverse = True)
Sorted_List_WebShell = sorted(dictionary_WebShell, key=dictionary_WebShell.__getitem__, reverse = True)


Sorted_List_All_Top30=collections.OrderedDict()
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



Sorted_List_Training_5tuple = sorted(dictionary_Training_5tuple, key=dictionary_Training_5tuple.__getitem__, reverse = True)
Sorted_List_Adduser_5tuple = sorted(dictionary_Adduser_5tuple, key=dictionary_Adduser_5tuple.__getitem__, reverse = True)
Sorted_List_HydraFTP_5tuple = sorted(dictionary_HydraFTP_5tuple, key=dictionary_HydraFTP_5tuple.__getitem__, reverse = True)
Sorted_List_HydraSSH_5tuple = sorted(dictionary_HydraSSH_5tuple, key=dictionary_HydraSSH_5tuple.__getitem__, reverse = True)
Sorted_List_JavaMeterpreter_5tuple = sorted(dictionary_JavaMeterpreter_5tuple, key=dictionary_JavaMeterpreter_5tuple.__getitem__, reverse = True)
Sorted_List_Meterpreter_5tuple = sorted(dictionary_Meterpreter_5tuple, key=dictionary_Meterpreter_5tuple.__getitem__, reverse = True)
Sorted_List_Webshell_5tuple = sorted(dictionary_WebShell_5tuple, key=dictionary_WebShell_5tuple.__getitem__, reverse = True)

Sorted_List_All_Top30_5tuple=collections.OrderedDict()
for s in Sorted_List_Adduser_5tuple[:int(0.3*len(Sorted_List_Adduser_5tuple))]:
	if s in Sorted_List_All_Top30_5tuple:
		continue
	else:
		Sorted_List_All_Top30_5tuple[s] = 1
for s in Sorted_List_HydraFTP_5tuple[:int(0.3*len(Sorted_List_HydraFTP_5tuple))]:
	if s in Sorted_List_All_Top30_5tuple:
		continue
	else:
		Sorted_List_All_Top30_5tuple[s] = 1
for s in Sorted_List_HydraSSH_5tuple[:int(0.3*len(Sorted_List_HydraSSH_5tuple))]:
	if s in Sorted_List_All_Top30_5tuple:
		continue
	else:
		Sorted_List_All_Top30_5tuple[s] = 1
for s in Sorted_List_JavaMeterpreter_5tuple[:int(0.3*len(Sorted_List_JavaMeterpreter_5tuple))]:
	if s in Sorted_List_All_Top30_5tuple:
		continue
	else:
		Sorted_List_All_Top30_5tuple[s] = 1
for s in Sorted_List_Meterpreter_5tuple[:int(0.3*len(Sorted_List_Meterpreter_5tuple))]:
	if s in Sorted_List_All_Top30_5tuple:
		continue
	else:
		Sorted_List_All_Top30_5tuple[s] = 1
for s in Sorted_List_Webshell_5tuple[:int(0.3*len(Sorted_List_Webshell_5tuple))]:
	if s in Sorted_List_All_Top30_5tuple:
		continue
	else:
		Sorted_List_All_Top30_5tuple[s] = 1
for s in Sorted_List_Training_5tuple[:int(0.3*len(Sorted_List_Training_5tuple))]:
	if s in Sorted_List_All_Top30_5tuple:
		continue
	else:
		Sorted_List_All_Top30_5tuple[s] = 1


Sorted_List_Training_3tuple = sorted(dictionary_Training_3tuple, key=dictionary_Training_3tuple.__getitem__, reverse = True)
Sorted_List_Adduser_3tuple = sorted(dictionary_Adduser_3tuple, key=dictionary_Adduser_3tuple.__getitem__, reverse = True)
Sorted_List_HydraFTP_3tuple = sorted(dictionary_HydraFTP_3tuple, key=dictionary_HydraFTP_3tuple.__getitem__, reverse = True)
Sorted_List_HydraSSH_3tuple = sorted(dictionary_HydraSSH_3tuple, key=dictionary_HydraSSH_3tuple.__getitem__, reverse = True)
Sorted_List_JavaMeterpreter_3tuple = sorted(dictionary_JavaMeterpreter_3tuple, key=dictionary_JavaMeterpreter_3tuple.__getitem__, reverse = True)
Sorted_List_Meterpreter_3tuple = sorted(dictionary_Meterpreter_3tuple, key=dictionary_Meterpreter_3tuple.__getitem__, reverse = True)
Sorted_List_Webshell_3tuple = sorted(dictionary_WebShell_3tuple, key=dictionary_WebShell_3tuple.__getitem__, reverse = True)

Sorted_List_All_Top30_3tuple=collections.OrderedDict()
for s in Sorted_List_Adduser_3tuple[:int(0.3*len(Sorted_List_Adduser_3tuple))]:
	if s in Sorted_List_All_Top30_3tuple:
		continue
	else:
		Sorted_List_All_Top30_3tuple[s] = 1
for s in Sorted_List_HydraFTP_3tuple[:int(0.3*len(Sorted_List_HydraFTP_3tuple))]:
	if s in Sorted_List_All_Top30_3tuple:
		continue
	else:
		Sorted_List_All_Top30_3tuple[s] = 1
for s in Sorted_List_HydraSSH_3tuple[:int(0.3*len(Sorted_List_HydraSSH_3tuple))]:
	if s in Sorted_List_All_Top30_3tuple:
		continue
	else:
		Sorted_List_All_Top30_3tuple[s] = 1
for s in Sorted_List_JavaMeterpreter_3tuple[:int(0.3*len(Sorted_List_JavaMeterpreter_3tuple))]:
	if s in Sorted_List_All_Top30_3tuple:
		continue
	else:
		Sorted_List_All_Top30_3tuple[s] = 1
for s in Sorted_List_Meterpreter_3tuple[:int(0.3*len(Sorted_List_Meterpreter_3tuple))]:
	if s in Sorted_List_All_Top30_3tuple:
		continue
	else:
		Sorted_List_All_Top30_3tuple[s] = 1
for s in Sorted_List_Webshell_3tuple[:int(0.3*len(Sorted_List_Webshell_3tuple))]:
	if s in Sorted_List_All_Top30_3tuple:
		continue
	else:
		Sorted_List_All_Top30_3tuple[s] = 1
for s in Sorted_List_Training_3tuple[:int(0.3*len(Sorted_List_Training_3tuple))]:
	if s in Sorted_List_All_Top30_3tuple:
		continue
	else:
		Sorted_List_All_Top30_3tuple[s] = 1


with open("Sorted_List_All_Top30_1.txt","w") as f:
	for key, value in Sorted_List_All_Top30.items():
		f.write('%s:%s\n' % (key, value))

with open("Sorted_List_All_Top30_3tuple_1.txt","w") as f:
	for key, value in Sorted_List_All_Top30_3tuple.items():
		f.write('%s:%s\n' % (key, value))

with open("Sorted_List_All_Top30_5tuple_1.txt","w") as f:
	for key, value in Sorted_List_All_Top30_5tuple.items():
		f.write('%s:%s\n' % (key, value))

for file_object in  sec_get_Attack_Data_Master_files("Adduser"):
	new_file_path = get_new_file_ob(file_object,"7")
	list_new_file ={}
	file_data = file_object.read()
	for x in list(ngrams(file_data.split(), 7)):
		if x in list_new_file:
			list_new_file[x] += 1
		else:
			list_new_file[x] = 1
	with open(new_file_path, "w") as f:
		for key,value in Sorted_List_All_Top30.items():	
			if key in list_new_file:
				f.write('%s : %d\n' % (str(key), list_new_file[key]))
			else:
				f.write('%s : 0\n' % str(key))
	new_file_path = get_new_file_ob(file_object,"5")
	list_new_file ={}
	file_data = file_object.read()
	for x in list(ngrams(file_data.split(), 5)):
		if x in list_new_file:
			list_new_file[x] += 1
		else:
			list_new_file[x] = 1
	with open(new_file_path, "w") as f:
		for key,value in Sorted_List_All_Top30_5tuple.items():	
			if key in list_new_file:
				f.write('%s : %d\n' % (str(key), list_new_file[key]))
			else:
				f.write('%s : 0\n' % str(key))
	new_file_path = get_new_file_ob(file_object,"3")
	list_new_file ={}
	file_data = file_object.read()
	for x in list(ngrams(file_data.split(), 3)):
		if x in list_new_file:
			list_new_file[x] += 1
		else:
			list_new_file[x] = 1
	with open(new_file_path, "w") as f:
		for key,value in Sorted_List_All_Top30_3tuple.items():	
			if key in list_new_file:
				f.write('%s : %d\n' % (str(key), list_new_file[key]))
			else:
				f.write('%s : 0\n' % str(key))

print(len(Sorted_List_All_Top30))
print(len(Sorted_List_All_Top30_3tuple))
print(len(Sorted_List_All_Top30_5tuple))

print("--- %s seconds ---" % (time.time() - start_time))
