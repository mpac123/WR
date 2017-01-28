#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

try:
    Leds.set_color(Leds.LEFT,Leds.RED)
    Leds.set_color(Leds.RIGHT,Leds.RED)
    lm=LargeMotor('outD')
    rm=LargeMotor('outA')
    dzwig=MediumMotor('outB')

    #ts = TouchSensor()
    csl = ColorSensor('in3')
    csr = ColorSensor('in2')
    ins = InfraredSensor()

    vel=300
    leftvel=0
    rightvel=0
    error=0
    hist=0
    but=Button()
    Leds.set_color(Leds.LEFT,Leds.AMBER)
    Leds.set_color(Leds.RIGHT,Leds.AMBER)
    #dzwig.run_to_abs_pos(position_sp=1200)
    while not but.up:
        sleep(0.1)
    Leds.set_color(Leds.LEFT,Leds.GREEN)
    Leds.set_color(Leds.RIGHT,Leds.GREEN)
    while not but.backspace:
        if but.down:
            Leds.set_color(Leds.LEFT,Leds.AMBER)
            Leds.set_color(Leds.RIGHT,Leds.AMBER)
            lm.stop()
            rm.stop()
            while not but.up:
                sleep(0.1)
            Leds.set_color(Leds.LEFT,Leds.GREEN)
            Leds.set_color(Leds.RIGHT,Leds.GREEN)
        else:
            try:
                gr=csl.green
                bl=csl.blue
                re=csl.red
                lewy=(gr+bl+re)
                gr2=csr.green
                bl2=csr.blue
                re2=csr.red
                prawy=(gr2+bl2+re2)
                #print("lewy:",re,gr,bl,"prawy:",re2,gr2,bl2)
                #print(lewy,prawy)
                #dist=ins.value()
                
                #jazda po czarnej linii
                P=0.3 ####P jest git, dodaj calke!!!!!!!!!!!!!!!!!!!
                I=0.03
                D=0
                
                prerror=error
                error=prawy-lewy

                hist=hist*0.75+error
                

                leftvel=vel-(P*error+I*hist+D*(prerror-error))
                rightvel=vel+(P*error+I*hist+D*(prerror-error))
                if leftvel>1000:
                    leftvel=1000
                if rightvel>1000:
                    rightvel=1000
                
                lm.run_forever(speed_sp=leftvel)
                rm.run_forever(speed_sp=rightvel)
            except OSError:
                lm.stop()
                rm.stop()
                csl = ColorSensor('in3')
                csr = ColorSensor('in2')
                ins = InfraredSensor()
    
    lm.stop()
    rm.stop()
    Leds.set_color(Leds.LEFT,Leds.RED)
    Leds.set_color(Leds.RIGHT,Leds.RED)
except KeyboardInterrupt:
    lm.stop()
    rm.stop()
    Leds.set_color(Leds.LEFT,Leds.RED)
    Leds.set_color(Leds.RIGHT,Leds.RED)
        

    
    #err=vall-valr
    
    #Leds.set_color(Leds.LEFT, (Leds.GREEN, Leds.RED)[ts.value()])
    
#odczyty dla zielonego ##srednio 100
#40 130 65
#dla czerwonego 
#250 57 30 ## srednio 140
#dla czarnego
#35 50 30 ## srednio 37
#dla bialego
#300 300 350 ## srednio 310
#pomiedzy
#240 250 300 ## srednio 270
    
