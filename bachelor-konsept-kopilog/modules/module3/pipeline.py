import os
import sys

from modules.module5log.logger import log_op
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from modules.module3.rename_file import RenameFileModule

if len(sys.argv) < 2:
    print("❌ Ingen filer spesifisert.")
    log_op(f"Ingen fil spesifisert", level="error", event="error")
    sys.exit(1)

input_dir = "storage/filtered_data"
output_dir = "storage/processed_data"

if __name__ == "__main__":
    
    rename_module = RenameFileModule()

    for file in sys.argv[1:]:  # Itererer over ALLE filene
        input_file = os.path.join(input_dir, file)
        new_name = f"processed_{file}"
        rename_module.process(input_file, output_dir, new_name)
        
    
    print("✅ Modul 3: Alle filer gitt nytt navn i storage/processed/")
    log_op(f"Alle filer gitt nytt navn i storage/processed/", level="info", category="filesystem", event="job_completed")