import functools
import sounddevice
from scipy.io.wavfile import write
import wavio
@functools.cache
def record(freq = 44100,duration = 5):
    recording = sounddevice.rec(int(duration * freq), samplerate=freq, channels=2)
    sounddevice.wait()
    write("recording0.wav", freq, recording)
    wavio.write("recording1.wav", recording, freq, sampwidth=2)