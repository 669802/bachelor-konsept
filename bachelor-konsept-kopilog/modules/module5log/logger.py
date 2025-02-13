import time
import os
import sys

if not os.path.exists("logs"):
    os.mkdir("logs")

def log_op(message, file="System", type="Unspecified", stage="0"):
    call_loc = sys._getframe(1)
    with open(os.path.join(f"logs\\{stage}", f"log_{file}.txt"), "a", encoding="utf-8") as log:
        log.write(time.strftime("[%Y-%m-%d %H:%M:%S]") + "[" + os.path.basename(os.path.dirname(call_loc.f_code.co_filename)) + "/" + os.path.basename(call_loc.f_code.co_filename) + "]" + f" {type} - {message}\n")