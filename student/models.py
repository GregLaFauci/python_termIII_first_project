from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    student_picture = models.ImageField(upload_to='images/', blank=True)

    COURSES = (
        ('PHYSICS', 'Physics'),
        ('GEOMETRY', 'Geometry'),
        ('SOCIAL_STUDIES', 'Social Studies'),
        ('CHEMISTRY', 'Chemistry'),
        ('LANGUAGE_ARTS', 'Language Arts'),
        ('ENGLISH', 'English'),
        ('WORLD_LITERATURE', 'World Literature'),
        ('JOURNALISM', 'Journalism'),
        ('PAINTING', 'Painting'),
        ('SCULPTURE', 'Sculpture'),
        ('DRAWING', 'Drawing'),
        ('PROGRAMMING', 'Programming'),
        ('PHOTOSHOP', 'Photoshop'),
        ('WEB_DESIGN', 'Web Design'),
        ('HEALTH', 'Health'),
    )

    courses = MultiSelectField(choices=COURSES)

    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        GRADUATE = 'GR', _('Graduate')

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }

    @property
    def full_name(self):
        """Returns the student's full name."""
        return '%s %s' % (self.first_name, self.last_name)


    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return full_name