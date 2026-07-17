from django.db import models
from .models import ProjectStatus

class ResumeQuerySet(models.QuerySet):

    def public(self):
        return self.filter(
            is_public=True,
        )

    def with_skills(self):
        return self.prefetch_related(
            "skills",
            "skills__category",
        )

    def with_projects(self):
        return self.prefetch_related(
            "projects",
            "projects__technologies",
        )

    def with_social_links(self):
        return self.prefetch_related(
            "social_links",
        )


class ResumeManager(models.Manager):

    def get_queryset(self):
        return ResumeQuerySet(
            self.model,
            using=self._db,
        )

    def public(self):
        return self.get_queryset().public()

    def detail(self):
        return (
            self.get_queryset()
            .public()
            .with_skills()
            .with_projects()
            .with_social_links()
        )
    
    def active(self):
        return self.public()
    
# ----------------------------

class ProjectQuerySet(models.QuerySet):

    def published(self):
        return self.filter(
            status=ProjectStatus.PUBLISHED,
        )

    def with_resume(self):
        return self.select_related(
            "resume",
        )

    def with_technologies(self):
        return self.prefetch_related(
            "technologies",
            "technologies__category",
        )

    def detail(self):
        return (
            self.with_resume()
            .with_technologies()
        )


class ProjectManager(models.Manager):

    def get_queryset(self):
        return ProjectQuerySet(
            self.model,
            using=self._db,
        )

    def published(self):
        return (
            self.get_queryset()
            .published()
        )

    def detail(self):
        return (
            self.get_queryset()
            .published()
            .detail()
        )