from mouse import LeftButton
from restartable_timer import RestartableTimer
from window import foreground_window, process_name

DURATION = 15
PROCESS_NAME = "Spotify.exe"

def beep():
	print("Skip song ahead.")
	print("\a")

if __name__ == "__main__":
	button = LeftButton()
	timer = RestartableTimer(DURATION, beep)

	while True:
		if button.released:
			if process_name(foreground_window()) == PROCESS_NAME:
				print(f"{DURATION}-second timer started...")
				timer.restart()
