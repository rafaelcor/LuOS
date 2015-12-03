#!/usr/bin/env python
#coding=utf-8
import requests
from Tkinter import *
from tkSnack import *
root = Tk()

initializeSnack(root)
import os

def convertToUrl(string):
	toReturn = "@22%s\@22" % string
	toReturn = toReturn.replace(" ", "%20").replace("@", "%")
	
	return toReturn


#http://api.naturalreaders.com/v2/tts?t=%22Me%20llamo%20Alberto%22&r=19&s=1&requesttoken=27f9f9d331fb25d120a8140eb6e52261
with open('output.mp3', 'wb') as handle:
    response = requests.get('http://api.naturalreaders.com/v2/tts?t=%22Me%20llamo%20Alberto%22&r=19&s=1&requesttoken=28f9f9d331fb25d120a8140eb6e52261', stream=True)

    if not response.ok:
        # Something went wrong
        print "error"
    
    for block in response.iter_content(1024):
		handle.write(block)
		
s = Sound()
s.read("output.mp3")
s.play()
root.mainloop()
