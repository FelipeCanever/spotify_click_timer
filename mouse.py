import win32api

class LeftButton:
	def __init__(self):
		self._state = self._current_state()
	
	@staticmethod
	def _current_state():
		return win32api.GetKeyState(0x01)

	@property
	def released(self):
		new_state = LeftButton._current_state()
	
		if new_state != self._state:
			self._state = new_state

			if self._state >= 0:
				return True
		
		return False
	
