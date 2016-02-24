import re
import string


__author__ = 'Newton McCollum & Ike Clinton'


#Opening the file for which expressions will be compared against
textFile = open("TextFile.txt")
Text = textFile.read();

#Opening the file which contains other RegEx expressions
regexFile = open("RegExFile.txt").read()

regexArr = regexFile.split("\n")



regexIPv4 = "(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
regexUrl = "[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}"
regexUrlDir = "[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}([-a-zA-Z0-9@:%_\+.~#?&//=]*)"





#Finds all the prevelant IPv4 Addresses and prints thme out
print("\n---------------Printing all IPv4 Addresses---------------")
print(re.findall(regexIPv4, Text))



#finds all the addresses and there extensions and adds them together then prints them out
address = re.findall(regexUrl, Text)
extension = re.findall(regexUrlDir, Text)
print("\n---------------Printing all urls Found---------------")
for i in range(0, len(address)):
       print("%s%s:"%( address[i],extension[i]))



#Prints out all lines for which password is present in
print("\n---------------Printing all lines in which password is found---------------")
TextSplit = Text.split('\n');
for i in range(0, len(TextSplit)):
       if "password" in (TextSplit[i]):
              print(TextSplit[i])


