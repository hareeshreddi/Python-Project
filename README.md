# Python-Project
Part of CS241 and CS244 Courses in my Engineering 2nd Year at IIT Guwahati.
Description of Australian Defence Force Academy-Linux Dataset (ADFA-LD) :
1) The dataset was generated on Linux local server running on Ubuntu 11.04, offering a variety
of functions such as file sharing, database, remote access and web server.
2) Six types of attacks occur in ADFA-LD including two brute force password guessing
attempts on the open ports enabled by FTP and SSH respectively, an unauthorised attempt to
create a new user with root privileges through encoding a malicious payload into a normal
executable, the uploads of Java and Linux executable Meterpreter payloads for the remote
compromise of a target host, and the compromise and privilege escalation using C100
webshell. These types are termed as Hydra-FTP, Hydra-SSH, Adduser, Java-Meterpreter,
Meterpreter and Webshell respectively. You can find these attacks inside the folder
“Attack_Data_Master”
3) 833 and 4373 normal traces are generated for training and validation respectively, over a
period during which no attacks occur against the host and legitimate application activities
ranging from web browsing to document writing are operated as usual. These training and
validation can be found in the “Training_Data_Master” and “Validation_Data_Master”
folders, respectively.

Assignment Task(Simplified):
1) Split the Attack data of each category (Hydra-FTP, Hydra-SSH, Adduser, Java-Meterpreter,
Meterpreter and Webshell ) into 70% training data and 30 % test data. For instance there are
are 10 folders in “Adduser” attack. Therefore, 7 of these folders are to be used for training
and 3 folders are to be used for testing.
2) For the Normal data, files in “Training_Data_Master” folder are to be used as training data
and files in “Validation_Data_Master” folder are to be used as test data.
3) Write a python script to find the frequency of occurences of all unique 3-grams, 5-grams
and 7-grams system call sequences in the training data for both Attack data (across all
categories of attack) and Normal data. 
4) Perform the same task on files in the “Training_Data_Master” to obtain all the unique 3-
grams, 5-grams and 7-grams.
5) Once you have obtained the frequencies of all the unique n-grams terms in the training data,
use the top 30% n-grams terms with the highest frequency to create a data set
6) Apply the same procedure to generate the test dataset from the test files of the attack data
(for all attack types) and the normal files in the “Validation_Data_Master” using the top
30% 3-grams terms with highest frequencies obtained during the training phase. The
classifier model developed during the training phase will finally be validated on the Test
dataset.
