from datetime import date

from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import (
    Application,
    ApplicationInfo,
)
from odin.education.models import Course
from odin.users.models import BaseUser


def validate_can_create_application_info(*, instance: ApplicationInfo):

    if instance.course.start_date < timezone.now().date():
        raise ValidationError(f"{instance.course} has already started")

    if instance.start_date >= instance.end_date:
        raise ValidationError("Start date can not be after end date")

        if instance.start_interview_date >= instance.end_interview_date:
            raise ValidationError(
                "Start interview date can not be after end interview date")


def validate_can_create_or_update_application(*, instance: Application):

    if not instance.application_info.apply_is_active():
        raise ValidationError(
            f"The application period for {instance.application_info.course} has expired!")


def create_application_info(*,
                            start_date: date,
                            end_date: date,
                            course: Course,
                            start_interview_date: date=None,
                            end_interview_date: date=None,
                            description: str=None,
                            external_application_form: str=None) -> ApplicationInfo:

    instance = ApplicationInfo(start_date=start_date,
                               end_date=end_date,
                               course=course,
                               start_interview_date=start_interview_date,
                               end_interview_date=end_interview_date,
                               description=description,
                               external_application_form=external_application_form)

    instance.full_clean()
    validate_can_create_application_info(instance=instance)
    instance.save()

    return instance


def create_application(*,
                       application_info: ApplicationInfo,
                       user: BaseUser,
                       full_name: str,
                       phone: str=None,
                       skype: str=None,
                       works_at: str=None,
                       studies_at: str=None,
                       has_interview_date: bool=False) -> Application:

    instance = Application(
        application_info=application_info,
        user=user,
        phone=phone,
        skype=skype,
        works_at=works_at,
        studies_at=studies_at,
        has_interview_date=has_interview_date
    )

    instance.full_clean()
    validate_can_create_or_update_application(instance=instance)
    instance.save()

    if user.profile:
        user.profile.full_name = full_name
        user.profile.save()

    return instance
