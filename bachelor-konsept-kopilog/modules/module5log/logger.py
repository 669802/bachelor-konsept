import time
import os
import sys
import json
import uuid
from datetime import datetime

if not os.path.exists("logs"):
    os.mkdir("logs")

def log_op(message, file="System", level="info", category="application", event="unspecified"):
    call_loc = sys._getframe(1)
    with open(os.path.join(f"logs\\{category}", f"log_{file}.txt"), "a", encoding="utf-8") as log:
        json.dump({"@timestamp": datetime.utcnow().isoformat() + "Z", "log.level": level.lower(), "message": message, "event": {"category": category, "type": event}, "process": {"pid": os.getpid(), "name": file}, "source": {"file": os.path.basename(call_loc.f_code.co_filename)}, "trace": {"id": str(uuid.uuid4())}}, log)
        log.write("\n")