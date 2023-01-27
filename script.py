import os
import re

def replace_polish_chars(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # replace ą with a
    text = re.sub(r'ą', 'a', text)
    # replace ę with e
    text = re.sub(r'ę', 'e', text)
    # replace ś with s
    text = re.sub(r'ś', 's', text)
    # replace ł with l
    text = re.sub(r'ł', 'l', text)
    # replace ż with z
    text = re.sub(r'ż', 'z', text)
    # replace ź with z
    text = re.sub(r'ź', 'z', text)
    # replace ć with c
    text = re.sub(r'ć', 'c', text)
    # replace ń with n
    text = re.sub(r'ń', 'n', text)
    # replace ó with o
    text = re.sub(r'ó', 'o', text)
    # replace ż with z
    text = re.sub(r'ż', 'z', text)
    # replace ź with z
    text = re.sub(r'ź', 'z', text)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)





os.chdir(os.getcwd()+'/baza')
for file in os.listdir():
    replace_polish_chars(file)