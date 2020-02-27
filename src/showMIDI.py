from MIDI import MIDIFile
from sys import argv

c = MIDIFile(argv[1])
c.parse()
for track in c:
    track.parse()
    print(str(track))
