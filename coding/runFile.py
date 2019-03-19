import os
import subprocess
import crypt


def runfile(languages):

    if languages == 1:
        result =  subprocess.check_output(["python", "coding/content.py"])
    elif languages == 2:
        subprocess.call(["gcc", "coding/content.c", "-o", "content"])
        result = subprocess.check_output(["./content"])
    elif languages == 3:
        subprocess.call(["javac", "-d", ".", "coding/content.java"])
        result = subprocess.check_output(["java", "-cp", ".", "content"])
    else:
        subprocess.call(["g++", "coding/content.cpp", "-o", "content2"])
        result = subprocess.check_output(["./content2"])

    return result



