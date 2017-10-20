import mistune

from django import template

register = template.Library()


@register.filter(name='markdown')
def convert_from_markdown(text):
    md = mistune.Markdown()
    return md(text)


@register.filter(name='iterable_from_difference')
def iterable_from_difference(x, subtract_from):
    return range(subtract_from-x)


@register.filter(name='solved_tasks_for_course')
def solved_tasks_for_course(student, course):
    solved = student.solutions.get_solved_solutions_for_student_and_course(student=student, course=course)

    return solved.count()


@register.filter(name='get_date_for_weekday')
def get_date_for_weekday(dates, weekday):
    date = dates.get(weekday)

    if date:
        return date.get('lecture_date')

    return 'No Lecture'


@register.filter(name='get_lecture_id_for_weekday')
def get_lecture_id_for_weekday(dates, weekday):
    date = dates.get(weekday)

    if date:
        return date.get('lecture_id', None)

    return None


@register.filter(name='get_courses_containing_task')
def get_courses_containing_task(task):
    included_tasks = task.included_tasks.all()
    return set(task.topic.course.name for task in included_tasks)


@register.filter(name='get_courses_containing_material')
def get_courses_containing_material(material):
    included_materials = material.included_materials.all()
    return set(material.topic.course.name for material in included_materials)
