import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import sys

class VoiceRecorder:
    def __init__(self):
        self.freq = 44100
        self.recording = []
        self.running = True

    def record(self):
        print("Recording started. Press ESC to stop.")
        with sd.InputStream(samplerate=self.freq,channels=2,callback=self.audio_callback):
            while self.running:
                sd.sleep(100)
        self.save_recording()

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        if self.running:
            self.recording.append(indata.copy())
    def stop(self):
        self.running = False

    def save_recording(self):
        if self.recording:
            audio_data=np.concatenate(self.recording, axis=0)
            write("recording.wav",self.freq,audio_data)
