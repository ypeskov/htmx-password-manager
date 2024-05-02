from django.db import models


class CreditCard(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    holder_name = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=16, null=True, blank=True)
    expiration_month = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    expiration_year = models.IntegerField()
    cvv = models.CharField(max_length=3, null=True, blank=True)
    pin = models.CharField(max_length=10, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        last_four = self.number[-4:]
        return f'{self.title} - {self.holder_name} - {self.brand} - {last_four}'
