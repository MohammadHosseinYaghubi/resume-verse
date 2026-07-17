from urllib.parse import urlparse
from rest_framework import serializers
from apps.resume.constants import SOCIAL_DOMAINS, MAX_IMAGE_SIZE

def validate_name(value):
    value = value.strip()

    if not value:
        raise serializers.ValidationError(
            "This field cannot be empty."
        )

    return value
        
def validate_slug(value):
    value = value.strip()

    if not value:
        raise serializers.ValidationError(
            "This field cannot be empty."
        )
    
    if " " in value:
        raise serializers.ValidationError(
            "Slug cannot contain spaces."
        )
        
    return value
    

def validate_social_url(platform, url):

    domain = urlparse(url).netloc.lower()
    expected_domain = SOCIAL_DOMAINS.get(platform)

    if expected_domain:
        if expected_domain not in domain:
            raise serializers.ValidationError(
                f"This is not a valid {platform} url."
            )

    return url
 
    
def validate_project_url(self, value):

    if value and not value.startswith("https://"):

        raise serializers.ValidationError(

            "Project URL must start with https://"

        )

    return value

def validate_image(self, image):

    if image.size > MAX_IMAGE_SIZE:

        raise serializers.ValidationError(

            "Image is too large."

        )

    return image