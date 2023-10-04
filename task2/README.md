# Awesome Music Player

The Awesome Music Player is a simple Python script that allows you to play music files (MP3 and WAV) from a specified directory using the Pygame library. You can control playback with options such as play, pause/resume, skip to the next track, and quit.

## Prerequisites

Before you can use this script, make sure you have the following installed:

- Python 3.x
- Pygame library

## Usage

Clone this repository

```shell
git clone https://github.com/abdibrokhim/CodeClause-Internship-Solutions/
```

Open a terminal and navigate to the directory where you cloned the repository.

Install the required packages using the following command:

```shell
python -m pip install -U pygame==2.5.2 --user
```

Run the script using the following command:

```shell
python main.py -d YOUR_MUSIC_DIRECTORY
```

Replace `YOUR_MUSIC_DIRECTORY` with the path to the directory containing your music files (MP3 and WAV).

The Awesome Music Player will start, and you'll see a menu in the terminal with the following options:

1. `Play`: Starts playing music.
2. `Pause/Resume`: Pauses or resumes music playback.
3. `Next Track`: Skips to the next track in the playlist.
4. `Quit`: Quits the music player.

Use the corresponding number keys (1, 2, 3, or 4) to select the desired option.