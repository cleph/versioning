from django.db import models
from django.utils.translation import gettext_lazy as _

class Platform(models.Model):
    STATUS_CHOICES = [
        ('PreAlpha', _('PreAlpha')),
        ('Alpha', _('Alpha')),
        ('Beta', _('Beta')),
        ('Gamma', _('Gamma')),
        ('RC', _('RC')),
        ('Rolling', _('Rolling')),
        ('Stable', _('Stable')),
    ]
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    url = models.URLField(verbose_name=_("URL"))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name=_("Status"))
    version = models.CharField(max_length=255,verbose_name=_("Version"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _('Platform')
        verbose_name_plural = _('Platforms')

    def __str__(self):
        return f"{self.title} (v{self.version})"


class Patch(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name=_("Platform"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _('Patch')
        verbose_name_plural = _('Patches')

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name=_("Platform"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _('Test')
        verbose_name_plural = _('Tests')

    def __str__(self):
        return self.title


class Bug(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name=_("Platform"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _('Bug')
        verbose_name_plural = _('Bugs')

    def __str__(self):
        return self.title
