from django.db import models

class Coding(models.Model):
    TYPE_LANGUAGES = (
            (1, ('python')),
            (2, ('C')),
            (3, ('Java')),
            (4, ('C++')),
            )

    languages = models.IntegerField(choices=TYPE_LANGUAGES, default=1)
    content = models.CharField(max_length = 10000)


    def generate(self):
        return self.save()
    
    def __str__(self):
        return self.content
    
    def delete(self):
        Coding.objects.all().delete()
