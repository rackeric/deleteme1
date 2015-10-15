import unittest
import app

class TestMethods(unittest.TestCase):

  def test_myput(self):
      self.assertEqual(app.myput(5), 5)
      

if __name__ == '__main__':
    unittest.main()
