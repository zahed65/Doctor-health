from modeltranslation.translator import register, TranslationOptions
from .models import Service, Article, DoctorInfo

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'short_desc',)

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(DoctorInfo)
class DoctorInfoTranslationOptions(TranslationOptions):
    fields = ('name','speciality','bio','address','working_hours',)
