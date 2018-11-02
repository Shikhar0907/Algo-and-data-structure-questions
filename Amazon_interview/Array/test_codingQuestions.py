import unittest
import codingQuestion


class TestCode(unittest.TestCase):

    def test_fisrt(self):
        result = codingQuestion.arithmetic_boggle(4,[])
        self.assertEqual(result,False)

if '__name__' == '__main__':
    unittest.main()
        
