import os
import time
import argparse
import subprocess
from watchdog.tricks import Trick
from watchdog.observers.polling import PollingObserver as Observer

class ReloadTrick(Trick):
	def __init__(self, command, patterns=None):
		if patterns: patterns = patterns.split(";")
		super(ReloadTrick, self).__init__(patterns)
		self.process = None
		self.command = command
		self.start()

	def on_any_event(self, event):
		print "Reload.py killing command: {}".format(self.command)
		self.kill()
		print "Reload.py starting command: {}".format(self.command)
		self.start()

	def start(self):
		self.process = subprocess.Popen(self.command, shell=True, preexec_fn=os.setsid)

	def kill(self):
		if self.process is None: return
		try:
			os.killpg(os.getpgid(self.process.pid), 9)
		except OSError:
			pass
		self.process = None

def main():
	# parse command line arguments
	parser = argparse.ArgumentParser(description='Watches a directory and restarts a script on file changes.')
	parser.add_argument("command", help="Command to run and reload when file changes are detected. For example: 'echo hello!'")
	parser.add_argument("-d", "--directory", help="Directory to watch.", default=".")
	parser.add_argument("-p", "--patterns", help="Pattern limiting which files trigger a reload. For example: '*.txt;*.py'", default=None)
	args = parser.parse_args()

	# setup observer
	trick = ReloadTrick(args.command, patterns=args.patterns)
	observer = Observer(timeout=1.0)
	observer.schedule(trick, args.directory, recursive=True)

	# start reloader process
	observer.start()
	try:
		while True: time.sleep(1.0)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()

if __name__ == "__main__":
	main()
