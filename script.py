#!/usr/bin/python
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

bleu=17
vert=27
rouge=22
bouton=4

GPIO.setwarnings(False)
GPIO.setup(bouton, GPIO.IN)
GPIO.setup(bleu, GPIO.OUT)
GPIO.setup(vert, GPIO.OUT)
GPIO.setup(rouge, GPIO.OUT)

compteur=0

while True:

	print(compteur)

	if(GPIO.input(bouton) == False):
          if(compteur<3):
                  compteur+=1
                  time.sleep(0.5)
	  else: 
                  compteur= 0
	          time.sleep(0.5)

	if(compteur==0):
		GPIO.output(bleu, False);
		GPIO.output(vert, False);
		GPIO.output(rouge, False);


        if(compteur==1):

		GPIO.output(bleu, True);
		GPIO.output(vert, False);
		GPIO.output(rouge, False);

	if(compteur==2):

		GPIO.output(bleu, False);
		GPIO.output(vert, True);
		GPIO.output(rouge, False);


	if(compteur==3):

		GPIO.output(bleu, False);
		GPIO.output(vert, False);
		GPIO.output(rouge, True);




		
































