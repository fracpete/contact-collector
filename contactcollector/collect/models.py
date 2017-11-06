from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Employer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=250)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.name) + " - " + str(self.address)

class Employee(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name)

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    technical_skills = models.TextField(blank=True)  # comma-separated list
    responsibilities = models.TextField(blank=True)  # comma-separated list
    deliverables = models.TextField(blank=True)
    description = models.TextField()
    full_time = models.BooleanField()
    categories = models.TextField()  # comma-separated list

    def __str__(self):
        return self.title

