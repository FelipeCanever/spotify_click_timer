from psutil import Process
from win32gui import GetForegroundWindow
from win32process import GetWindowThreadProcessId

def foreground_window():
	"""A handle to the window currently on the foreground."""
	return GetForegroundWindow()

def process_name(window):
	try:
		p_id = GetWindowThreadProcessId(window)
		return Process(p_id[-1]).name()
	except:
		return ""
