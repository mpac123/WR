#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

lm=LargeMotor('outD')
rm=LargeMotor('outA')
dzwig=MediumMotor('outB')
leds=Leds()

#ts = TouchSensor()
csl = ColorSensor('in3')
csr = ColorSensor('in2')
ins = InfraredSensor()

but=Button()
pos=0
Leds.set_color(Leds.LEFT,Leds.AMBER)
while 1:
	lgr=csl.green
	lbl=csl.blue
	lre=csl.red
	lewy=(lgr+lbl+lre)
	rgr=csr.green
	rbl=csr.blue
	rre=csr.red
	prawy=(rgr+rbl+rre)
	print("lewy:",lre,lgr,lbl,"prawy:",rre,rgr,rbl)
	if but.enter:
		dzwig.run_to_abs_pos(position_sp=pos,speed_sp=100)
		pos=pos+100
		print(pos)
