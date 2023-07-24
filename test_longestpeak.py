import unittest
import longestpeak as lp

class LongestPeakTest(unittest.TestCase):
  def sampleInput(self):
    givenArray = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
    actualAnswer = 6
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)

  def testCaseOne(self):
    givenArray = []
    actualAnswer = 0
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)

  def testCaseTwo(self):
    givenArray = [1,3,2]
    actualAnswer = 3
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)


  def testCaseThree(self):
    givenArray = [5, 4, 3, 2, 1, 2, 1]
    actualAnswer = 3
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)


  def testCaseFour(self):
    givenArray = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
    actualAnswer = 5
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)

  def testCaseFive(self):
    givenArray = [5, 4, 3, 2, 1, 2, 10, 12]
    actualAnswer = 0
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)

  def testCaseSix(self):
    givenArray = [1, 2, 3, 4, 5, 6, 10, 100, 1000]
    actualAnswer = 0
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)

  def testCaseSeven(self):
    givenArray = [1, 2, 3, 3, 2, 1]
    actualAnswer = 0
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)

  def testCaseEight(self):
    givenArray = [1, 1, 3, 2, 1]
    actualAnswer = 4
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)

  def testCaseNine(self):
    givenArray = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
    actualAnswer = 9
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)

  def testCaseTen(self):
    givenArray = [1, 2, 3, 3, 4, 0, 10]
    actualAnswer = 3
    self.userOutput = lp.longestpeak(givenArray)
    self.assertEqual(self.userOutput,actualAnswer)
