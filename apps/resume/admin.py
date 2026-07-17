
from django.contrib import admin
from .models import Resume, Project, Skill, SkillCategory

# ثبت دسته‌بندی مهارت‌ها
@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

# ثبت مهارت‌ها
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name']

# ثبت رزومه
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_info', 'experience', 'education', 'profile_picture', 'youtube_url', 'linkedin_url', 'instagram_url', 'telegram_url', 'facebook_url', 'twitter_url', 'background_image']
    fields = ['name', 'contact_info', 'experience', 'education', 'skills', 'profile_picture', 'youtube_url', 'linkedin_url', 'instagram_url', 'telegram_url', 'facebook_url', 'twitter_url', 'background_image']
    filter_horizontal = ['skills'] # نمایش انتخاب چندتایی مهارت‌ها
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name']

admin.site.register(Project)
