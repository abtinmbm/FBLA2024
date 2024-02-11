from partners.models import PartnerTag, Resource, ResourceTag

# Function to fetch public resources along with partner information
def get_public_resources():
    resources = []  # List to store public resources
    # Iterate through active resources
    for resource in Resource.objects.filter(partner__status="active").all():
        # Construct resource dictionary with relevant information
        resources.append(
            {
                "id": resource.id,
                "name": resource.name,
                "description": resource.description,
                "tags": list(resource.tags.all().values()),  # Convert tags to list of dictionaries
                "partner": {
                    "name": resource.partner.name,
                    "description": resource.partner.description,
                    "logo": (
                        resource.partner.logo.url if resource.partner.logo else None
                    ),  # Add logo URL if exists, otherwise None
                    "website": resource.partner.website,
                    "contact_email": resource.partner.contact_email,
                    "contact_phone": resource.partner.contact_phone,
                    "tags": list(resource.partner.tags.all().values()),  # Convert partner tags to list of dictionaries
                },
            }
        )
    return resources  # Return list of public resources with partner information
