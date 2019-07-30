from gpiozero import PWMLED
from gpiozero import Button
from time import sleep
from signal import pause

led = PWMLED(15)
plus_btn = Button(2)
minus_btn = Button(3)
brightness = 50;

def update_brightness():
    b = pow(brightness/100, 2)
    print("Brightness set to ", b*100, "%")
    if brightness == 100:
        led.value = .3;
        sleep(.1)
    led.value = b

def increase():
    global brightness
    brightness = min(brightness+5, 100)
    update_brightness()

def decrease():
    global brightness
    brightness = max(brightness-5, 0)
    update_brightness()

update_brightness()
plus_btn.when_pressed = increase
minus_btn.when_pressed = decrease



pause()
