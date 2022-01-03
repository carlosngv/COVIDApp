from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='reports', null=True, blank=True)
    image_str = models.TextField(blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class CSV(models.Model):
    file_name = models.FileField(upload_to='cvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)
