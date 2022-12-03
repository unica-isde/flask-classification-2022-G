import subprocess

subprocess.Popen("sudo -s python worker.py", start_new_session=True, shell=True)

subprocess.Popen("sudo -s python worker_histo.py", start_new_session=True, shell=True)

subprocess.Popen("sudo -s python runserver.py",start_new_session=True, shell=True)
