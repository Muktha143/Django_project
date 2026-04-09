import random
import string

from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Pincode(models.Model):
    code = models.CharField(max_length=6)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.city}"

class UserData(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    aadhaar_number = models.CharField(max_length=12, unique=True, blank=True, null=True)
    pan_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    dob = models.DateField()
    father_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    pincode = models.ForeignKey(Pincode, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Data'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.aadhaar_number:
            self.aadhaar_number = self._generate_unique_aadhaar()
        if not self.pan_number:
            self.pan_number = self._generate_unique_pan()
        super().save(*args, **kwargs)

    @classmethod
    def _generate_unique_aadhaar(cls):
        while True:
            aadhaar = ''.join(random.choices(string.digits, k=12))
            if not cls.objects.filter(aadhaar_number=aadhaar).exists():
                return aadhaar

    @classmethod
    def _generate_unique_pan(cls):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=5))
            digits = ''.join(random.choices(string.digits, k=4))
            suffix = random.choice(string.ascii_uppercase)
            pan = f"{letters}{digits}{suffix}"
            if not cls.objects.filter(pan_number=pan).exists():
                return pan

    def __str__(self):
        return self.full_name