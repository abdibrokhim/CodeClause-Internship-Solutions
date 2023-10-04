import pygame
import os
import sys
import argparse

pygame.init()
pygame.mixer.init()

def get_music_files(music_dir):
    return [f for f in os.listdir(music_dir) if f.endswith((".mp3", ".wav"))]

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    parser = argparse.ArgumentParser(description="Awesome Music Player")
    parser.add_argument('-d', '--directory', required=True, help="Directory where music files are located")
    args = parser.parse_args()

    music_dir = args.directory
    music_files = get_music_files(music_dir)

    if not music_files:
        print("No music files found in the directory.")
        sys.exit(1)

    current_track = 0
    playing = False

    while True:
        print("\nAwesome Music Player")
        print("------------")
        print("1. Play")
        print("2. Pause/Resume")
        print("3. Next Track")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if not playing:
                play_music(os.path.join(music_dir, music_files[current_track]))
                playing = True
        elif choice == "2":
            if playing:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            else:
                pygame.mixer.music.unpause()
                playing = True
        elif choice == "3":
            if playing:
                stop_music()
                current_track = (current_track + 1) % len(music_files)
                play_music(os.path.join(music_dir, music_files[current_track]))
            else:
                print("No music is playing.")
        elif choice == "4":
            if playing:
                stop_music()
            pygame.quit()
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
