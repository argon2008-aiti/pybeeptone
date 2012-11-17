import math
from pyaudio import PyAudio
import sys

class pybeeptone:
    def __init__(self, rate=44100):
        self.rate = 44100
        self.pyaudio = PyAudio()
        self.stream = self.pyaudio.open(
                                format = self.pyaudio.get_format_from_width(1),
                                channels = 1, rate = self.rate, output = True)

    def play_tone(self, freq=1000, duration=0.3):
        rate = self.rate
        length = int(math.ceil(self.rate*duration))
        data = ''.join( [chr(int(math.sin(x/((rate/freq)/math.pi))*127+128)) 
                            for x in xrange(length)] )
        self.stream.write(data)

    def play_rest(self, duration):
        rate = self.rate
        length = int(math.ceil(self.rate*duration))
        data = ''.join( [chr(int(128)) for x in xrange(length)] )
        self.stream.write(data)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio.terminate()
