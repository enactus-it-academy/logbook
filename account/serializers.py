from djoser.serializers import UserCreateSerializer


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('username', 'password', 'is_owner')
