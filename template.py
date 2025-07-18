import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "voiceofuser"

list_of_files = [
    "main.py",
    "models.py",
    "database.py",
    "summarizer.py",
    ".env",
    "requirements.txt"
]

for file in list_of_files:
    # Join project_name to create files under "voiceofuser/"
    filepath = Path(project_name) / file

    filedir = filepath.parent

    if not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filepath.name}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            pass  # You can optionally write a template here
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} is already created")
