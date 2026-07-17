from rest_framework import serializers


class PDFStatusSerializer(serializers.Serializer):

    status = serializers.CharField()

    download_url = serializers.CharField(
        required=False,
    )