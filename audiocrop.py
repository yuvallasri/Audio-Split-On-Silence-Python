import argparse
from pydub import AudioSegment
from pydub.silence import split_on_silence
import time
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

start_time = time.time()
number_of_tracks = 0
file_location = None
parser = argparse.ArgumentParser()
parser.add_argument("-in", "--input_file", type=str, help="input file name")
parser.add_argument("-out", "--output_file", default="out/track_%d.wav", type=str, help="output file name")
parser.add_argument("-min", "--min_silence_len", default=500, type=int, help="(in ms) minimum length of a silence to be used for")
parser.add_argument("-th", "--silence_thresh", default=-40, type=int, help="(in dBFS) anything quieter than this will be (40,60,100)")
parser.add_argument("-ks", "--keep_silence", default=200, type=int, help="(in ms) amount of silence to leave at the beginning")
args = parser.parse_args()

sound = AudioSegment.from_file('in/test.wav', format="wav")
chunks = split_on_silence(sound, min_silence_len=args.min_silence_len, silence_thresh=args.silence_thresh, keep_silence=args.keep_silence)

for idx, chunk in enumerate(chunks):
    chunk.export(args.output_file % idx, format="wav")
    number_of_tracks = number_of_tracks + 1

print("numer of splits track: ", number_of_tracks)
print("time to split the file: %s seconds " % (time.time() - start_time))

spf = wave.open("in/dumsample.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
fs = spf.getframerate()

# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)


Time = np.linspace(0, len(signal) / fs, num=len(signal))

plt.figure(1)
plt.title("Signal Wave...")
plt.plot(Time, signal)
plt.show()
