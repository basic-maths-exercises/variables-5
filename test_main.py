import unittest
import main

class UnitTests(unittest.TestCase) :
    def test_ratio(self) :
      self.assertTrue( numerator / denominator == 4 / (7*(10-4)), "The value of numerator has not been set to the correct value at the end of the code."  )
      
    def test_r_correct(self) : 
      self.assertTrue( r == (4+5)*(3+1/2)/(7*(10-4)), "The value that has been calculated for r is not correct" )
      
    def test_denominator_correct(self) : 
      self.assertTrue( denominator == 7*(10-4), "The variable called denominator does not have the correct value" )
      
    def test_r_exists(self) : 
      self.assertTrue( "r" in globals(), "A variable called r has not been defined" ) 
      
    def test_denominator_exists(self) : 
      self.assertTrue( "r" in globals(), "A variable called denominator has not been defined" )
      
    def test_numerator_exists(self) : 
      self.assertTrue( "r" in globals(), "A variable called numerator has not been defined" )
