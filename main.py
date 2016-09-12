import wave
import struct
import numpy

# Input time
raw_time = input('Start moment, in format 00:00\n').split(':')
start_time = int(raw_time [0]) * 60 + int(raw_time [1])

# Open
w = wave.open("input.wav","rb")
p = w.getparams()
f = p[3]
start_frame = start_time * p[2]
s = w.readframes(start_frame - 1)
w.setpos(start_frame)
s_loudpart = w.readframes(f-start_frame)
w.close()

# Edit
s = numpy.fromstring(s, numpy.int16)
s = struct.pack('h'*len(s), *s)
s_loudpart = numpy.fromstring(s_loudpart, numpy.int16) // 10 * 35
s_loudpart = struct.pack('h'*len(s_loudpart), *s_loudpart)

# Save
w = wave.open("output.wav","wb")
w.setparams(p)
w.writeframes(s)

w.writeframes(s_loudpart)

w.close()
input('Done. Press anykey to exit')
