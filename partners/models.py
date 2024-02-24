from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field

# Model for Partner Tags
class PartnerTag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Partner Tag"
        verbose_name_plural = "Partner Tags"

# Model for Resource Tags
class ResourceTag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Resource Tag"
        verbose_name_plural = "Resource Tags"

# Model for Partner Profile
class PartnerProfile(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255,
        choices={
            ("pending", "Pending"),
            ("active", "Active"),
            ("suspended", "Suspended"),
        },
        default="pending",
    )
    description = models.TextField(max_length=300)
    website = models.URLField()
    logo = models.ImageField(blank=True, null=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=255)
    tags = models.ManyToManyField(PartnerTag)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Partner Profile"
        verbose_name_plural = "Partner Profiles"

# Model for Partner Staff
class PartnerStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    partner = models.ForeignKey(PartnerProfile, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=255,
        choices={
            ("editor", "Editor"),
            ("manager", "Manager"),
        },
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Partner Staff"
        verbose_name_plural = "Partner Staffs"

# Model for Resource
class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = CKEditor5Field(max_length=1000)
    tags = models.ManyToManyField(ResourceTag)
    partner = models.ForeignKey(PartnerProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"
