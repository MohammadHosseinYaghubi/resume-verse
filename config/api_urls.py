from django.urls import (
    include,
    path,
)

urlpatterns = [

    path(

        "v1/",

        include(

            (

                "config.api_v1_urls",

                "v1",

            ),

            namespace="v1",

        ),

    ),

]