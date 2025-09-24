import os
import subprocess

def execute_command(command):
    subprocess.run(
        command, 
        check = True,
    )

execute_command("python.exe FWP_Python/7.py")
