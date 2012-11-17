from pybeeptone import pybeeptone

long_note = 0.20
short_note = 0.15

octave_1 = dict( [
            ("c",   523.25),
            ("C",   554.37),
            ("d",   587.33),
            ("D",   622.25),
            ("e",   659.26),
            ("f",   698.46),
            ("F",   739.99),
            ("g",   783.99),
            ("G",   830.61),
            ("a",   880.00),
            ("A",   932.33),
            ("b",   987.77) ] )

octave_2 = dict( [  
            ("c",   1046.50),
            ("C",   1108.73),
            ("d",   1174.66),
            ("D",   1244.51),
            ("e",   1318.51),
            ("f",   1396.91),
            ("F",   1479.98),
            ("g",   1567.98),
            ("G",   1661.22),
            ("a",   1760.00),
            ("A",   1864.66),
            ("b",   1975.53) ] )

# T|  4|---b---G--e--e--e--F--G--a---b---b---b--G
tune = [    ("b",   long_note),
            ("G",   long_note),
            ("e",   short_note),
            ("e",   short_note),
            ("e",   short_note),
            ("F",   short_note),
            ("G",   short_note),
            ("a",   short_note),
            ("b",   long_note),
            ("b",   long_note),
            ("b",   long_note),
            ("G",   short_note) ]
                            
octave = octave_2

# play General Lee Dixie horn three times
t = pybeeptone()
for _ in range(3):
    for (note,dur) in tune:
        t.play_tone(octave[note], dur)
        t.play_rest(0.02)
    t.play_rest(0.2)
t.close()
