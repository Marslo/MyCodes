import unittest
import myclass

class myclasstest(unittest.TestCase):

  def setUp(self):
    self.tclass = myclass.myclass()

  def tearDown(self):
    pass

  def testsum(self):
    self.assertEqual(self.tclass.sum(1,2), 3, 'tclass sum failed')

  def testsub(self):
    self.assertEqual(self.tclass.sub(2, 1), 0, 'tclass sub failed')

if __name__ == '__main__':
  unittest.main()
