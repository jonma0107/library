from django.db import models

# Create your models here.
class Libro(models.Model):
    title=models.CharField(max_length=100, null=False)
    image=models.ImageField(upload_to='img/', null=False)
    description=models.TextField(null=False)    

    def __str__(self):
        return (self.title)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()    

