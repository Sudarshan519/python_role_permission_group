from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

from userlevelperm.models import Post

def create_permission():
    try:
        content_type = ContentType.objects.get_for_model(Post)
        post_permission = Permission.objects.filter(content_type=content_type)
        print([perm.codename for perm in post_permission])
        # => ['add_post', 'change_post', 'delete_post', 'view_post']

        user = User.objects.create_user(username="test", password="test", email="test@user.com")

        # Check if the user has permissions already
        print(user.has_perm("userlevelperm.view_post"))
        # => False

        # To add permissions
        for perm in post_permission:
            user.user_permissions.add(perm)

        print(user.has_perm("userlevelperm.view_post"))
        # => False
        # Why? This is because Django's permissions do not take
        # effect until you allocate a new instance of the user.

        user = get_user_model().objects.get(email="test@user.com")
        print(user.has_perm("userlevelperm.view_post"))
        # => True
    except:
        print('already executed')
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from userlevelperm.models import Post

def create_group():
    try:
        author_group, created = Group.objects.get_or_create(name="Author")
        editor_group, created = Group.objects.get_or_create(name="Editor")
        publisher_group, created = Group.objects.get_or_create(name="Publisher")

        content_type = ContentType.objects.get_for_model(Post)
        post_permission = Permission.objects.filter(content_type=content_type)
        print([perm.codename for perm in post_permission])
        # => ['add_post', 'change_post', 'delete_post', 'view_post']

        for perm in post_permission:
            if perm.codename == "delete_post":
                publisher_group.permissions.add(perm)

            elif perm.codename == "change_post":
                editor_group.permissions.add(perm)
                publisher_group.permissions.add(perm)
            else:
                author_group.permissions.add(perm)
                editor_group.permissions.add(perm)
                publisher_group.permissions.add(perm)

        user = User.objects.get(username="test")
        user.groups.add(author_group)  # Add the user to the Author group

        user = get_object_or_404(User, pk=user.id)

        print(user.has_perm("userlevelperm.delete_post")) # => False
        print(user.has_perm("userlevelperm.change_post")) # => False
        print(user.has_perm("userlevelperm.view_post")) # => True
        print(user.has_perm("userlevelperm.add_post")) # => True
    except:
        print('group exists')