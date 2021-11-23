import time
import board
import digitalio

import neopixel

import usb_midi
import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn


## solenoid
s1 = digitalio.DigitalInOut(board.D9)
s1.direction = digitalio.Direction.OUTPUT

s2 = digitalio.DigitalInOut(board.D10)
s2.direction = digitalio.Direction.OUTPUT

s3 = digitalio.DigitalInOut(board.D11)
s3.direction = digitalio.Direction.OUTPUT


# 0 is MIDI channel 1
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], in_channel=0)

# led
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.1

while True:
    msg = midi.receive()
    
    if msg is not None:

        if isinstance(msg, NoteOn):
            mod = msg.note % 3
            if mod == 0:
                pixel.fill((255,0,0))
                s1.value = True
            elif mod == 1:
                pixel.fill((0,255,0))
                s2.value = True
            elif mod == 2:
                pixel.fill((0,0,255))
                s3.value = True
        else:
            pixel.fill((255,255,255))
            s1.value = False
            s2.value = False
            s3.value = False
