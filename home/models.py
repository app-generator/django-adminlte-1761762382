# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Loadbalancer(models.Model):

    #__Loadbalancer_FIELDS__
    datacenter = models.TextField(max_length=255, null=True, blank=True)
    lb_name = models.TextField(max_length=255, null=True, blank=True)
    lb_ip = models.TextField(max_length=255, null=True, blank=True)

    #__Loadbalancer_FIELDS__END

    class Meta:
        verbose_name        = _("Loadbalancer")
        verbose_name_plural = _("Loadbalancer")


class Vs(models.Model):

    #__Vs_FIELDS__
    location = models.TextField(max_length=255, null=True, blank=True)
    lb_ip = models.TextField(max_length=255, null=True, blank=True)
    lb_name = models.CharField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    dest_address = models.TextField(max_length=255, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)
    partition = models.TextField(max_length=255, null=True, blank=True)
    vs_full_path = models.TextField(max_length=255, null=True, blank=True)
    vs_description = models.TextField(max_length=255, null=True, blank=True)
    ssl = models.TextField(max_length=255, null=True, blank=True)
    ssl-client = models.TextField(max_length=255, null=True, blank=True)
    ssl-server = models.TextField(max_length=255, null=True, blank=True)
    pool_name = models.TextField(max_length=255, null=True, blank=True)
    pool_members = models.TextField(max_length=255, null=True, blank=True)
    members_name = models.TextField(max_length=255, null=True, blank=True)
    pool_description = models.TextField(max_length=255, null=True, blank=True)
    vlan = models.TextField(max_length=255, null=True, blank=True)
    self_ip = models.TextField(max_length=255, null=True, blank=True)
    floating_ip = models.TextField(max_length=255, null=True, blank=True)
    rules = models.TextField(max_length=255, null=True, blank=True)

    #__Vs_FIELDS__END

    class Meta:
        verbose_name        = _("Vs")
        verbose_name_plural = _("Vs")



#__MODELS__END
