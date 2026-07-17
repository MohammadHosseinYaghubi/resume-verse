from rest_framework.routers import (
    SimpleRouter,
)

from .views import (
    ContactViewSet,
)


router = SimpleRouter()

router.register(

    "contacts",

    ContactViewSet,

    basename="contact",

)