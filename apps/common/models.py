from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, 
                          default=uuid.uuid4,
                          editable=False,
                        )
    class Meta:
        abstract = True


class TimeStampedModel(BaseModel):
    """
    Abstract base model that provides self-updating
    created_at and updated_at fields.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True