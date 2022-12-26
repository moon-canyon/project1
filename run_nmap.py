import subprocess

def nmapscan():
    subprocess.run('nmap -sP -v -oX scan.xml 192.168.8.0/24', shell=True)

