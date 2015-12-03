#!/usr/bin/env python
#coding=utf-8
from os import environ, path, system
import pyaudio
import utils
import sys
import time
import difflib
import requests
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

MODELDIR = "voxforge-es-0.2/"
#MODELDIR = "esMX/"
DATADIR = "pocketsphinx/test/data"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'model_parameters/voxforge_es_sphinx.cd_ptm_3000'))
config.set_string('-lm', path.join(MODELDIR, 'etc/voxforge_es_sphinx.transcription.test.lm'))
config.set_string('-dict', path.join(MODELDIR, 'etc/voxforge_es_sphinx.dic'))

config.set_string('-inmic', "yes")
config.set_string('-logfn', '/dev/null')
decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()

p = pyaudio.PyAudio()
 
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()
in_speech_bf = True
#decoder.start_utt()

matem = {"cero":0, "uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5, "seis":6, "siete":7, "ocho":8, "nueve":9, "mas":"+"}

nombre = "Ram"

while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
        try:
            if  decoder.hyp().hypstr != '':
                print 'Partial decoding result:', decoder.hyp().hypstr
        except AttributeError:
            pass
        if decoder.get_in_speech():
            sys.stdout.write('.')
            sys.stdout.flush()
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                try:
                    if decoder.hyp().hypstr != '':
                        print 'Stream decoding result:', decoder.hyp().hypstr
                        if difflib.SequenceMatcher(None, "como es tu nombre", decoder.hyp().hypstr).quick_ratio() > 0.79:
                            system("espeak -ves 'Mi nombre es {1}'".format(nombre))
                            time.sleep(2)
                        elif difflib.SequenceMatcher(None, "como estás", decoder.hyp().hypstr).quick_ratio() > 0.79:
                            system("espeak -ves 'Estoy bien'")
                            time.sleep(2)
                        #elif difflib.SequenceMatcher(None, "cuanto es", decoder.hyp().hypstr).quick_ratio() > 0.79:
                            #if difflib.SequenceMatcher(None, "como es tu nombre", decoder.hyp().hypstr).quick_ratio() > 0.79:
                            #system("espeak -ves 'Esto no fue implementado aun'")
                            #time.sleep(2)
                            #ab = decoder.get_in_speech()
                            #print ab
                            #for num in matem:
                                
                except AttributeError:
                    pass
                decoder.start_utt()
    else:
        break
decoder.end_utt()
print 'An Error occured:', decoder.hyp().hypstr
