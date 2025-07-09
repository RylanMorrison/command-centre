#!venv/bin/python3

import speech_recognition as sr
import simpleaudio as sa
import time
import json
from modules.rain import Rain

# suppress vosk logs
from vosk import SetLogLevel
SetLogLevel(-1)

class CommandCentre:
  def __init__(self):
    self.recognizer = sr.Recognizer()
    self.microphone = sr.Microphone()

  def _play_shutdown(self):
    shutdown_sound = sa.WaveObject.from_wave_file("./assets/shutdown.wav")
    shutdown_sound.play().wait_done()

  def run(self):
    try:
      with self.microphone as source:
        self.recognizer.adjust_for_ambient_noise(source) # calibrate
      while True:
        time.sleep(1)

        with self.microphone as source:
          audio = self.recognizer.listen(source)
          try:
            value = json.loads(self.recognizer.recognize_vosk(audio))['text']
          except sr.UnknownValueError:
            print("Didn't catch that, try again.")
            continue
          except sr.RequestError as e:
            print(e)
            continue

        if value == 'play rain':
          Rain(self.recognizer, self.microphone).play_rain(4)
        elif value == 'shut down':
          print('Shutting down')
          self._play_shutdown()
          break
        elif value == 'help me':
          print(
            "\nAvailable commands:\n"
            "- 'play rain': Start the playback of rain.\n"
            "- 'stop now': Stop the playback of rain.\n"
            "- 'shut down': Shutdown the Command Centre.\n"
            "- 'help me': Show this help message.\n"
          )
        else:
          print(value)

    except KeyboardInterrupt:
      return

if __name__ == "__main__":
  print("Command Centre is running. Say 'help me' for commands.")
  CommandCentre().run()
  print('Command Centre has stopped.')
