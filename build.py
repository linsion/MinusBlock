#!/usr/bin/env python
from os import listdir
import string
import random
import os
makeFileString=""
def subModuleList():
	returnString="_FILES = Tweak.xm"
	FileList=listdir("./Hooks/SDKSpecific/")
	for x in FileList:
		if(x.endswith(".mm")==False and x.endswith(".m")==False and x.endswith(".xm")==False):
			print x+" "+"Not A Code File"
		else:	
			string=" "+"Hooks/SDKSpecific/"+x
			returnString+=string
	List2=listdir("./Hooks/APIHooks/")
	for x in List2:
		if(x.endswith(".mm")==False and x.endswith(".m")==False and x.endswith(".xm")==False):
			print x+" "+"Not A Code File"
		else:
			string=" "+"Hooks/APIHooks/"+x
			returnString+=string
	FileList3=listdir("./Hooks/")
	for x in FileList3:
		if(x.endswith(".mm")==False and x.endswith(".m")==False and x.endswith(".xm")==False):
			print x+" "+"Not A Code File"
		else:	
			string=" "+"Hooks/"+x
			returnString+=string
	return returnString
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	#Thanks to http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
	return ''.join(random.choice(chars) for _ in range(size))
randomTweakName=id_generator(size=10)#Generate Random Name To Help Bypass Detection
os.remove("./Makefile")
makeFileString+="include theos/makefiles/common.mk\n"
makeFileString+="export ARCHS = armv7 armv7s arm64\n"
makeFileString+="export TARGET = iphone:clang:7.0:7.0\n"
makeFileString+="TWEAK_NAME = "+randomTweakName+"\n"
makeFileString+=randomTweakName+subModuleList()+"\n"
makeFileString+="ADDITIONAL_CCFLAGS  = -Qunused-arguments\n"
makeFileString+="ADDITIONAL_LDFLAGS  = -Wl,-segalign,4000\n"
makeFileString+="include $(THEOS_MAKE_PATH)/tweak.mk\n"
makeFileString+="after-install::\n"
makeFileString+="	install.exec \"killall -9 SpringBoard\""
#print makeFileString
fileHandle = open('Makefile','w')
fileHandle.write(makeFileString)
fileHandle.close() 
os.system("make package")


