import subprocess

args = ['ping','-c', '5','ya.ru']
subprocess_ping = subprocess.Popen(args,stdout=subprocess.PIPE)

for line in subprocess_ping.stdout:
    print(line.decode())

