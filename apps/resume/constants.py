from apps.resume.models import SocialPlatform

SOCIAL_DOMAINS = {

    SocialPlatform.GITHUB: "github.com",

    SocialPlatform.LINKEDIN: "linkedin.com",

    SocialPlatform.TWITTER: "twitter.com",

    SocialPlatform.INSTAGRAM: "instagram.com",

    SocialPlatform.TELEGRAM: "t.me",

    SocialPlatform.FACEBOOK: "facebook.com",

    SocialPlatform.YOUTUBE: "youtube.com",

}

class Messages:
    SUCCESS = "Success"
    CREATED = "Created successfully."
    UPDATED = "Updated successfully."
    DELETED = "Deleted successfully."

MAX_IMAGE_SIZE = 5 * 1024 * 1024

# MAX_SKILLS

# MAX_SOCIAL_LINKS

# MAX_PROJECTS