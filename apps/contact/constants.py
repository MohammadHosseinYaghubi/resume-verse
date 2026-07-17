from django.db import models


class ContactStatus(models.TextChoices):

    NEW = "new", "New"

    READ = "read", "Read"

    ANSWERED = "answered", "Answered"

    CLOSED = "closed", "Closed"