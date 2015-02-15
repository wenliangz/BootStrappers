#!/usr/bin/env python

import os, errno
import urllib

class Utils:
    @staticmethod
    def mkdir_p(path):
     # from http://stackoverflow.com/a/600612
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: 
                raise

    @staticmethod
    def chrNumAsString(num):
        return "chr" + str(num)

    @staticmethod
    def get_file_if_size_diff(url, path):
        fn = url.split('/')[-1]
        out_fnp = os.path.join(path, fn)
        net_file_size = int(urllib.urlopen(url).info()['Content-Length'])
        if os.path.exists(out_fnp):
            fn_size = os.path.getsize(out_fnp)
            if fn_size == net_file_size:
                print "skipping download of", fn
                return out_fnp
            else: 
                print "files sizes differed:"
                print "\t", "on disk:", fn_size
                print "\t", "from net:", net_file_size
        print "retrieving", fn
        urllib.urlretrieve(url, out_fnp)
        return out_fnp

class Paths():
    def __init__(self, lectureNumber):
        self.homeFolder = os.path.abspath(os.path.expanduser("~"))
        self.desktopFolder = os.path.join(self.homeFolder, "Desktop")
        self.python2folder = os.path.join(self.desktopFolder, "python_2")
        lecture = "lecture_" + str(lectureNumber)
        self.lectureFolder = os.path.join(self.python2folder, lecture)
        print "today's lecture folder location will be:", self.lectureFolder
        Utils.mkdir_p(self.lectureFolder)

    def makeFilePath(self, fn):
        return os.path.join(self.lectureFolder, fn)

class HG19chrSize():
	def __init__(self,paths):
		self.paths=paths
		self.url="http://bioinfo.umassmed.edu/bootstrappers/bootstrappers-courses/python2/lecture1/hg19.chrom.sizes"
		fnp=Utils.get_file_if_size_diff(self.url,paths.lectureFolder)
		self.chrTolen={}
	 	with open(fnp) as f:
			for line in f:
				line_split=line.split()
				chrom=line_split[0]
				lenth=line_split[1]
				self.chrTolen[chrom]=lenth

	def chr_length(self,chr_num):
		return self.chrTolen["chr"+str(chr_num)]

paths=Paths(3)
print HG19chrSize(paths).chr_length(7)