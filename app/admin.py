from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import ImageModel
from .models import QuestionModel
from .models import GroupQuestionsModel
from .models import ResultModel
from .models import TestModel
from .models import QuestionInTestModel
from .models import GroupInTestModel

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser


admin.site.register(MyUser, UserAdmin)

@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(GroupQuestionsModel)
class GroupQuestionsAdmin(admin.ModelAdmin):
    pass

@admin.register(ResultModel)
class ResultAdmin(admin.ModelAdmin):
    pass

@admin.register(TestModel)
class TesttAdmin(admin.ModelAdmin):
    pass

@admin.register(QuestionInTestModel)
class QuestionInTestAdmin(admin.ModelAdmin):
    pass

@admin.register(GroupInTestModel)
class GroupInTestModelAdmin(admin.ModelAdmin):
    pass
