import subprocess
import os
import glob

print("✅ Starter hovedpipen for alle filer samtidig...")

# Opprett nødvendige mapper
os.makedirs("output", exist_ok=True)
os.makedirs("storage/raw_data", exist_ok=True)
os.makedirs("storage/filtered_data", exist_ok=True)
os.makedirs("storage/processed_data", exist_ok=True)

# Hent alle tekstfiler fra input-mappen
input_files = os.listdir("input")

# Tilbakestiller systemet og flytter filer tilbake
if not input_files:
    print("Ingen tekstfiler funnet i input-mappen.")
    input_files = os.listdir("storage/raw_data")
    subprocess.run(["python3", "modules/module0/pipeline.py"] + input_files, check=True)
    folder_path = "output"
    for file in glob.glob(f"{folder_path}/*"):  # Henter alle filer i mappen
        os.remove(file)  # Sletter hver fil

    exit(1)

# 1️⃣ Flytt alle filer til raw_data/
print("✅ Initialiserer modul 1")
subprocess.run(["python3", "modules/module1/pipeline.py"] + input_files, check=True)

# 2️⃣ Kopier alle filer fra temp/ til output/
raw_files = os.listdir("storage/raw_data")
print("✅ Initialiserer modul 2")
subprocess.run(["python3", "modules/module2/pipeline.py"] + raw_files, check=True)

# 3️⃣ Gi alle filer nytt navn i output/
filtered_files = os.listdir("storage/filtered_data")
print("✅ Initialiserer modul 3")
subprocess.run(["python3", "modules/module3/pipeline.py"] + filtered_files, check=True)

# 4️⃣ Flytt alle filer til output/
processed_files = os.listdir("storage/processed_data")
print("✅ Initialiserer modul 4")
subprocess.run(["python3", "modules/module4/pipeline.py"] + processed_files, check=True)

print("✅ Hovedpipeline fullført! Sjekk output-mappen.")