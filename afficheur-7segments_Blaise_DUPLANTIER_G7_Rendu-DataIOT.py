from machine import Pin, PWM
import time 

# initialisation des broches de la Raspberry Pi pour chaque segment de l'afficheur
a = PWM(Pin(17, mode=Pin.OUT))
a.duty_u16(0)

b = PWM(Pin(16, mode=Pin.OUT))
b.duty_u16(0)

c = PWM(Pin(14, mode=Pin.OUT))
c.duty_u16(0)

d = PWM(Pin(13, mode=Pin.OUT))
d.duty_u16(0)

e = PWM(Pin(12, mode=Pin.OUT))
e.duty_u16(0)

f = PWM(Pin(18, mode=Pin.OUT))
f.duty_u16(0)

g = PWM(Pin(19, mode=Pin.OUT))
g.duty_u16(0)


while True:

    
    # Numéro 1
    b.duty_u16(5000)
    c.duty_u16(10000) # J'ai augmenté la valeur des variables c et f car ces segments avait du mal à s'éclairer
    time.sleep(1)
    
    # Numéro 2
    c.duty_u16(0)
    a.duty_u16(5000)
    d.duty_u16(5000)
    e.duty_u16(5000)
    g.duty_u16(5000)
    time.sleep(1)
    
    # Numéro 3
    e.duty_u16(0)
    c.duty_u16(10000)
    time.sleep(1)
    
    # Numéro 4
    a.duty_u16(0)
    d.duty_u16(0)
    f.duty_u16(40000)
    time.sleep(1)
    
    # Numéro 5
    b.duty_u16(0)
    a.duty_u16(5000)
    d.duty_u16(5000)
    time.sleep(1)
    
    # Numéro 6
    e.duty_u16(5000)
    time.sleep(1)
    
    # Numéro 7
    d.duty_u16(0)
    e.duty_u16(0)
    f.duty_u16(0)
    g.duty_u16(0)
    b.duty_u16(5000)
    time.sleep(1)
    
    # Numéro 8
    d.duty_u16(5000)
    e.duty_u16(5000)
    f.duty_u16(40000)
    g.duty_u16(5000)
    time.sleep(1)
    
    # Numéro 9
    e.duty_u16(0)
    time.sleep(1)
    a.duty_u16(0)
    b.duty_u16(0)
    c.duty_u16(0)
    d.duty_u16(0)
    e.duty_u16(0)
    f.duty_u16(0)
    g.duty_u16(0)