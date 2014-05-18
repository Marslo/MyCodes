import unittest
import mycase

class mytest(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testsum(self):
    self.assertEqual(mycase.sum(1, 2), 3, 'test sum fail')

  def testsub(self):
    self.assertEqual(mycase.sub(2, 1), 1, 'test sub fail')

if __name__ == '__main__':
  unittest.main()
