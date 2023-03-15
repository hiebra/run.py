import sys
import subprocess
args = sys.argv
if len(args) > 0:
    try:
        subprocess.check_call(args[1:])
    except:
        pass
else:
    raise Exception('Missing argument: Shell command to run')