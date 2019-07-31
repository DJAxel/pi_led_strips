from gpiozero import PWMLED
from gpiozero import Button
from time import sleep
from signal import pause

cold_led = PWMLED(15)
warm_led = PWMLED(14)
plus_btn = Button(2)
minus_btn = Button(3)
warm_btn = Button(21)
cold_btn = Button(20)
brightness = 50
warmth = 50

def printStripValues(warm, cold):
    for strip in [warm, cold]:
        slider = ""
        for i in range(51):
            if i/50 <= strip and (i+1)/50 > strip:
                slider += "|"
            else:
                slider += "-"
        print(slider, " ", round(strip*100, 1), "%", sep="")
    print()
        

def update_brightness():
    b = pow(brightness/100, 2)
    warm = b*(warmth/100)
    cold = b*(1-warmth/100)
    printStripValues(warm, cold)
    warm_led.value = warm
    cold_led.value = cold

def increase():
    global brightness
    brightness = min(brightness+5, 100)
    if brightness == 100:
        cold_led.value = .3;
        warm_led.value = .3;
        sleep(.1)
    update_brightness()

def decrease():
    global brightness
    brightness = max(brightness-5, 0)
    update_brightness()

def warmer():
    global warmth
    warmth = min(warmth+5, 100)
    update_brightness()

def colder():
    global warmth
    warmth = max(warmth-5, 0)
    update_brightness()

update_brightness()
plus_btn.when_pressed = increase
minus_btn.when_pressed = decrease
warm_btn.when_pressed = warmer
cold_btn.when_pressed = colder



pause()
