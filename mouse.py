import win32api

class LeftButton:
	def __init__(self):
		self._state = self._current_state()
	
	@staticmethod
	def _current_state():
		return win32api.GetKeyState(0x01)

	def _state_changed(self, callback):
		"""
		Returns whether the button's state has changed.	

		Keyword arguments:
		callback -- in case the state has changed, the function testing its value
		"""
		new_state = LeftButton._current_state()
	
		if new_state != self._state:
			self._state = new_state

			if callback(self._state):
				return True
		
		return False
	
	@property
	def released(self):
		return self._state_changed(lambda state: state >= 0)
