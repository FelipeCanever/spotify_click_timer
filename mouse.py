import win32api

def left_button_state():
	return win32api.GetKeyState(0x01)

def has_left_button_been_released(state):
	return state >= 0
