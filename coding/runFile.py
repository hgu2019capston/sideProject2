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
        result = "now preparing..."
    else:
        result = "now preparing..."

    return result



