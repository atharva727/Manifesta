from datetime import datetime
from django.db import models
from django.conf import settings


def get_profile_pic_path(self, filename):
    return f"Customer/profile_images/{self.id}/{filename}"


def get_default_profile_pic_path():
    return "Customer/profile_images/default_profile_pic.jpg"


def get_vendor_profile_pic_path(self, filename):
    return f"Vendor/profile_images/{self.id}/{filename}"


# Create your models here.
class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, default="")
    last_name = models.CharField(max_length=100, null=True, default="")
    contact = models.CharField(max_length=10, null=True, default="")
    profile_image = models.ImageField(upload_to=get_profile_pic_path, default=get_default_profile_pic_path, )

    def __str__(self):
        return str(self.id) + "  " + self.first_name + ' ' + self.last_name


class Categories(models.Model):
    name = models.CharField(max_length=50, default="None")

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length=50, default="None")

    def __str__(self):
        return self.name


class VendorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    contact = models.CharField(max_length=10, null=True, default="")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    events = models.ManyToManyField(Events)
    description = models.CharField(max_length=2000, null=True, default='')
    profile_image = models.ImageField(upload_to=get_vendor_profile_pic_path, default=get_default_profile_pic_path, )

    def __str__(self):
        return str(self.id) + "  " + self.name + " (" + str(self.category) + ")"

    def getevents(self):
        return ", ".join([a.name for a in self.events.all()])

    def sincebeen(self):
        then = self.user.date_joined
        now = datetime.now()
        dur = (now.year - then.year) * 12 + now.month - then.month
        if dur % 12 == 0:
            return f"{dur // 12} Years"
        return f"{dur // 12} Years {dur % 12} Months"


class Order(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    price = models.IntegerField()
    orderPlacedTime = models.DateTimeField(default=datetime.today())
    orderDeliveryTime = models.DateTimeField()
    message = models.CharField(max_length=2000)
    address = models.CharField(max_length=2000)
    pin_code = models.CharField(max_length=6)

