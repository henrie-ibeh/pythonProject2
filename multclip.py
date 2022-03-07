"""
import os
import re

path = "C:/Users/pc/Downloads/Compressed/HI_candidates/NitarandaAlexander__CV.docx"
print(os.listdir(path))


def pathOpener(filePath):
    for x in os.listdir(filePath):
        try:
            opener = open(filePath + x)
        except PermissionError:
            continue
        print(opener)
        return opener


pathOpener(path)
"""

with open("C:/Users/pc/Downloads/Compressed/HI_candidates/NitarandaAlexander__CV.docx") as file:
    for email in file:
        str.encode(email)
        print(email.split('@'))
