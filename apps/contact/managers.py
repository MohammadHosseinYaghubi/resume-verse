from django.db import models

from .constants import ContactStatus


class ContactQuerySet(
    models.QuerySet,
):

    def new(self):

        return self.filter(
            status=ContactStatus.NEW,
        )

    def read(self):

        return self.filter(
            status=ContactStatus.READ,
        )

    def answered(self):

        return self.filter(
            status=ContactStatus.ANSWERED,
        )

    def closed(self):

        return self.filter(
            status=ContactStatus.CLOSED,
        )


class ContactManager(
    models.Manager,
):

    def get_queryset(self):

        return ContactQuerySet(
            self.model,
            using=self._db,
        )

    def new(self):

        return self.get_queryset().new()

    def read(self):

        return self.get_queryset().read()

    def answered(self):

        return self.get_queryset().answered()

    def closed(self):

        return self.get_queryset().closed()