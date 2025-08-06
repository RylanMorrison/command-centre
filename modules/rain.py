import simpleaudio as sa
from threading import Thread
from pydub import AudioSegment

RAIN_1_PATH = './assets/rain_1.mp3'
RAIN_2_PATH = './assets/rain_2.mp3'

class Rain:
  def _init_threads(self):
    self.threads: list[Thread] = []
    self._init_audio_buffers()

    for buffer in self.audio_buffers:
      self.threads.append(self._new_thread(buffer))

  def _init_audio_buffers(self):
    self.audio_buffers: list[sa.PlayObject] = [
      self._audio_buffer(RAIN_1_PATH),
      self._audio_buffer(RAIN_2_PATH)
    ]

  def _new_thread(self, audio_buffer) -> Thread:
    return Thread(target=self._wait_for_audio, args=(audio_buffer,))

  # Construct an audio buffer from an MP3 file
  def _audio_buffer(self, file_path) -> sa.PlayObject:
    audio = AudioSegment.from_mp3(file_path)
    return sa.play_buffer(
      audio.raw_data,
      num_channels=audio.channels,
      bytes_per_sample=audio.sample_width,
      sample_rate=audio.frame_rate
    )

  def _wait_for_audio(self, buffer):
    buffer.wait_done()

  def _stop_playback(self):
    for buffer in self.audio_buffers:
      buffer.stop()

  def _start_threads(self):
    for thread in self.threads:
      thread.start()

  def _wait_for_threads(self):
    for thread in self.threads:
      thread.join()

  # Use threads to play the sounds of rain
  def play(self, max_play_count):
    print("It's raining")
    play_count = 0
    while play_count < max_play_count:
      try:
        self._init_threads()
        self._start_threads()

        self._wait_for_threads()
        play_count += 1
      except KeyboardInterrupt:
        self._stop_playback()
        self._wait_for_threads()
        # don't play again
        play_count = max_play_count
    print('Rain stopped')
