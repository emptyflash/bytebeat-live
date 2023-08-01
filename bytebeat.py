import sys
import threading
import time
import math


with open("livecode.bb", "r") as f:
    program_src = f.read()
    program = eval("lambda t: " + program_src)
    program_dict = {
        "program_fn": program,
        "old_program_fn": program,
        "last_src": program_src,
    }

def reload_program(program_dict):
    while True:
        with open("livecode.bb", "r") as f:
            program_src = f.read()
            if program_dict["last_src"] != program_src:
                try:
                    program_dict["program_fn"] = eval("lambda t: " + program_src)
                except Exception as e:
                    sys.stderr.write(str(e) + "\n")
                    continue
                program_dict["old_program_fn"] = program_dict["program_fn"]
                program_dict["last_src"] = program_src
        time.sleep(1)

threading.Thread(target=reload_program, args=(program_dict,), daemon=True).start()

t = 0
while True:
    t += 1
    try:
        sys.stdout.write(chr(program_dict["program_fn"](t)))
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        program_dict["program_fn"] = program_dict["old_program_fn"]
