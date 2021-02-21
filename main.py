import win32api

def get_left_mouse_button_state():
	return win32api.GetKeyState(0x01)

def has_left_mouse_button_been_released(state):
	return state >= 0


if __name__ == "__main__":
	state = get_left_mouse_button_state()

	while True:
		new_state = get_left_mouse_button_state()

		if new_state != state:
			state = new_state

			if has_left_mouse_button_been_released(new_state):
				print("Left mouse button released.")
