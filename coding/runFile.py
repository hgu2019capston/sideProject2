import os
import subprocess
import crypt


def runfile():

   result = subprocess.check_output(["python", "coding/content.py"])
   return result



   '''myCmd = 'python content.py > out.txt'

    os.system(myCmd)'''
