from pybeeptone import pybeeptone

# T|  4|---b---G--e--e--e--F--G--a---b---b---b--G
long_note = 0.20
short_note = 0.15

t = pybeeptone()
t.play_tone(988, long_note)    # b
t.play_tone(831, long_note)    # G
t.play_tone(659, short_note)    # e
t.play_tone(659, short_note)    # e
t.play_tone(659, short_note)    # e
t.play_tone(698, short_note)    # F
t.play_tone(831, short_note)    # G
t.play_tone(880, short_note)    # a
t.play_tone(988, long_note)    # b
t.play_tone(988, long_note)    # b
t.play_tone(988, long_note)    # b
t.play_tone(831, short_note)    # G
t.close()
