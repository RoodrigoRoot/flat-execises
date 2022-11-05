from typing import Dict

from properties.models import Property
from properties.integrations.user_api import UserApiIntegration

def create_property(data: Dict):
    try:
        owner_data = data.pop('owner', None)
        prop = Property(**data)
        response = create_owner(owner_data, prop)
        if response['success']:
            prop.save()
            return {"message": "Propiedad creada", "sucess": True}
        print(response)
        return response
    except Exception as e:
        return {"message": str(e), "sucess": False}

def create_owner(data: Dict, property_: Property) -> Dict:
    response = UserApiIntegration().send_data(data)
    if response['success']:
        property_.owner_id = response.get('property_id')
        return {'success': True}
    return response

