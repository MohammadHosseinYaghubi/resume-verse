def resume_key(slug):
    return f"resume:{slug}"


def project_key(slug):
    return f"project:{slug}"


def skill_list_key():
    return "skills:list"


def category_list_key():
    return "categories:list"


def social_list_key(resume_id):
    return f"socials:{resume_id}"