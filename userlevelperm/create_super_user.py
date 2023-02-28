from django.contrib.auth import get_user_model
User = get_user_model()
def create_admin():
    try:
        superuser = User.objects.create_superuser(
            username="super", password="test", email="super@test.com"
        )
    
        # Output will be true
        print(superuser.has_perm("userlevelperm.view_post"))

        # Output will be true even if the permission does not exists
        print(superuser.has_perm("foo.add_bar"))
    except Exception as e:
        print(e)
        print("user exists")