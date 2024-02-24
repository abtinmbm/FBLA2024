import json
from django.shortcuts import render, redirect
from .models import PartnerProfile, PartnerStaff, PartnerTag, Resource, ResourceTag
from .forms import PartnerForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.shortcuts import render
from django.db import IntegrityError, transaction
from django.http import HttpResponseRedirect, JsonResponse
from .models import PartnerProfile
from .functions import get_public_resources
import re

# View to render partner list page
def partner_list(request):
    # Fetch public resources
    resources = get_public_resources()
    # Fetch all partner tags and resource tags
    partner_tags = PartnerTag.objects.all()
    resource_tags = ResourceTag.objects.all()
    # Render the partner list template with resources and tags
    return render(
        request,
        "partner_list.html",
        {
            "resources": resources,
            "resources_json": json.dumps(resources),  # Convert resources to JSON
            "partner_tags": partner_tags,
            "resource_tags": resource_tags,
        },
    )

# View to return partner list data in JSON format to be used for filtering and searching
def partner_list_json(request):
    # Fetch public resources
    resources = get_public_resources()
    # Return JSON response with resources data
    return JsonResponse({"data": resources})

# View to handle partner proposal form submission
def partner_proposal(request):
    if request.method == "POST":
        form = PartnerForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if username or email already exists
            if User.objects.filter(username__iexact=form.cleaned_data["username"]).exists():
                form.add_error("username", "Username already exists")
                return render(request, "partner_proposal.html", {"form": form})
            if User.objects.filter(email__iexact=form.cleaned_data["email"]).exists():
                form.add_error("email", "Email already exists")
                return render(request, "partner_proposal.html", {"form": form})
             # Validate phone number format
            phone_number = form.cleaned_data["contact_phone"]
            if not re.match(r'^\(\d{3}\) \d{3}-\d{4}$', phone_number):
                form.add_error("contact_phone", "Invalid phone number, please use the format (123) 456-7890")
                return render(request, "partner_proposal.html", {"form": form})
            
            try:
                # Create partner profile and associated user
                with transaction.atomic():
                    profile = PartnerProfile.objects.create(
                        name=form.cleaned_data["name"],
                        description=form.cleaned_data["description"],
                        logo=form.cleaned_data["logo"],
                        website=form.cleaned_data["website"],
                        contact_email=form.cleaned_data["contact_email"],
                        contact_phone=phone_number,
                    )
                    user = User.objects.create_user(
                        username=form.cleaned_data["username"],
                        email=form.cleaned_data["email"],
                        password=form.cleaned_data["password"],
                        is_staff=True,
                    )
                    profile.tags.set(form.cleaned_data["tags"])  # Associate tags with profile
                    user.groups.add(Group.objects.get(id=1))  # Add user to default group
                    # Create partner staff record
                    PartnerStaff.objects.create(user=user, partner=profile, role="manager")
                    login(request, user)  # Log in the user
                    return HttpResponseRedirect("/admin")  # Redirect to admin page after successful creation
            except IntegrityError:
                form.add_error(
                    None, "Something went wrong. Please try again or contact support."
                )
                return render(request, "partner_proposal.html", {"form": form})

    # If it's a GET request, render blank partner proposal form
    else:
        form = PartnerForm()

    return render(request, "partner_proposal.html", {"form": form})
def partner_terms(request):
    return render(request, "partner_terms.html")