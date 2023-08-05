import subprocess
import os

"""
Spusť tento skript pro kontrolu svého řešení
"""

SCRIPT_PATH = os.path.join(os.getcwd(), "argv_priklad.py")

process = subprocess.run([SCRIPT_PATH,
                          ".", "2023", "8", '4', "neco.txt",
                          "-t", "22", "22", "0", "ahoj.docx", "bruh.exe"], capture_output=True)
assert process.stdout.decode() == "04.08.2023 22.22.00\nneco.txt\nahoj.docx\nbruh.exe\n", \
    "Neshoduje se výstup"
assert process.stderr == b'', "Neprázdný stderr"

process = subprocess.run([SCRIPT_PATH,
                          ".", "2023", "8"], capture_output=True)
assert process.stderr != b'', "Prázdný stderr, měl by obsahovat chybové hlášení"
assert process.returncode != 0, "Nulový návratový kód, měl by být nenulový"

process = subprocess.run([SCRIPT_PATH,
                          ".", "2023", "8", "99"], capture_output=True)
assert process.stderr != b'', "Prázdný stderr, měl by obsahovat chybové hlášení"
assert process.returncode != 0, "Nulový návratový kód, měl by být nenulový"

process = subprocess.run([SCRIPT_PATH,
                          ".", "2023", "8", "7", "-t", "10", "12"], capture_output=True)
assert process.stderr != b'', "Prázdný stderr, měl by obsahovat chybové hlášení"
assert process.returncode != 0, "Nulový návratový kód, měl by být nenulový"

process = subprocess.run([SCRIPT_PATH,
                          ".", "2023", "8", "7", "-t", "10", "12", "420"], capture_output=True)
assert process.stderr != b'', "Prázdný stderr, měl by obsahovat chybové hlášení"
assert process.returncode != 0, "Nulový návratový kód, měl by být nenulový"

