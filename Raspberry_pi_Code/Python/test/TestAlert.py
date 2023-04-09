import sys

key_press = sys.stdin.readline().strip()
if key_press == "a":
	print("BIG ALERT")
elif key_press == "s":
	print("SMALL ALERT")
else:
	print("You entered '", key_press, "'.")