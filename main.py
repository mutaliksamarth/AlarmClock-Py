# Python Alarm Clock

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "alarm.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")
        if current_time == alarm_time:
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                print("Time to wake up! Stupid!")
                continue
            break

        time.sleep(1)

if __name__ == '__main__':
    alarm_time = input("Enter the time for the alarm in format 'HH:MM:SS': ")
    set_alarm(alarm_time)