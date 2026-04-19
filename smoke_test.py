import subprocess
import time

process = subprocess.Popen(['/Users/huzaifamahmood/Desktop/Travel Planner/.venv/bin/python', 'app.py'], 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.STDOUT, 
                           text=True)

time.sleep(5)
process.terminate()
output, _ = process.communicate()
print(output)
