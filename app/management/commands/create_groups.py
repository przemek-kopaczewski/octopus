from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from app.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        administrators, created1 = Group.objects.get_or_create(name='Administrators')
        users, created2 = Group.objects.get_or_create(name='Users')

        model_ct = ContentType.objects.get_for_model(CustomUser)

        can_add = Permission(name='Can add user', codename='can_add_user', content_type=model_ct)
        can_add.save()
        can_change = Permission(name='Can change user', codename='can_change_user', content_type=model_ct)
        can_change.save()
        can_delete = Permission(name='Can delete user', codename='can_delete_user', content_type=model_ct)
        can_delete.save()
        can_view = Permission(name='Can view user', codename='can_view_user', content_type=model_ct)
        can_view.save()

        users.permissions.add(can_view)
        administrators.permissions.add(can_add, can_change, can_delete, can_view)
