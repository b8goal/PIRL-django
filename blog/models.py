from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class M1_Train_data(models.Model):
    bmi = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=30)
    triglycerides = models.FloatField(null=True, blank=True)
    hdl = models.FloatField(null=True, blank=True)  # min: 1, max: 97, mean: 56.790048
    ldl = models.FloatField(null=True, blank=True)  # min: -12.2, max: 204.0, mean: 113.38690240000004
    sex = models.PositiveSmallIntegerField(null=True, blank=True)  # min: 1, max: 2, mean: 1.499904
    waist = models.FloatField(null=True, blank=True)  # min: 48, max: 166, mean: 79.958884
    systolic_pressure = models.FloatField(null=True, blank=True)  # min: 70, max: 236, mean: 121.438776
    diastolic_pressure = models.FloatField(null=True, blank=True)  # min: 39, max: 151, mean: 75.451088
    fbs = models.FloatField(null=True, blank=True)  # min: 18, max: 685, mean: 98.937808
    old = models.PositiveSmallIntegerField(null=True, blank=True)  # min: 5, max: 18, mean: 10.421392
    smoke = models.PositiveSmallIntegerField(null=True, blank=True)  # min: 1, max: 3, mean: 1.57258
    alcohol_hepatitis = models.PositiveSmallIntegerField(null=True, blank=True)  # min: 0, max: 1, mean: 0.041848

    def __str__(self):
        return self.location
