import subprocess
subprocess.Popen("systemctl restart redis-server.service", shell=True)
subprocess.Popen("x-terminal-emulator -e \"python worker.py\" & x-terminal-emulator -e \"python worker_histo.py\" & x-terminal-emulator -e \"python runserver.py\"", shell=True)
