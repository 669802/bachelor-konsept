import os
import sys

from modules.module5log.logger import log_op
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from modules.module1.move_file import MoveFileModule

if len(sys.argv) < 2:
    print("❌ Ingen fil spesifisert.")
    log_op(f"Ingen fil spesifisert", type="ERROR")
    sys.exit(1)

input_dir = "input"
output_dir = "storage/raw_data"

if __name__ == "__main__":
   
    move_module = MoveFileModule()

    for file in sys.argv[1:]:  # Itererer over ALLE filene
        input_file = os.path.join(input_dir, file)
        move_module.process(input_file, output_dir)  

    print("✅ Modul 1: Alle filer flyttet til storage/raw_data")
    log_op(f"Alle filer flyttet til storage/raw_data", type="INFO")