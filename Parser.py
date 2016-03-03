# To add files to be tracked/removed:
# git add -A

# To commit changes and stage them to be pushed
# git commit -am "my commit message"

# To push changes to github
# git push origin master

# To create a new branch
# git checkout -b my_new_branch

# To merge branch back in when done (after you have committed and pushed
# change from branch):
# git checkout master
# git puhs

# Test Branch
import re
import string
import sys
import getopt
import os, os.path
from glob import glob


__author__ = 'Newton McCollum & Ike Clinton'

#Parses the command line inputs
#Optoons are -k (Keywordfile) -t (Textfile) -d (Directory) or -r (regexfile)
#Default balues: Parser.py -t TextFile.txt -k Keyword.txt -r RegExFile.txt -d null
def main(argv):
   keyfile = 'Keyword.txt'
   textfile = ['TextFile.txt']
   refile = 'RegExFile.txt'
   try:
      opts, args = getopt.getopt(argv,"hk:t:r:d:",["kfile=", "tfile=", "rfile=", "dfile="])
   except getopt.GetoptError:
      print('Parser.py -t <inputfile> -k <keywordfile> -r <regexfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('Default: Parser.py -t TextFile.txt -k Keyword.txt -r RegExFile.txt')
         print('Parser.py\n'
               '-t <inputfile>\n'
               '-k <keywordfile>\n'
               '-r <regexfile>\n'
               '-d <search dir>\n')
         sys.exit()
      elif opt in ("-k", "--kfile"):
         print(arg)
         keyfile = arg
      elif opt in ("-t", "--tfile"):
         print(arg)
         textfile = [arg]
      elif opt in ("-r", "--rfile"):
          print(arg)
          refile = arg
      #Work In Progress Searching through directory
      elif opt in("-d", "--dfile"):
          textfile = []
          #print(arg)
          for name in os.listdir(arg):
              if os.path.isfile(os.path.join(arg,name)):
                  textfile.append(name)

   print("TEXTFILE: ", textfile)
   print("KEYFILE: ", keyfile)
   print("REGEXFILE: ", refile)

   return [textfile, keyfile, refile]


#Searches through a given file parsing out information
#Such as regular expressions information, and keywords
def searchFile(files , keyfileArr, refile):


    #regexIPv4 = "(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
    regexUrl = "[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}"
    regexUrlDir = "[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}([-a-zA-Z0-9@:%_\+.~#?&//=]*)"

    # finds all the addresses and there extensions and adds them together then prints them out
    address = re.findall(regexUrl, text)
    extension = re.findall(regexUrlDir, text)
    print("\n---------------Printing all urls Found---------------")
    for i in range(0, len(address)):
        print("%s%s:" % (address[i], extension[i]))

    # Prints out all lines for which password is present in
    # Here we want to check multiple words and maybe even a text file of key
    # words in the text file (pass, pw, secret, PASSWORD, etc)
    # make not lowercase, etc

    # Change this to look for a list of keywords?
    # We also want to find things like "rsa-dss" and "key" and "aws.credential"
    # Make a regex that finds all instances of "credential", "key", etc
    print("\n---------------Printing all lines in which keywords that are found---------------")
    textArr = text.split('\n')
    for keyword in keyWordArr:
        print("Keyword:", keyword)
        for i in range(0, len(textArr)):
            if keyword in (textArr[i]):
                if (textArr[i] != ''):
                    print("     ",textArr[i])


    # Looping through the text file and using each regex found in the regExFile
    print("\n---------------Printing all text found using RegEx---------------")
    for regEx in regexArr:
        regexLineArr = regEx.split(" : ")
        print("Using regex to retrieve",regexLineArr[0] )
        print("     RESULT",re.findall(regexLineArr[1], text),"\n")



#Command line functionality
fileArr = main(sys.argv[1:])

# Opening the file which contains the keywords which will be searched
keyWordArr = open(fileArr[1]).read().split('\n')

# Opening the file which contains other RegEx expressions
regexArr = open(fileArr[2]).read().split("\n")

#Searches through all files present in Dir
#Or the passed textfile from command line
for files in fileArr[0]:
    text = open(files).read()
    print(searchFile(text, keyWordArr,regexArr))











