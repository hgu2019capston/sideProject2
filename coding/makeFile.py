from .models import Coding
from  django.http import HttpResponse


def file(languages):
    code = Coding.objects.last().content

    if languages == 1:
        f=open("coding/content.py","w")
        f.write("%s" % code)
        f.close()
        
    elif languages == 2:
        f=open("coding/content.c","w")
        f.write("%s" % code)
        f.close()
                   
    elif languages == 3:
        f=open("coding/content.java","w")
        f.write("%s" % code)
        f.close()
          
    else:
        f=open("coding/content.cpp","w")
        f.write("%s" % code)
        f.close()
        
