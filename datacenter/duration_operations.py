import django
from django.utils.timezone import localtime


def get_visit_duration(passcard):
    entered_time = django.utils.timezone.localtime(passcard.entered_at)
    exit_time = django.utils.timezone.localtime(passcard.leaved_at)
    delta = exit_time - entered_time
    return delta


def is_visit_long(visit,minutes=60):
    visit_dur = get_visit_duration(visit)
    return visit_dur.total_seconds() > minutes * 60


def format_duration(duration):
    return f"{int(duration.total_seconds() // 3600)}:{int((duration.total_seconds() % 3600) // 60)}"
