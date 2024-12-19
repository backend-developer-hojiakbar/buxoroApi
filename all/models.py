from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(models.Model):
    telegram_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    fio = models.CharField(max_length=255)
    car_model = models.CharField(max_length=100)
    car_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fio} - {self.phone_number}"


class DriverRequest(models.Model):
    user_id = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=255, blank=True, null=True)
    telegram_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user_id} - {self.phone_number}"


class Reklama(models.Model):
    telegram_id = models.IntegerField()
    odamOrPochta = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    passenger_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_location} dan {self.to_location} - {self.passenger_count}"