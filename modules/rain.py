import speech_recognition as sr
import simpleaudio as sa
import time
import threading
from pydub import AudioSegment

class Rain:
  def __init__(self, recognizer, microphone):
    self.recognizer = recognizer
    self.microphone = microphone
    self.stop_event = threading.Event()

  # Construct an audio buffer from an MP3 file
  def _audio_buffer(self, file_path):
    audio = AudioSegment.from_mp3(file_path)
    return sa.play_buffer(
      audio.raw_data,
      num_channels=audio.channels,
      bytes_per_sample=audio.sample_width,
      sample_rate=audio.frame_rate
    )
  
  def _wait_for_audio(self, buffer):
    buffer.wait_done()

  # Listen for voice commands while the audio is playing
  def _listen_while_playing(self):
    while not self.stop_event.is_set():
      time.sleep(30)
      with self.microphone as source:
        audio = self.recognizer.listen(source)
      try:
        value = self.recognizer.recognize_google(audio)
        if value == 'stop now': self.stop_event.set()
      except sr.UnknownValueError:
        continue
      except sr.RequestError as e:
        print(e)

  # Use threads to play rain sounds and listen for commands
  def play_rain(self, max_play_count):
    play_count = 0
    while play_count < max_play_count:
      self.stop_event.clear()
      rain_1 = self._audio_buffer('./assets/rain_1.mp3')
      rain_2 = self._audio_buffer('./assets/rain_2.mp3')

      rain_thread_1 = threading.Thread(target=self._wait_for_audio, args=(rain_1,))
      rain_thread_2 = threading.Thread(target=self._wait_for_audio, args=(rain_2,))
      listen_thread = threading.Thread(target=self._listen_while_playing)

      rain_thread_1.start()
      rain_thread_2.start()
      listen_thread.start()

      while True:
        if self.stop_event.is_set():
          # threads were commanded to stop
          rain_1.stop()
          rain_2.stop()
          play_count = max_play_count # don't play again
          break
        if not rain_thread_1.is_alive() and not rain_thread_2.is_alive():
          # threads stopped naturally
          self.stop_event.set() # signal the listening thread to stop
          break

      rain_thread_1.join()
      rain_thread_2.join()
      listen_thread.join()
      play_count += 1
