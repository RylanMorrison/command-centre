#!venv/bin/python3

import speech_recognition as sr
import simpleaudio as sa
import time
from modules.rain import Rain

class CommandCentre:
  def __init__(self):
    self.recognizer = sr.Recognizer()
    self.microphone = sr.Microphone()

  def _play_shutdown(self):
    shutdown_sound = sa.WaveObject.from_wave_file("./assets/shutdown.wav")
    play_shutdown = shutdown_sound.play()
    play_shutdown.wait_done()

  def run(self):
    try:
      with self.microphone as source:
        self.recognizer.adjust_for_ambient_noise(source) # calibrate
      while True:
        time.sleep(0.5)
        with self.microphone as source:
          audio = self.recognizer.listen(source)
        try:
          value = self.recognizer.recognize_google(audio)

          if value == 'make it rain':
            Rain(self.recognizer, self.microphone).play_rain(3)
          elif value == 'shut down':
            self._play_shutdown()
            break
          elif value == 'help me':
            print(
              "\nAvailable commands:\n"
              "- 'make it rain': Start the playback of rain.\n"
              "- 'stop now': Stop the playback of rain.\n"
              "- 'shut down': Shutdown the Command Centre.\n"
              "- 'help me': Show this help message.\n"
            )
          else:
            print(value)
        except sr.UnknownValueError:
          print("Didn't catch that, try again.")
        except sr.RequestError:
          pass
    except KeyboardInterrupt:
      return

if __name__ == "__main__":
  print("Command Centre is running. Say 'help' for commands.")
  CommandCentre().run()
  print("Command Centre has stopped.")
