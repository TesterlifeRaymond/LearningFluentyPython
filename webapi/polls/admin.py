# -*- coding: utf-8 -*-
"""
    webapi.admin
    ~~~~~~~~~~~~

    DESCRIPTION

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-09-10 12:11:22
"""

from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


# Register your models here.
