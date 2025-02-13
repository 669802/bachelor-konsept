import os
import sys

from modules.module5log.logger import log_op
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from modules.module4.move_file import MoveFileModule

if len(sys.argv) < 2:
    print("❌ Ingen fil spesifisert.")
    log_op(f"Ingen fil spesifisert.", level="error", category="filesystem", event="error")
    sys.exit(1)

input_dir = os.path.join("storage", "processed_data")
output_dir = "output"

if __name__ == "__main__":
    
    move_module = MoveFileModule()

    for file in sys.argv[1:]:  # Itererer over ALLE filene
        input_file = os.path.join(input_dir, file)
        move_module.process(input_file, output_dir)

    print("✅ Modul 4: Alle filer flyttet til output/")
    log_op(f"Alle filer flyttet til output/", level="info", category="filesystem", event="job_completed")