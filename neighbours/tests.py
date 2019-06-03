from django.test import TestCase
from .models import Neighbour, Person, Post, Business

class PersonTestClass(TestCase):
  def setUp(self):
        self.kevin = Person(id = 132, neighbourhood = 1,email_address = "gilly@gmail.com", profile_picture = ' ', bio = 'i love my neighbours')

      # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kevin,Person))
    
    

        # Testing Save method
    def test_save(self):
        self.kevin.save_person()
        persons = Person.objects.all()
        self.assertTrue(len(persons)>0)

    # Testing Delete method
    def test_delete(self):
        self.kevin.delete_person()
        persons = Person.objects.all()
        self.assertTrue(len(persons) == 0)
