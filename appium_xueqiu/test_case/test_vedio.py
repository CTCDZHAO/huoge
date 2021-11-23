import os
import shlex
import signal
import subprocess
from time import sleep


def test_vedio():
    path = os.path.dirname(os.path.abspath(__file__))
    cmd=shlex.split(f"scrcpy --record {path}/tmp.mp4")
    cmd=f"scrcpy --record {path}/tmp.mp4"
    p=
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(p)
    sleep(10)
    os.kill(p.pid, signal.CTRL_C_EVENT)