from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from django.contrib.auth.models import User, Group
from .forms import PartnerStaffForm
from .models import (
    PartnerTag,
    ResourceTag,
    PartnerProfile,
    PartnerStaff,
    Resource,
)

# Registering PartnerTagAdmin to customize display in the admin panel
class PartnerTagAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(PartnerTag, PartnerTagAdmin)

# Registering ResourceTagAdmin to customize display in the admin panel
class ResourceTagAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(ResourceTag, ResourceTagAdmin)

# Customizing PartnerStaffAdmin to control access and actions related to partner staff members
class PartnerStaffAdmin(admin.ModelAdmin):
    list_display = ("user", "partner", "role")

    # Override get_form method to use custom form for non-superusers
    def get_form(self, request: HttpRequest, obj: Any = None, **kwargs: Any) -> Any:
        if not request.user.is_superuser and obj is None:
            kwargs["form"] = PartnerStaffForm
        return super().get_form(request, obj, **kwargs)

    # Exclude certain fields based on user permissions
    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        else:
            return ("partner", "user")

    # Control read-only fields based on user permissions
    def get_readonly_fields(self, request: HttpRequest, obj):
        if request.user.is_superuser:
            return super().get_readonly_fields(request, obj)
        else:
            if obj and obj.user and obj.user == request.user:
                return ["role"]
            else:
                return super().get_readonly_fields(request, obj)

    # Control delete permissions based on user permissions
    def has_delete_permission(self, request: HttpRequest, obj=None):
        if request.user.is_superuser:
            return True
        else:
            if obj and obj.user and obj.user == request.user:
                return False
            else:
                return True

    # Override delete_model method to handle non-superuser deletion
    def delete_model(self, request: HttpRequest, obj: Any) -> None:
        if request.user.is_superuser:
            return super().delete_model(request, obj)
        else:
            obj.user.delete()

    # Override save_model method to handle user creation and group assignment
    def save_model(self, request, obj, form, change):
        if "username" in form.cleaned_data:
            partner_staffs = PartnerStaff.objects.filter(user=request.user).first()
            obj.partner_id = partner_staffs.partner.id
            current_user = User.objects.filter(
                username__iexact=form.cleaned_data["username"],
                email__iexact=form.cleaned_data["email"],
            ).first()
            obj.user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
                is_staff=True,
            )
            if form.cleaned_data["role"] == "manager":
                group = Group.objects.get(name="Partner Staff - Manager")
            else:
                group = Group.objects.get(name="Partner Staff - Editor")
            obj.user.groups.add(group)
            obj.save()
        else:
            super().save_model(request, obj, form, change)

    # Limit queryset based on user permissions
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            partner_staffs = PartnerStaff.objects.filter(user=request.user).first()
            if partner_staffs is None:
                return qs.none()
            qs = qs.filter(partner=partner_staffs.partner)
        return qs

admin.site.register(PartnerStaff, PartnerStaffAdmin)

# Customizing PartnerProfileAdmin to control access and actions related to partner profiles
class PartnerProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "tag_list")

    # Limit queryset based on user permissions
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            partner_staffs = PartnerStaff.objects.filter(user=request.user).first()
            if partner_staffs is None:
                return qs.none()
            qs = qs.filter(id=partner_staffs.partner.id)
        return qs

    # Custom method to display tag list in admin panel
    def tag_list(self, obj):
        return ", \n ".join([p.name for p in obj.tags.all()])

    # Control read-only fields based on user permissions
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ["status"]
        else:
            return []

admin.site.register(PartnerProfile, PartnerProfileAdmin)

# Customizing ResourceAdmin to control access and actions related to resources
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("name", "tag_list", "partner")

    # Custom method to display tag list in admin panel
    def tag_list(self, obj):
        return ", \n ".join([p.name for p in obj.tags.all()])

    # Exclude certain fields based on user permissions
    def get_exclude(self, request, obj):
        if not request.user.is_superuser:
            return ["partner"]
        else:
            return []

    # Override save_model method to handle partner assignment
    def save_model(self, request, obj, form, change):
        if not obj.partner_id:
            partner_staffs = PartnerStaff.objects.filter(user=request.user).first()
            if partner_staffs is None:
                return
            obj.partner_id = partner_staffs.partner.id
        obj.save()

    # Limit queryset based on user permissions
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            partner_staffs = PartnerStaff.objects.filter(user=request.user).first()
            if partner_staffs is None:
                return qs.none()
            qs = qs.filter(partner=partner_staffs.partner)

        return qs

admin.site.register(Resource, ResourceAdmin)
