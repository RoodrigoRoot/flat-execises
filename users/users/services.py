import uuid
from typing import Dict

from users.models import Profile
from django.contrib.auth.models import User


def validate_user_exists(email):
    return User.objects.filter(email=email).first()


def create_user(data: Dict) -> User:
    user = User(**data)
    user.username = str(uuid.uuid4())
    user.save()
    return user


def create_profile(data: Dict) -> Profile:
    try:
        user_data = data.pop("user")

        user = validate_user_exists(user_data['email'])
        if not user:
            user = create_user(user_data)
            profile = Profile(**data)
            profile.property_id = str(uuid.uuid4())
            profile.user = user
            profile.save()
            return {'success': True, 'property_id': profile.property_id}

        return {'success': True, 'property_id': user.profile.property_id}

    except Exception as e:
        return {'success': False, 'message': str(e)}

