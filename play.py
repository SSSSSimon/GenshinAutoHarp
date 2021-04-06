import mido, time, sys
from pynput.keyboard import Controller

mid = mido.MidiFile(sys.argv[1])
keyboard = Controller()

def note_to_key(note):
    if note ==  48 :
        return 'z'
    elif note ==  50 :
        return 'x'
    elif note ==  52 :
        return 'c'
    elif note ==  53 :
        return 'v'
    elif note ==  55 :
        return 'b'
    elif note ==  57 :
        return 'n'
    elif note ==  59 :
        return 'm'
    elif note ==  60 :
        return 'a'
    elif note ==  62 :
        return 's'
    elif note ==  64 :
        return 'd'
    elif note ==  65 :
        return 'f'
    elif note ==  67 :
        return 'g'
    elif note ==  69 :
        return 'h'
    elif note ==  71 :
        return 'j'
    elif note ==  72 :
        return 'q'
    elif note ==  74 :
        return 'w'
    elif note ==  76 :
        return 'e'
    elif note ==  77 :
        return 'r'
    elif note ==  79 :
        return 't'
    elif note ==  81 :
        return 'y'
    elif note ==  83 :
        return 'u'
    else:
        return 'k'
    
time.sleep(5)
for msg in mid.play():
    if msg.type == 'note_on':
        keyboard.tap(note_to_key(msg.note))
