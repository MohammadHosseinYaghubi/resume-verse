from apps.resume.selectors import resume_queryset


def build_resume_context(*, resume):

    resume = (
        resume_queryset()
        .filter(
            id=resume.id,
        )
        .prefetch_related(
            "skills__category",
            "projects__technologies",
            "social_links",
        )
        .get()
    )

    return {
        "resume": resume,
    }