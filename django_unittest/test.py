from django.test import TestCase
from myapp1.models import MyApp1, MyApp2, MyApp3


class MyApp1Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        MyApp1.objects.create(name='Big', surname='Bob', age="66", status=True, sex="Male")

    def test_name(self):
        author=MyApp1.objects.get(id=1)
        self.assertEquals(author.name,'Big')

class MyApp2Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        MyApp2.objects.create(name='Alex', surname='Bobr', age="21", status=True, sex="Male")

    def test_name(self):
        author=MyApp2.objects.get(id=1)
        self.assertEquals(author.name,'Alex')

class MyApp3Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        MyApp3.objects.create(name='Petro', surname='Griboyed', age="103", status=False, sex="Male")

    def test_name(self):
        author=MyApp3.objects.get(id=1)
        self.assertEquals(author.name,'Petro')
