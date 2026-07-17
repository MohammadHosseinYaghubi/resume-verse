from django.shortcuts import render
from ..models import Resume, Project, SkillCategory

def resume_view(request):
    resume = Resume.objects.first()  # Get your resume data
    projects = Project.objects.all() # Get all project data
    skill_categories = SkillCategory.objects.all()
    # هر دسته و مهارت‌های مرتبط با رزومه
    categorized_skills = []
    if resume:
        for category in skill_categories:
            skills = resume.skills.filter(category=category)
            if skills.exists():
                categorized_skills.append({
                    'category': category.name,
                    'skills': skills
                })
    return render(request, 'resume.html', {
        'resume': resume,
        'projects': projects,
        'categorized_skills': categorized_skills
    })
