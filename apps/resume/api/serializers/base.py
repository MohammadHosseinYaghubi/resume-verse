from rest_framework import serializers


class BaseReadSerializer(serializers.ModelSerializer):
    """
    Base serializer for read operations.
    """

    class Meta:
        abstract = True


class BaseWriteSerializer(serializers.ModelSerializer):
    """
    Base serializer for write operations.
    """

    class Meta:
        abstract = True