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
                
    #jazda po czarnej linii
    P=0.2 
    I=0.03
    D=0

    vel=50
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
                
                #print(gr,bl,re)
                
                
                #zakret 90 st w prawo
                if prawy<134 and lewy>174:
                    #czp=1
                    czl=0
                    Leds.set_color(Leds.LEFT,Leds.GREEN)
                    Leds.set_color(Leds.RIGHT,Leds.YELLOW)
                    
                #zakret 90 st w lewo
                if lewy<174 and prawy>134:
                    #czl=1
                    czp=0
                    Leds.set_color(Leds.LEFT,Leds.YELLOW)
                    Leds.set_color(Leds.RIGHT,Leds.GREEN)
                    

                        
                #znalazl zielony lewym czujnikiem        
                if (lgr>140  and lre<73 and lgr-lre>90 and czy_ziel==0):
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
                    while not (lgr>140  and lre<73 and lgr-lre>90):
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
                elif (rgr>105 and rre<62 and rgr-rre>60 and czy_ziel==0):
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
                    while not (rgr>105 and rre<62 and rgr-rre>60 ):
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
                elif czy_ziel==1 and (lgr>140 and lbl<124 and lre<73 and rgr>105 and rbl<120 and rre<62):
                        lm.run_forever(speed_sp=vel/4)
                        rm.run_forever(speed_sp=vel/4)
                        czy_ziel=2
                        while ins.value()>0:
                            sleep(0.1)
                        lm.run_forever(speed_sp=0)
                        rm.run_forever(speed_sp=0)
                        dzwig.run_to_abs_pos(position_sp=2000,speed_sp=500)
                        dzwig.wait_while('running')    
                        while (lgr>140 and lbl<124 and lre<73 and rgr>105 and rbl<120 and rre<62):
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
                elif czy_ziel==2 and prawy<171 and lewy<203:
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
                elif (lgr<100 and lbl<100 and lre>200 and czy_czerw==0 and czy_ziel==3):
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
                    while not (lgr<100 and lbl<100 and lre>200):
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
                elif (rgr<100 and rbl<100 and rre>200 and czy_ziel==0 and czy_czerw==3):
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
                    while not (rgr<100 and rbl<100 and rre>200):
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
                
                
                #znajdowanie czerwongo obydwoma czujnikami
                elif czy_czerw==1 and rgr<100 and rbl<100 and rre>200 and lgr<100 and lbl<100 and lre>200:
                        lm.run_forever(speed_sp=vel/4)
                        rm.run_forever(speed_sp=vel/4)
                        czy_czerw=2
                        lm.run_forever(speed_sp=0)
                        rm.run_forever(speed_sp=0)
                        dzwig.run_to_abs_pos(position_sp=0,speed_sp=500)
                        dzwig.wait_while('running')  
                        lm.run_to_rel_pos(position_sp=-150,speed_sp=vel)
                        rm.run_to_rel_pos(position_sp=-150,speed_sp=vel) 
                        lm.wait_while('running')
                        Sound.speak('I am done').wait()
                        break        
                
                
                
               
                
                elif czp==1 and prawy>815 and lewy>955:
                    
                    while lewy>955:
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
                    czp=0; czl=0
                    Leds.set_color(Leds.LEFT,Leds.GREEN)
                    Leds.set_color(Leds.RIGHT,Leds.GREEN)
                    
                
                elif czl==1 and prawy>815 and lewy>955:
                    
                    while prawy>815:
                            try:
                                lm.run_forever(speed_sp=-vel/4)
                                rm.run_forever(speed_sp=vel/4)
                                rgr=csr.green
                                rbl=csr.blue
                                rre=csr.red
                                prawy=rgr+rbl+rre
                            except OSError:
                                lm.stop()
                                rm.stop()
                                csl = ColorSensor('in3')
                                csr = ColorSensor('in2')
                                ins = InfraredSensor()
                    czp=0; czl=0
                    Leds.set_color(Leds.LEFT,Leds.GREEN)
                    Leds.set_color(Leds.RIGHT,Leds.GREEN)
                    
                    
                else:
                
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
        

    
#CZARNY: lewy: 21 34 22 prawy: 23 45 28
#BIALY BRUDNY: lewy: 159 251 154 prawy: 194 261 282
#CZERWONY: lewy: 166 39 24 prawy: 205 49 28
#ZIELONY: lewy: 22 115 40 prawy: 27 129 64


