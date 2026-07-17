# from rest_framework import serializers

# from django.contrib.auth import get_user_model

# User = get_user_model()


# class ProfileReadSerializer(
#     serializers.ModelSerializer,
# ):

#     class Meta:

#         model = User

#         fields = (
#             "id",
#             "username",
#             "email",
#             "first_name",
#             "last_name",
#         )

#         read_only_fields = fields


# class ProfileWriteSerializer(
#     serializers.ModelSerializer,
# ):

#     class Meta:

#         model = User

#         fields = (
#             "first_name",
#             "last_name",
#             "email",
#         )