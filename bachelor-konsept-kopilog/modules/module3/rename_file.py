import os

from modules.module5log.logger import log_op

class RenameFileModule:
    def process(self, input_file, output_dir, new_name):
        if not os.path.exists(input_file):
            print(f"❌ Fil ikke funnet: {input_file}")
            log_op(f"Fil ikke funnet: {input_file}", level="error", event="error")
            return None

        new_file_path = os.path.join(output_dir, new_name)

        try:
            os.rename(input_file, new_file_path)
            print(f"🔄 Filen ble omdøpt til: {new_file_path}")
            log_op(f"Filen ble omdøpt til: {new_file_path}", file=os.path.basename(input_file), level="info", category="filesystem", event="file_modify")
            return new_file_path
        except Exception as e:
            print(f"❌ Feil ved omdøping av {input_file}: {e}")
            log_op(f"Feil ved omdøping av {input_file}: {e}", file=os.path.basename(input_file), level="error", event="error", category="filesystem")
            log_op(f"Feil ved omdøping av {input_file}: {e}", level="error", category="filesystem", event="error")
            return None