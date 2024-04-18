from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    
    def clean(self):
        super().clean()
        count_true_tags = list(filter(lambda form: form.cleaned_data['is_main'], self.forms))
        if len(count_true_tags) == 0:
            raise ValidationError('Укажите основной раздел')
        if len(count_true_tags) > 1:
            raise ValidationError('Основным может быть только один раздел')
        
         


class ScopeInline(admin.TabularInline):
    
    model = Scope
    formset = ScopeInlineFormset



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'name'] 