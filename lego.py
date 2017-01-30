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
    
    czl=0;
    czp=0;

    vel=200
    error=0
    hist=0
    war=0
    czy_ziel=0
    czy_czerw=0
    but=Button()
    Leds.set_color(Leds.LEFT,Leds.AMBER)
    Leds.set_color(Leds.RIGHT,Leds.AMBER)
    dzwig.run_to_abs_pos(position_sp=0,speed_sp=500)
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
                sleep(0.01)
                lgr=csl.green
                lbl=csl.blue
                lre=csl.red
                lewy=(lgr+lbl+lre)
                rgr=csr.green
                rbl=csr.blue
                rre=csr.red
                prawy=(rgr+rbl+rre)
                
                #print("lewy:",re,gr,bl,"prawy:",re2,gr2,bl2)
                #print(lewy,prawy)
                #dist=ins.value()
                
                #jazda po czarnej linii
                P=0.3 ####P jest git, dodaj calke!!!!!!!!!!!!!!!!!!!
                I=0.03
                D=0
                
                
                prerror=error
                error=prawy-lewy
                
                #print(gr,bl,re)
                #znalazl zielony lewym czujnikiem
                if (lgr>110 and lbl<60 and lre<40 and czy_ziel==0):
                    czy_ziel=1
                    lm.run_to_rel_pos(position_sp=70,speed_sp=vel) #bylo 100
                    rm.run_to_rel_pos(position_sp=70,speed_sp=vel) #bylo 100
                    lm.wait_while('running')
                    Leds.set_color(Leds.LEFT,Leds.ORANGE)
                    Leds.set_color(Leds.RIGHT,Leds.ORANGE)
                    lgr=csl.green
                    lbl=csl.blue
                    lre=csl.red
                    lewy=(lgr+lbl+lre)
                    rgr=csr.green
                    rbl=csr.blue
                    rre=csr.red
                    prawy=(rgr+rbl+rre)
                    while not (lgr>110 and lbl<60 and lre<40):
                        try:
                            lm.run_forever(speed_sp=-vel/4)
                            rm.run_forever(speed_sp=vel/4)
                            lgr=csl.green
                            lbl=csl.blue
                            lre=csl.red
                        except OSError:
                            lm.stop()
                            rm.stop()
                            csl = ColorSensor('in3')
                            csr = ColorSensor('in2')
                            ins = InfraredSensor()
                    lm.run_to_rel_pos(position_sp=-50,speed_sp=vel)
                    rm.run_to_rel_pos(position_sp=50,speed_sp=vel)
                    lm.wait_while('running')    
                    Leds.set_color(Leds.LEFT,Leds.GREEN)
                    Leds.set_color(Leds.RIGHT,Leds.GREEN)
                
                #znalazl zielony prawym czujnikiem
                if (rgr>120 and rbl<80 and rre<50 and czy_ziel==0):
                    czy_ziel=1
                    lm.run_to_rel_pos(position_sp=70,speed_sp=vel) #bylo 100
                    rm.run_to_rel_pos(position_sp=70,speed_sp=vel) #bylo 100
                    lm.wait_while('running')
                    Leds.set_color(Leds.LEFT,Leds.ORANGE)
                    Leds.set_color(Leds.RIGHT,Leds.ORANGE)
                    lgr=csl.green
                    lbl=csl.blue
                    lre=csl.red
                    lewy=(lgr+lbl+lre)
                    rgr=csr.green
                    rbl=csr.blue
                    rre=csr.red
                    prawy=(rgr+rbl+rre)
                    while not (rgr>120 and rbl<80 and rre<50):
                        try:
                            lm.run_forever(speed_sp=vel/4)
                            rm.run_forever(speed_sp=-vel/4)
                            rgr=csr.green
                            rbl=csr.blue
                            rre=csr.red
                        except OSError:
                            lm.stop()
                            rm.stop()
                            csl = ColorSensor('in3')
                            csr = ColorSensor('in2')
                            ins = InfraredSensor()
                    lm.run_to_rel_pos(position_sp=50,speed_sp=vel)
                    rm.run_to_rel_pos(position_sp=-50,speed_sp=vel)
                    lm.wait_while('running')    
                    Leds.set_color(Leds.LEFT,Leds.GREEN)
                    Leds.set_color(Leds.RIGHT,Leds.GREEN)
                    
                #znajduje zielony obydwoma czujnikami            
                if czy_ziel==1:
                    if (lgr>110 and lbl<60 and lre<40 and rgr>120 and rbl<80 and rre<50):
                        lm.run_forever(speed_sp=vel/4)
                        rm.run_forever(speed_sp=vel/4)
                        czy_ziel=2
                        while ins.value()>0:
                            sleep(0.1)
                        lm.run_forever(speed_sp=0)
                        rm.run_forever(speed_sp=0)
                        dzwig.run_to_abs_pos(position_sp=2000,speed_sp=500)
                        dzwig.wait_while('running')    
                        while (lgr>110 and lbl<60 and lre<40 and rgr>120 and rbl<80 and rre<50):
                            try:
                                lm.run_forever(speed_sp=-vel/4)
                                rm.run_forever(speed_sp=-vel/4)
                                rgr=csr.green
                                rbl=csr.blue
                                rre=csr.red
                                lgr=csl.green
                                lbl=csl.blue
                                lre=csl.red
                            except OSError:
                                lm.stop()
                                rm.stop()
                                csl = ColorSensor('in3')
                                csr = ColorSensor('in2')
                                ins = InfraredSensor()
                        lm.run_to_rel_pos(position_sp=150,speed_sp=vel)
                        rm.run_to_rel_pos(position_sp=-150,speed_sp=vel)
                        lm.wait_while('running')    
                        lgr=csl.green
                        lbl=csl.blue
                        lre=csl.red
                        lewy=lgr+lbl+lre
                        while lewy>200:
                            try:
                                lm.run_forever(speed_sp=vel/4)
                                rm.run_forever(speed_sp=-vel/4)
                                lgr=csl.green
                                lbl=csl.blue
                                lre=csl.red
                                lewy=lgr+lbl+lre
                            except OSError:
                                lm.stop()
                                rm.stop()
                                csl = ColorSensor('in3')
                                csr = ColorSensor('in2')
                                ins = InfraredSensor()
                
                #wracam z zielonego pola                
                if czy_ziel==2:
                    if prawy<140 and lewy<120:
                        czy_ziel=3
                        lm.run_to_rel_pos(position_sp=70,speed_sp=vel/2)
                        rm.run_to_rel_pos(position_sp=70,speed_sp=vel/2)
                        lm.wait_while('running')  
                        lgr=csl.green
                        lbl=csl.blue
                        lre=csl.red
                        lewy=lgr+lbl+lre  
                        while lewy>200:
                            try:
                                lm.run_forever(speed_sp=vel/4)
                                rm.run_forever(speed_sp=-vel/4)
                                lgr=csl.green
                                lbl=csl.blue
                                lre=csl.red
                                lewy=lgr+lbl+lre
                            except OSError:
                                lm.stop()
                                rm.stop()
                                csl = ColorSensor('in3')
                                csr = ColorSensor('in2')
                                ins = InfraredSensor()
                    
                #znalazl czerwony lewym czujnikiem
                if (lgr<60 and lbl<50 and lre>150 and czy_czerw==0):
                    czy_czerw=1
                    lm.run_to_rel_pos(position_sp=70,speed_sp=vel) #bylo 100
                    rm.run_to_rel_pos(position_sp=70,speed_sp=vel) #bylo 100
                    lm.wait_while('running')
                    Leds.set_color(Leds.LEFT,Leds.ORANGE)
                    Leds.set_color(Leds.RIGHT,Leds.ORANGE)
                    lgr=csl.green
                    lbl=csl.blue
                    lre=csl.red
                    lewy=(lgr+lbl+lre)
                    rgr=csr.green
                    rbl=csr.blue
                    rre=csr.red
                    prawy=(rgr+rbl+rre)
                    while not (lgr<60 and lbl<50 and lre>150):
                        try:
                            lm.run_forever(speed_sp=-vel/4)
                            rm.run_forever(speed_sp=vel/4)
                            lgr=csl.green
                            lbl=csl.blue
                            lre=csl.red
                        except OSError:
                            lm.stop()
                            rm.stop()
                            csl = ColorSensor('in3')
                            csr = ColorSensor('in2')
                            ins = InfraredSensor()
                    lm.run_to_rel_pos(position_sp=-50,speed_sp=vel)
                    rm.run_to_rel_pos(position_sp=50,speed_sp=vel)
                    lm.wait_while('running')    
                    Leds.set_color(Leds.LEFT,Leds.GREEN)
                    Leds.set_color(Leds.RIGHT,Leds.GREEN)
                
                #znalazl czerwony prawym czujnikiem
                if (rgr<70 and rbl<50 and rre>180 and czy_ziel==0):
                    czy_ziel=1
                    lm.run_to_rel_pos(position_sp=70,speed_sp=vel) #bylo 100
                    rm.run_to_rel_pos(position_sp=70,speed_sp=vel) #bylo 100
                    lm.wait_while('running')
                    Leds.set_color(Leds.LEFT,Leds.ORANGE)
                    Leds.set_color(Leds.RIGHT,Leds.ORANGE)
                    lgr=csl.green
                    lbl=csl.blue
                    lre=csl.red
                    lewy=(lgr+lbl+lre)
                    rgr=csr.green
                    rbl=csr.blue
                    rre=csr.red
                    prawy=(rgr+rbl+rre)
                    while not (rgr<70 and rbl<50 and rre>180):
                        try:
                            lm.run_forever(speed_sp=vel/4)
                            rm.run_forever(speed_sp=-vel/4)
                            rgr=csr.green
                            rbl=csr.blue
                            rre=csr.red
                        except OSError:
                            lm.stop()
                            rm.stop()
                            csl = ColorSensor('in3')
                            csr = ColorSensor('in2')
                            ins = InfraredSensor()
                    lm.run_to_rel_pos(position_sp=50,speed_sp=vel)
                    rm.run_to_rel_pos(position_sp=-50,speed_sp=vel)
                    lm.wait_while('running')    
                    Leds.set_color(Leds.LEFT,Leds.GREEN)
                    Leds.set_color(Leds.RIGHT,Leds.GREEN)
                if prawy<110:
                    czp=1
                    Leds.set_color(Leds.RIGHT,Leds.YELLOW)
                if lewy<95:
                    czl=1
                    Leds.set_color(Leds.LEFT,Leds.YELLOW)
                
                #znajdowanie czerwongo obydwoma czujnikami
                if czy_czerw==1:
                    if rgr<70 and rbl<50 and rre>180 and lgr<60 and lbl<50 and lre>150:
                        lm.run_forever(speed_sp=0)
                        rm.run_forever(speed_sp=0)
                        czy_czerw=0
                        sleep(1)
                
                if czp==1 and czl==1:
                    czp=0; czl=0
                    Leds.set_color(Leds.LEFT,Leds.GREEN)
                    Leds.set_color(Leds.RIGHT,Leds.GREEN)
                
                czp=0; czl=0
                
                if czp==1 and prawy>600 and lewy>550:
                    
                    
                    rm.run_forever(speed_sp=-vel/2)
                    lm.run_forever(speed_sp=vel/2)
                    Leds.set_color(Leds.RIGHT,Leds.RED)
                    while (lewy>450 and war!=2):
                        gr=csl.green
                        bl=csl.blue
                        re=csl.red
                        lewy=(gr+bl+re)
                        gr2=csr.green
                        bl2=csr.blue
                        re2=csr.red
                        prawy=(gr2+bl2+re2)
                        if war==0:
                            if prawy<110:
                                war=1
                        if war==1:
                            if prawy>250:
                                war=2
                        
                    Leds.set_color(Leds.LEFT,Leds.GREEN)
                    Leds.set_color(Leds.RIGHT,Leds.GREEN)
                    war=0
                    
                    hist=0
                    gr=csl.green
                    bl=csl.blue
                    re=csl.red
                    lewy=(gr+bl+re)
                    gr2=csr.green
                    bl2=csr.blue
                    re2=csr.red
                    prawy=(gr2+bl2+re2)
                    error=prawy-lewy
                    prerror=0
                    czp=0
                    
                if czl==1 and lewy>550 and prawy>600:
                    
                    lm.run_forever(speed_sp=-vel/2)
                    rm.run_forever(speed_sp=vel/2)
                    Leds.set_color(Leds.LEFT,Leds.RED)
                    while (prawy>500 and war!=2):
                        gr=csl.green
                        bl=csl.blue
                        re=csl.red
                        lewy=(gr+bl+re)
                        gr2=csr.green
                        bl2=csr.blue
                        re2=csr.red
                        prawy=(gr2+bl2+re2)
                        if war==0:
                            if lewy<90:
                                war=1
                        if war==1:
                            if lewy>200:
                                war=2
                        
                    Leds.set_color(Leds.LEFT,Leds.GREEN)
                    Leds.set_color(Leds.RIGHT,Leds.GREEN)
                    war=0
                    
                    hist=0
                    gr=csl.green
                    bl=csl.blue
                    re=csl.red
                    lewy=(gr+bl+re)
                    gr2=csr.green
                    bl2=csr.blue
                    re2=csr.red
                    prawy=(gr2+bl2+re2)
                    error=prawy-lewy
                    prerror=0
                    czl=0
                    
                
                        
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
        

    
#CZARNY: lewy: 21 34 22 prawy: 23 45 28
#BIALY BRUDNY: lewy: 159 251 154 prawy: 194 261 282
#CZERWONY: lewy: 166 39 24 prawy: 205 49 28
#ZIELONY: lewy: 22 115 40 prawy: 27 129 64


