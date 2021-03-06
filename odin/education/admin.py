from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import (
    ProgrammingLanguage,
    Course,
    Task,
    IncludedTask,
    Week,
    Test,
    IncludedTest,
    Solution,
    CourseAssignment,
    CourseDescription,
)


class CoursesListFilter(SimpleListFilter):
    title = ('course')
    parameter_name = 'course'

    def lookups(self, request, model_admin):

        return [lookup for lookup in Course.objects.values_list('slug_url', 'name')]

    def queryset(self, request, queryset):

        if not self.value():
            return queryset.all()

        return queryset.filter(task__course__slug_url=self.value())


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug_url')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'gradable')


@admin.register(IncludedTask)
class IncludedTaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'week')
    list_select_related = ('task', 'week', 'week__course')


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'course', 'start_date', 'end_date')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'language')


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user', 'course', 'verbose_status')
    list_select_related = ('task', 'task__course', 'user')

    search_fields = ('task__name', 'user__email', 'task__course__name', )
    list_filter = ['status', CoursesListFilter]

    def course(self, obj):
        return obj.task.course


@admin.register(CourseAssignment)
class CourseAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'teacher', 'course', 'hidden')


@admin.register(CourseDescription)
class CourseDescriptionAdmin(admin.ModelAdmin):
    list_display = ('course', 'verbose')


@admin.register(IncludedTest)
class IncludedTestAdmin(admin.ModelAdmin):
    list_display = ('task', 'get_week', 'get_course')
    list_select_related = ('task', 'test', 'task__course', 'task__week')

    ordering = ('-id', )

    def get_course(self, obj):
        return obj.task.course

    def get_week(self, obj):
        return obj.task.week.number
