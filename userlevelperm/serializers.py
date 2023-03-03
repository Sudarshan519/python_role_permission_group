from rest_framework import serializers
from .models import User
class UserSerializer(serializers.HyperlinkedModelSerializer): 
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
  
    class Meta:
        model = User
        fields = [#'url', 
        'id',# 'username',
         'email',
         'password',
         'is_foreigner',
         'date_joined',#'is_staff',
                  #'user_permissions',
                  "firebase_token","created_gps","device_id", 
        ]
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        # self.is_staff=False
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    