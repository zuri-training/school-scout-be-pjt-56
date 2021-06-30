import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient,  APITestCase

from core.models import Course, School
from .serializers import CourseSerializer


#TEST FOR COURSES

class CourseCreateTest(APITestCase):
    """ Test module for POST course API """
    def setUp(self):
        self.client = APIClient()
       #user = User.objects.create(<fill params here>)
        
        #create test database
        self.school = School.objects.create(
            school_name='Zuri University', overview = 'Something about zuri', location='zuri')

        self.data = {
                    'course_name':'Backend',
                    'school': 1
        }

    def test_create_course(self):
            #get API response
        url = reverse('create-course')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().course_name, 'Backend')

class CourseListTest(APITestCase):
    """ Test module for GET Courses API """
    def setUp(self):
        #create test database
        self.backend = Course.objects.create(
                course_name = 'Backend',
                school =  School.objects.create(
                school_name='Zuri University', overview = 'Something about zuri', location='zuri'
                )
                   )
        self.frontend = Course.objects.create(
                course_name = 'Frontend',
                school = School.objects.create(
                school_name='I4G University', overview = 'Something about I4G', location='I4G'
                )
                    )
        
    def test_course_list_view(self):
            #get API response
        url = reverse('get-course-list')
        response = self.client.get(url, format='json')
        #get data from database
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateCourseTest(APITestCase):
    """ Test module for PUT course API"""
    def setUp(self):
        #create test database

        self.frontend = Course.objects.create(
                course_name = 'Frontend',
                school = School.objects.create(
                school_name='I4G University', overview = 'Something about I4G', location='I4G'
        )
    )
        
        self.data = {
            'course_name':'Frontend',
            'school': 1
}
    def test_update_course(self):
         #get API response
        url = reverse('update-course', kwargs={'pk': self.frontend.pk})
        response = self.client.put( url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class DeleteSpecificSchoolTest(APITestCase):
    """ Test module for DELETE course API """
    def setUp(self):
        #create test database
        self.frontend = Course.objects.create(
            course_name = 'Frontend',
            school = School.objects.create(
            school_name='I4G University', overview = 'Something about I4G', location='I4G'
        )
    )
            
    def test_delete_course(self):
         #get API response
        url = reverse('delete-course', kwargs={'pk': self.frontend.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class GetSpecificCourseTest(APITestCase):
    """ Test module for GET single course API """
    def setUp(self):
        #create test database
        self.frontend = Course.objects.create(
            course_name = 'Frontend',
            school = School.objects.create(
            school_name='I4G University', overview = 'Something about I4G', location='I4G'
        )
    )
                                                
    def test_get_specific_course(self):
         #get API response
        url =  reverse('view-course', kwargs={'pk': self.frontend.pk})
        response = self.client.get(url)

        #get data from database
        course = Course.objects.get(pk=self.frontend.pk)
        serializer = CourseSerializer(course)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
