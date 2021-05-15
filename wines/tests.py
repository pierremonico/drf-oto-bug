from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from wines.models import Bottle, Cork


class WineTesting(APITestCase): # isn't it spelled WineTasting?
    def test_create_bottle_with_cork_fk(self):
        """
        Test if we can create a Bottle object and set its `cork` reverse relationship.
        """
        # Cork
        cork_create_url = reverse('cork-list')
        cork_data = { "name": "Corky"}

        cork_response = self.client.post(cork_create_url, cork_data, format='json')
        cork_id = cork_response.data["id"]

        self.assertEqual(cork_response.status_code, status.HTTP_201_CREATED)

        # Bottle with Cork
        bottle_create_url = reverse('bottle-list')
        bottle_data = {
            "name": "Domaine de la Romanée-Conti",
            "cork": cork_id
        }

        bottle_response = self.client.post(bottle_create_url, bottle_data, format='json')
        bottle_id = bottle_response.data["id"]

        self.assertEqual(bottle_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bottle_response.data["cork"], cork_id)

        bottle_from_db = Bottle.objects.get(id=bottle_id)
        
        print(bottle_from_db.name)

        self.assertEquals(bottle_from_db.cork.id, cork_id)