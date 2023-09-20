from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        if (len(list(filter(lambda i: len(i.cleaned_data) > 0, self.forms))) == 0): raise ValidationError("Необходимо добавить хотя бы один тег")
        isMainCount = 0
        for form in self.forms:
            if (form.cleaned_data.get("is_main") == True): isMainCount += 1
        if (isMainCount > 1): raise ValidationError("Главный тег может быть только один")
        if (isMainCount < 1): raise ValidationError("Необходимо назначить главный тег")
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
