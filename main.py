import subprocess
while True:
     CREATE_NO_WINDOW = 0x08000000
     subprocess.call('taskkill /F /IM etkontrol.exe',creationflags=DETACHED_PROCESS)
