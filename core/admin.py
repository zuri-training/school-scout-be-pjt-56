
from django.contrib import admin

# from core.savedcourse.models import SavedCourse
# from core.savedscholarship.models import SavedScholarship
# from core.savedschool.models import SavedSchool
# from core.advisor.models import CareerQuestion, CareerQuestionAnswer, CareerQuestionOption
from core.student.models import StudentAccount #StudentAccountAdmin
# from core.testimonials.models import Testimonial
# from core.news.models import News
from core.schools.models import School
# from core.reviews.models import Review
from core.faculty.models import Faculty
from core.department.models import Department
# from core.courses.models import Course
from core.comments.models import Comment
from core.articles.models import Article
from core.scholarships.models import Scholarship
# #from core.location.models import Location
# from core.requirement.models import EntryRequirement
# from core.fees.models import Tuition

   


# #poshpeck
admin.site.register(StudentAccount)
# admin.site.register(StudentAccountAdmin)
# admin.site.register(CareerQuestion)
# admin.site.register(CareerQuestionAnswer)
# admin.site.register(SavedSchool)
# admin.site.register(SavedScholarship)
# admin.site.register(SavedCourse)
# admin.site.register(CareerQuestionOption)


# #pauline-banye
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Scholarship)
# admin.site.register(News)
# #admin.site.register(EntryRequirement)



#hezekiah
#admin.site.register(Course)
admin.site.register(School)


#Iconnell
#admin.site.register(Review)
#admin.site.register(Testimonial)


#Blaise
#admin.site.register(Location)
#admin.site.register(Tuition)











