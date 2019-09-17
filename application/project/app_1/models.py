from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=False)
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=False)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
