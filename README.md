# Command Centre

Experimenting with Python voice recognition to build a personal collection of voice-controlled utilities.

## Setup

- Install Python 3.11.12
  - Use whichever method you prefer. If you use [mise](https://github.com/jdx/mise) you can just run `mise install`.

- Set up virtual environment
  - Run `python -m venv venv`

- Activate virtual environment
  - Run `source venv/bin/activate`

- Install dependencies
  - Run `pip install -r requirements.txt`

- Vosk
  - Download a model from https://alphacephei.com/vosk/models, create a `model` folder in the root of the project and put the model files in to it

- Microphone
  - You may need to configure your microphone settings or input volume for the voice commands to be interpreted comfortably

## Run

Run `python command_centre.py` or give `command_centre.py` executable permissions and run `./command_centre.py`

Say `help me` to display the list of available voice commands. Say `shut down` to play the shutdown sound found in `assets/` and exit.

## Utilities

There is currently one functional utility

### Rain

See `modules/rain.py`. Uses threads to play the rain sound files found in `assets/`. Say any phrase containing the word `rain` to start playback. Press `Ctrl-C` to stop playback and return to the command centre. Play count can be passed to `Rain.play` to loop the audio.

## Notes

Voice commands with more than one syllable are more reliably interpreted

Playback using local sound files works when the screen is locked (unlike YouTube videos for example) and removes any online dependency

Using [Vosk](https://github.com/alphacep/vosk-api) for offline speech recognition also removes any online dependency
