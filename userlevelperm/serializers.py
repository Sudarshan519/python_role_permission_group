from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

from django.core.exceptions import ValidationError 
import re
def validate_pass(password):
    if re.search('[A-Z]', password)==None and re.search('[0-9]', password)==None and re.search('[^A-Za-z0-9]', password)==None:
            raise ValidationError(
                ("This password is not strong."),
                code='password_is_weak',
            )
    return True
    # else:
    #     raise ValidationError("Your password must contain at least 1 number, 1 uppercase and 1 non-alphanumeric character.")
 
class UserSerializer(serializers.HyperlinkedModelSerializer): 
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_pass],
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password',}
    )

    class Meta:
        model = User
        fields = ('id','url', 'username', 'email', 'password')

 
    # class Meta:
    #     model = User
    #     fields = ['url', 'id', 'username', 'email','date_joined',#'is_staff',
    #            'password',   #'user_permissions',
    #               "firebase_token","created_gps","device_id", 
    #     ]
    #     write_only_fields = ('password',)

    # def create(self, validated_data):
    #     # self.is_staff=False
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return User.objects.create(**validated_data)


# class RegisterUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User