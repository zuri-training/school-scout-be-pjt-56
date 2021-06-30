import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient,  APITestCase

from core.models import School
from .serializers import SchoolSerializer

# TEST FOR SCHOOLS

class SchoolTestsCreate(APITestCase):
    """ Test module for POST school API """
    def setUp(self):
        self.client = APIClient()
       #user = User.objects.create(<fill params here>)
        
        #create test database
        self.data = {
                    'school_name': 'Zuri University',
                    'overview': 'Zuri is an insitution of higher learning',
                    'location': 'Zuri',  
                    'overview': 'Zuri is an insitution of higher learning',
                    'location': 'Zuri'
        }

    def test_create_school(self):
            #get API response
        url = reverse('create-school')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 1)
        self.assertEqual(School.objects.get().school_name, 'Zuri University')



class SchoolListTest(APITestCase):
    """ Test module for GET schools API """
    def setUp(self):
        #create test database
        self.zuriuniversity = School.objects.create(
            school_name='Zuri University', overview = 'Something about zuri', location='zuri')
        self.i4guniversity = School.objects.create(
            school_name='I4G University', overview = 'Something about I4G', location='I4G')

    
    def test_school_list_view(self):
            #get API response
        url = reverse('get-school-list')
        response = self.client.get(url, format='json')
    
        #get data from database
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




class UpdateSchoolTest(APITestCase):
    """ Test module for PUT school API"""
    def setUp(self):
        #create test database
        self.zuriuniversity = School.objects.create(
            school_name='Zuri University', overview = 'Something about zuri', location='zuri')
    
        self.data = {
            'school_name': 'Zuri Univeristy',
            'overview' : 'Something about zuri', 
            'location':'zuri'  
        }

    def test_update_school(self):
         #get API response
        url = reverse('update-school', kwargs={'pk': self.zuriuniversity.pk})
        response = self.client.put( url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteSpecificSchoolTest(APITestCase):
    """ Test module for DELETE school API """
    def setUp(self):
        #create test database
        self.zuriuniversity = School.objects.create(
            school_name='Zuri University', overview = 'Something about zuri', location='zuri')
        
    def test_delete_school(self):
         #get API response
        url = reverse('delete-school', kwargs={'pk': self.zuriuniversity.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class GetSpecificSchoolTest(APITestCase):
    """ Test module for GET single school API """
    def setUp(self):
        #create test database
        self.zuriuniversity = School.objects.create(
            school_name='Zuri University', overview = 'Something about zuri', location='zuri')
                                                
    def test_get_specific_school(self):
         #get API response
        url =  reverse('view-school', kwargs={'pk': self.zuriuniversity.pk})
        response = self.client.get(url)

        #get data from database
        school = School.objects.get(pk=self.zuriuniversity.pk)
        serializer = SchoolSerializer(school)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
