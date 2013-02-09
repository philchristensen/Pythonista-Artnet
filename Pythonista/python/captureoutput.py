import _outputcapture
import sys
import traceback
from functools import partial

class StdoutCatcher (object):
	def __init__(self):
		self.encoding = 'utf8'
	def write(self, s):
		if isinstance(s, str):
			_outputcapture.CaptureStdout(s)
		elif isinstance(s, unicode):
			_outputcapture.CaptureStdout(s.encode('utf8'))
	def flush(self):
		pass

class StderrCatcher (object):
	def __init__(self):
		self.encoding = 'utf8'
	def write(self, s):
		if isinstance(s, str):
			_outputcapture.CaptureStderr(s)
		elif isinstance(s, unicode):
			_outputcapture.CaptureStderr(s.encode('utf8'))
	def flush(self):
		pass

class StdinCatcher (object):
	def __init__(self):
		self.encoding = 'utf8'
	def read(self, len=-1):
		return _outputcapture.ReadStdin(len)
	
	def readline(self):
		return _outputcapture.ReadStdin()

def exception_handler(script_path, type, value, tb):
	if tb is not None: 
		tracebacks = traceback.extract_tb(tb)
		for trace in reversed(tracebacks):
			path = trace[0]
			if path == script_path:
				line = trace[1]
				_outputcapture.HandleException(line, type.__name__, str(value))
				break
		else:
			sys.__excepthook__(type, value, tb)

sys.stdout = StdoutCatcher()
sys.stderr = StderrCatcher()
sys.stdin = StdinCatcher()
