#fake_utility.py, just generates lots of output over time
import sys, time
for i in range(10):
   print(i)
   sys.stdout.flush()
   time.sleep(0.5)

#display out put line by line
import subprocess
proc = subprocess.Popen(['python','Test2.py'],stdout=subprocess.PIPE)
#works in python 3.0+
#for line in proc.stdout:
for line in iter(proc.stdout.readline,''):
   print(line.rstrip())