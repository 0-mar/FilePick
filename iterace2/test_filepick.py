from typing import Set

import filepick
import sys
import os
import shutil

"""
Spusť tenhle skript pro kontrolu řešení.
"""

TARGET_DIR = "target"


def make_dirtree():
    os.makedirs(os.path.join("test", "1", "2"))
    os.makedirs(os.path.join("test", "1", "3"))
    os.makedirs(os.path.join("test", "4"))

    with open(os.path.join("test", "1", "a.txt"), "w"):
        pass
    with open(os.path.join("test", "1", "b.png"), "w"):
        pass
    with open(os.path.join("test", "1", "c.docx"), "w"):
        pass
    with open(os.path.join("test", "1", "2", "yeehaw.txt"), "w"):
        pass
    with open(os.path.join("test", "1", "3", "42.txt"), "w"):
        pass
    with open(os.path.join("test", "4", "d.txt"), "w"):
        pass
    with open(os.path.join("test", "4", "e.wtf"), "w"):
        pass


def test_filepick(source: str, correct_files: Set[str]) -> None:
    os.makedirs(TARGET_DIR)
    sys.argv[1] = source
    sys.argv[2] = TARGET_DIR
    filepick.filepick()

    assert set(os.listdir(TARGET_DIR)) == correct_files, \
        f"Neshodují se zkopírované soubory - zkopírovalo se jenom {set(os.listdir(TARGET_DIR))}, správně" \
        f"by se mělo zkopírovat {correct_files}"

    shutil.rmtree(TARGET_DIR)


def test():
    sys.argv = []
    sys.argv.append("filepick.py")
    sys.argv.append("filepick.py")
    sys.argv.append("filepick.py")
    make_dirtree()

    test_filepick(os.path.join("test", "1"), {'a.txt', 'c.docx', 'yeehaw.txt', '42.txt'})
    test_filepick(os.path.join("test", "1", "2"), {'yeehaw.txt'})
    test_filepick(os.path.join("test", "1", "3"), {'42.txt'})
    test_filepick(os.path.join("test", "4"), {'d.txt'})
    test_filepick(os.path.join("test"), {'a.txt', 'c.docx', 'yeehaw.txt', '42.txt', 'd.txt'})

    shutil.rmtree("test")


if __name__ == '__main__':
    test()