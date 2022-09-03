from django.conf import settings

GUARD_DEPT_MODEL = getattr(settings, "GUARD_DEPT_MODEL", "guard.Department")
