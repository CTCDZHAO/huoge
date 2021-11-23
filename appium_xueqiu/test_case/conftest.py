import os
import shlex
import signal
import subprocess

import pytest

@pytest.fixture(scope="class", autouse=True)
def record():
    path=os.path.dirname(os.path.abspath(__file__))
    cmd = shlex.split(f"scrcpy --record {path}/tmp.mp4")
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)