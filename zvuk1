import wave
import struct
n = int(input())
source = wave.open("in.wav", mode="rb")
dest = wave.open("out.wav", mode="wb")
dest.setparams(source.getparams())
frames_count = source.getnframes()
data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
if n > 0:
    newdata = [n*x for x in data]
else:
    newdata = [x//(-1 * n) for x in data]
newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
dest.writeframes(newframes)
source.close()
dest.close()
