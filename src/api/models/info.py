from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=2)
    date_of_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=2)
    date_of_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    shortname = models.CharField(max_length=20)
    fullname = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    date_of_created = models.DateTimeField(auto_now_add=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.shortname


class Region(models.Model):
    shortname = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    date_of_created = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.shortname


class District(models.Model):
    shortname = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    date_of_created = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.shortname
