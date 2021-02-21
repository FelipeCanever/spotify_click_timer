from mouse import LeftButton
from restartable_timer import RestartableTimer

DURATION = 15

def beep():
	print("\a")

if __name__ == "__main__":
	button = LeftButton()
	timer = RestartableTimer(DURATION, beep)

	while True:
		if button.released:
			print("Left mouse button released.")
			timer.restart()
