import subprocess
import time
import sys

process = subprocess.Popen([sys.executable, 'app.py'], 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.STDOUT, 
                           text=True)

time.sleep(5)
process.terminate()
output, _ = process.communicate()
print(output)
