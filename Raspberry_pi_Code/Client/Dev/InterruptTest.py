import subprocess
#import select   # not supported on Windows
import sys

# Start the first subprocess (infinite slideshow)
proc1 = subprocess.Popen(['python', 'LoopSlidesOS.py'], stdout=subprocess.PIPE)

# Start the second subprocess (event monitor)
proc2 = subprocess.Popen(['python', 'TestAlert.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

try:
	# Monitor the output of the second subprocess
	while True:
		# Check if there is any new keyboard input
		try:
			key_press = input()
		except EOFError:
			break
			
		proc2.stdin.write((key_press+"\n").encode())
		proc2.stdin.flush()
		
		# Read any output from the subprocess
		output, _ = proc2.communicate()
		output = output.decode().strip()
		print(output)
		if output:
			if output == "BIG ALERT":
				# If the second subprocess prints "BIG ALERT", kill the first subprocess and run a third subprocess
				proc1.terminate()  # Use kill() to force kill the subprocess if terminate() isn't good enough
				proc1.wait()  # Wait for the first subprocess to actually terminate
				proc3 = subprocess.Popen(['python', 'BigAlert.py'])
			elif output == "SMALL ALERT":
				# If the second subprocess prints "SMALL ALERT", run a fourth subprocess
				proc4 = subprocess.Popen(['python', 'SmallAlert.py'])
				
		# Reinitialize the event monitor
		proc2 = subprocess.Popen(['python', 'TestAlert.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
		
except KeyboardInterrupt:
    # Clean up and exit gracefully on keyboard interrupt
	proc1.terminate()
	proc1.wait()
	proc2.terminate()
	proc2.wait()