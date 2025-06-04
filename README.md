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
  - Run `pip install -r requirements.txt`xw

- Microphone
  - You may need to configure your microphone settings or input volume for the voice commands to be interpreted comfortably

## Run

Run `python command_centre.py` or give `command_centre.py` executable permissions and run `./command_centre.py`

Say `help me` to display the list of available voice commands. Say `shut down` to play the shutdown sound found in `assets/` and exit.

## Utilities

There is currently one functional utility

### Rain

See `modules/rain.py`. Uses threads to play the rain sound files found in `assets/`. Say `make it rain` to start playback. Say `stop now` to stop playback at any time and return to the command centre. Command listening is staggered while sound is playing to save resources. You may have to speak louder to be heard over the sound. Playback loops 3 times for around 40 minutes total playback time.

## Notes

Voice commands with more than one syllable are more reliably interpreted

Playback using local sound files works when the screen is locked (unlike YouTube videos for example) and removes any online dependency
