import shutil
import os

from modules.module5log.logger import log_op

class CopyFileModule:
    def process(self, input_file, output_dir):
        new_file = os.path.join(output_dir, os.path.basename(input_file))
        shutil.copy(input_file, new_file)
        print(f"🔄 Fil kopiert til: {new_file}")
        log_op(f"Kopierte fil til: {new_file}", file=os.path.basename(input_file), type="INFO", stage="1")
        return new_file