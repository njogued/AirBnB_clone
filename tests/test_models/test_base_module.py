#!/usr/bin/python3
'''
Test the Base Class
Cool fact: Use g; to go to last edited line before save

Issue: Remove the path in os.remove() in test_first_file_storage
'''
import unittest
import datetime
import os
import sys
sys.path.append("/alx-higher_level_programming/BnB")
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    '''Test the base class methods and attributes'''
    @classmethod
    def setUpClass(cls):
        '''setUpClass method to create the test object'''
        cls.obj = BaseModel()
        cls.obj2 = BaseModel()

    def test_uuid(self):
        '''Test the unique ID initilization'''
        self.assertIsInstance(TestBase.obj, BaseModel)
        self.assertTrue(hasattr(TestBase.obj, "id"))
        self.assertEqual(str, type(TestBase.obj.id))
        self.assertNotEqual(TestBase.obj.id, TestBase.obj2.id)
        obj3 = BaseModel(**(TestBase.obj.to_dict()))
        self.assertEqual(obj3.id, TestBase.obj.id)

    def test_datetime(self):
        '''Test the datetime initilization and update'''
        self.assertIsInstance(TestBase.obj.created_at, datetime.datetime)
        self.assertIsInstance(TestBase.obj.updated_at, datetime.datetime)
        self.assertNotEqual(TestBase.obj.created_at, TestBase.obj2.created_at)
        TestBase.obj.save()
        self.assertNotEqual(TestBase.obj.created_at, TestBase.obj.updated_at)

    def test_strmethod(self):
        '''Test the return string from the __str__ method'''
        string = f"[{TestBase.obj.__class__.__name__}] \
({TestBase.obj.id}) {TestBase.obj.__dict__}"
        self.assertEqual(str(TestBase.obj), string)
        self.assertIsInstance(str(TestBase.obj), str)

    def test_to_dict(self):
        '''Test the to_dict method'''
        dct = TestBase.obj.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIsInstance(dct["updated_at"], str)
        self.assertIsInstance(dct["created_at"], str)
        updateiso = TestBase.obj.updated_at.isoformat()
        self.assertEqual(updateiso, dct["updated_at"])

    def test_first_file_storage(self):
        '''Test the serialization and deserialization of BaseModel'''
        '''os.remove("/alx-higher_level_programming/BnB/file.json")'''
        objects = storage.all()
        self.assertIsInstance(objects, dict)

    @classmethod
    def tearDownClass(cls):
        '''tearDownClass method to destroy object after all tests run'''
        del cls.obj
        del cls.obj2


if __name__ == "__main__":
    unittest.main()
