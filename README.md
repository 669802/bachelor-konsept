```
pip install -r requirements.txt
```

Starte server:
```
python3 app.py
```

Starte/Kjøre gjennom terminal:
```
python3 main_pipeline.py
```
Serveren: http://localhost:5000/ || http://127.0.0.1:5000


```
root
├─ input/                 # Filene som skal prosesseres
│  ├─ input0.png
│  ├─ input1.png
│  ├─ input2.txt
│  ├─ input3.txt
│  ├─ input4.log
│  └─ input5.csv
├─ output/                # Filene som er ferdig prosessert
├─ modules/
│  ├─ __init__py
│  ├─ module0/            # Setter filene tilbake til utgangspunkt
│  │  ├─ __init__.py
│  │  ├─ pipeline.py
│  │  └─ move_file.py
│  ├─ module1/            # Flytter filene fra input/ til storage/raw_data/
│  │  ├─ __init__.py
│  │  ├─ pipeline.py
│  │  └─ move_file.py
│  ├─ module2             # Kopierer gyldige filer fra storage/raw_data/ til storage/filtered_data/
│  │  ├─ __init__.py
│  │  ├─ pipeline.py
│  │  └─ copy_file.py
│  ├─ module3             # Nytt navn til filene fra storage/filtered_data/ og plassert i storage/processed_data/
│  │  ├─ __init__.py
│  │  ├─ pipeline.py
│  │  └─ rename_file.py
│  └─ module4/            # Flytter filene fra storage/processed_data/ til output/
│     ├─ __init__.py
│     ├─ pipeline.py
│     └─ move_file.py
├─ storage/               # Lagringssone for data
│  ├─ raw_data/
│  ├─ filtered_data/
│  └─ processed_data/
├─ tests/                 # Tester til system
│  └─ test_pipeline.py
├─ templates/             # Interface til nettsiden
│  └─ index.html
├─ main_pipeline.py       # Pipelineprogrammet
├─ app_pipeline.py        # Hovedprogrammet som starter server og interface
├─ README.md
└─ requirements.txt
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)
