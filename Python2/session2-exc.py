# import os, errno
# def mkdir_p(path):
# # from http://stackoverflow.com/a/600612
# 	try:
# 		os.makedirs(path)
# 	except OSError as exc: # Python >2.5
# 		if exc.errno == errno.EEXIST and os.path.isdir(path):
# 			pass
# 		else: raise
# homeFolder = os.path.abspath(os.path.expanduser("~"))
# desktopFolder = os.path.join(homeFolder, "Desktop")
# python2folder = os.path.join(desktopFolder, "python_2")
# lecture1folder = os.path.join(python2folder, "lecture_1")
# print "today's lecture folder location will be:", lecture1folder
# mkdir_p(lecture1folder)

# url = "http://bib3.umassmed.edu/~purcarom/Python2/Lecture1/ENCFF002COQ.narrowPeak"
# fileName = os.path.basename(url)
# fnp = os.path.join(lecture1folder, fileName)
# print "going to download", fileName, "from", url
# import urllib
# urllib.URLopener().retrieve(url, fnp)

# def ChrPeakPtg(num):
# 	with open(fnp) as f: # the same as f=open(fnp), but this knows how to close file
# 		n=0
# 		i=0
# 		for line in f:
# 			i+=1
# 			if line.startswith("chr"+str(num)):
# 				n+=1
# 	return (n, str(n*100/i) + "%")  # return multiple values

# print ChrPeakPtg(7)


# dailyCalendar = { "9AM" : "PI Meeting",
# "11AM" : "conference ",
# "4PM" : "book club"
# }
# print dailyCalendar["4PM"]
# dailyCalendar["4PM"] = "PI meeting"
# print dailyCalendar["4PM"]
# #print dailyCalendar["3PM"]
# if "3PM" in dailyCalendar:
# 	print dailyCalendar["3PM"]

# for time, obligation in dailyCalendar.iteritems():
# 	print 'at', time, ":\t", obligation

# nums = set()
# nums.add(1)
# nums.add(1)
# nums.add(2)
# nums.add(3)
# nums.add(5)
# nums.add(8)
# nums.add(8)
# print nums
# print 10 in nums

from collections import defaultdict

dailyCalendar = defaultdict(str)
dailyCalendar["9AM"] = "PI Meeting"
dailyCalendar["11AM"] = "conference call"
dailyCalendar["4PM"] = "book club"
print dailyCalendar["4PM"]
print dailyCalendar["3PM"]