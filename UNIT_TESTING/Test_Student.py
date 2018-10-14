import unittest
from Student1 import Student
from Inventory import Inventory

class TestStudent(unittest.TestCase):
    
    def test_addStudInfo(self):
        self.assertTrue(Student('Fernando',2014102239,'ECE126L','N208','Sir'))
    
    def test_removeStudInfo(self):
        self.assertTrue(Student('Fernando',2014102239,'ECE126L','N208','Sir'))

class TestInventory(unittest.TestCase):
    
    def test_borrowItems(self):
        self.assertTrue(Inventory(2014102239, 'Rack','Switch','Router','Console','LAN','Power'))

    def test_returnItems(self):
        self.assertTrue(Inventory(2014102239, 'Rack','Switch','Router','Console','LAN','Power'))

    
    
if __name__ == "__main__":
    unittest.main()