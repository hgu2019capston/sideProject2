from .models import Coding

def file():
    f= open("coding/content.py","w")
    coding=Coding.objects.get(content='print("hello~")')
    f.write("%s" % coding)
    f.close()
    #Open the file back and read the contents
    #f=open("guru99.txt", "r")
    #if f.mode == 'r':
    #   contents =f.read()
    #    print (contents)
    #or, readlines reads the individual line into a list
    #fl =f.readlines()
    #for x in fl:
    #print(x)

