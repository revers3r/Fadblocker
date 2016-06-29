######################################
##            Fadblocker            ##
##                                  ##
##    @Jaehyuk Lim, @Sunghwan Jo    ##
######################################

from optparse import OptionParser
import httplib, urllib
import hashlib

if __name__ == '__main__':
	usage = """usage: fadblocker.py [-s] [-c]"""
	parser = OptionParser(usage=usage)
	parser.add_option("-l", dest="letter", action="store_true")
	parser.add_option("-c", dest="comment", action="store_true")

	(options, args) = parser.parse_args()
	