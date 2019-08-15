from django.db import models

# Create your models here.

DEVICE_STATUS = (
    (0, '关'),
    (1, '开'),
)

class Device(models.Model):
    device_name = models.CharField(verbose_name='设备名称', max_length=30, null=True, blank=True)
    device_status = models.IntegerField(verbose_name='设备状态', choices=DEVICE_STATUS, default=0)

    def __str__(self):
        return self.device_name
