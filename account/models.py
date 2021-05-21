from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Store


class User(AbstractUser):
    is_owner = models.BooleanField(default=False)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, related_name='employees')


@receiver(post_save, sender=User)
def create_or_update_user(sender, instance, created, **kwargs):
    if instance.is_owner:
        if created:
            Owner.objects.create(user=instance)
            Store.objects.create(owner=instance.owner)
        else:
            instance.owner.save()
    else:
        if created:
            Employee.objects.create(user=instance)
        else:
            instance.employee.save()
