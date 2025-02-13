import shutil
import os

from modules.module5log.logger import log_op

class MoveFileModule:
    def process(self, input_file, output_dir):
        new_file = os.path.join(output_dir, os.path.basename(input_file))
        shutil.move(input_file, new_file)
        print(f"🔄 Flyttet fil til: {new_file}")
        log_op(f"Flyttet fil til: {new_file}", file=os.path.basename(input_file), type="INFO", stage="2")
        return new_file