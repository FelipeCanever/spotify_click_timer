from threading import Timer

class RestartableTimer:
	"""
	A timer that can be restarted at any time.
	"""
	def __init__(self, duration, callback):
		"""
		Keyword arguments:
		duration -- in seconds; the timer will start counting down from this value
		callback -- will be called when the timer reaches zero
		"""
		self.duration = duration
		self.callback = callback

		self._timer = None
		self._reset()
	
	def _reset(self):
		self._timer = Timer(self.duration, self.callback)
	
	def start(self):
		self._timer.start()
	
	def cancel(self):
		self._timer.cancel()

	def restart(self):
		self.cancel()
		self._reset()
		self.start()
