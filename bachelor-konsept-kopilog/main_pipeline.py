import sys
from modules.module5log.logger import log_op
import subprocess
import os
import glob

print("✅ Starter hovedpipen for alle filer samtidig...")
log_op(f"Starter hovedpipen for alle filer samtidig...", level="info", event="job_started")

# Opprett nødvendige mapper
os.makedirs("output", exist_ok=True)
os.makedirs("storage/raw_data", exist_ok=True)
os.makedirs("storage/filtered_data", exist_ok=True)
os.makedirs("storage/processed_data", exist_ok=True)

# Hent alle tekstfiler fra input-mappen
input_files = os.listdir("input")

# Fikse for os
python_cmd = "python3" if sys.platform != "win32" else "python"

# Tilbakestiller systemet og flytter filer tilbake
if not input_files:
    print("Ingen tekstfiler funnet i input-mappen.")
    log_op(f"Ingen tekstfiler funnet i input-mappen.", level="warning", category="filesystem", event="file_modify")
    input_files = os.listdir("storage/raw_data")
    subprocess.run([python_cmd, "-m", "modules.module0.pipeline"] + input_files, check=True)
    folder_path = "output"
    for file in glob.glob(f"{folder_path}/*"):  # Henter alle filer i mappen
        os.remove(file)  # Sletter hver fil

    exit(1)

# 1️⃣ Flytt alle filer til raw_data/
print("✅ Initialiserer modul 1")
log_op(f"Initialiserer modul 1", level="info", event="job_started")
subprocess.run([python_cmd, "-m", "modules.module1.pipeline"] + input_files, check=True)

# 2️⃣ Kopier alle filer fra temp/ til output/
raw_files = os.listdir("storage/raw_data")
print("✅ Initialiserer modul 2")
log_op(f"Initialiserer modul 2", level="info", event="job_started")
subprocess.run([python_cmd, "-m", "modules.module2.pipeline"] + raw_files, check=True)

# 3️⃣ Gi alle filer nytt navn i output/
filtered_files = os.listdir("storage/filtered_data")
print("✅ Initialiserer modul 3")
log_op(f"Initialiserer modul 3", level="info", event="job_started")
subprocess.run([python_cmd, "-m", "modules.module3.pipeline"] + filtered_files, check=True)

# 4️⃣ Flytt alle filer til output/
processed_files = os.listdir("storage/processed_data")
print("✅ Initialiserer modul 4")
log_op(f"Initialiserer modul 4", level="info", event="job_started")
subprocess.run([python_cmd, "-m", "modules.module4.pipeline"] + processed_files, check=True)

print("✅ Hovedpipeline fullført! Sjekk output-mappen.")
log_op(f"Hovedpipeline fullført! Sjekk output-mappen.", level="info", event="job_completed")