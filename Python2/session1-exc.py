# v=[1,2,3,4,5,8,13,21]
# print v.count(1)
# print v[0]
# print v[-1]
# print v[-2]
# print v[::-1]
# print v.index(21)

# v = [1, 1, 2, 3, 5, 8, 13, 21]
# v = v[3:5]
# print v
# v[0] = 100
# print v
# v[1] = [1,1,2]
# print v

# s = "Hello World!"
# print s
# s = "Hello World!\n"
# print s
# print s[0:5]
# s[0:5] = "HELLO!"
# print s

# s = "Hello World!\n"
# s = "HELLO!" + s[5:-1]
# print s

# s = "Hello World!"
# print s.startswith("He")
# print s.split()
# print s.split("o")
# print s.split(" ")

# s = "2015"
# print s == 2015
# print int(s) == 2015
# print s == str(2015)

# import os
# homeFolder = os.path.expanduser("~")
# print homeFolder
# homeFolder = os.path.abspath(homeFolder)
# python2folder = os.path.join(homeFolder, "python_2")
# print homeFolder
# print python2folder

import os, errno
def mkdir_p(path):
# from http://stackoverflow.com/a/600612
	try:
		os.makedirs(path)
	except OSError as exc: # Python >2.5
		if exc.errno == errno.EEXIST and os.path.isdir(path):
			pass
		else: raise
homeFolder = os.path.abspath(os.path.expanduser("~"))
desktopFolder = os.path.join(homeFolder, "Desktop")
python2folder = os.path.join(desktopFolder, "python_2")
lecture1folder = os.path.join(python2folder, "lecture_1")
print "today's lecture folder location will be:", lecture1folder
mkdir_p(lecture1folder)

url = "http://bib3.umassmed.edu/~purcarom/Python2/Lecture1/ENCFF002COQ.narrowPeak"
fileName = os.path.basename(url)
fnp = os.path.join(lecture1folder, fileName)
print "going to download", fileName, "from", url
import urllib
urllib.URLopener().retrieve(url, fnp)

with open(fnp) as f: # the same as f=open(fnp), but this knows how to close file
	n=0
	i=0
	for line in f:
		i+=1
		if line.startswith("chr7"):
			n+=1
			print line
print n
print str(n*100/i) + "%"  # if you write" print str(n*100/i), "%" in which "," equals space in python
