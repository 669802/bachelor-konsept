import os

from modules.module5log.logger import log_op

class RenameFileModule:
    def process(self, input_file, output_dir, new_name):
        if not os.path.exists(input_file):
            print(f"❌ Fil ikke funnet: {input_file}")
            log_op(f"Fil ikke funnet: {input_file}", type="ERROR")
            return None

        new_file_path = os.path.join(output_dir, new_name)

        try:
            os.rename(input_file, new_file_path)
            print(f"🔄 Filen ble omdøpt til: {new_file_path}")
            log_op(f"Filen ble omdøpt til: {new_file_path}", file=os.path.basename(input_file), type="INFO", stage="1")
            os.rename(os.path.join(f"logs\\1", f"log_{os.path.basename(input_file)}.txt"), os.path.join(f"logs\\2", f"log_{os.path.basename(new_file_path)}.txt"))
            return new_file_path
        except Exception as e:
            print(f"❌ Feil ved omdøping av {input_file}: {e}")
            log_op(f"Feil ved omdøping av {input_file}: {e}", file=os.path.basename(input_file), type="ERROR", stage="1")
            log_op(f"Feil ved omdøping av {input_file}: {e}", type="ERROR")
            return None