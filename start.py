import subprocess


subprocess.call("sudo -s python runserver.py", shell=True)
subprocess.call("sudo -s python worker.py", shell=True)
subprocess.call("sudo -s python worker_histo.py", shell=True)
