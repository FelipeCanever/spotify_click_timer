import mouse

if __name__ == "__main__":
	state = mouse.left_button_state()

	while True:
		new_state = mouse.left_button_state()

		if new_state != state:
			state = new_state

			if mouse.has_left_button_been_released(new_state):
				print("Left mouse button released.")
