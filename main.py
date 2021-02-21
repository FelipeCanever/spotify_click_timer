from mouse import LeftButton

if __name__ == "__main__":
	button = LeftButton()

	while True:
		if button.released:
			print("Left mouse button released.")
