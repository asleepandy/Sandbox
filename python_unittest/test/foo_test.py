import sys
import unittest


class FooTest(unittest.TestCase):
    """Sample test case"""

    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "FooTest:setUp_"

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "FooTest:tearDown_"

    # test routine A
    # @unittest.skip("FooTest:test_A:skipped")
    def test_A(self):
        """Test routine A"""
        self.skipTest("FooTest:test_A:skipped")
        print "FooTest:test_A"

    # test routine B
    def test_B(self):
        """Test routine B"""
        fooA = 123
        fooB = 234
        self.assertEqual(fooA, fooB, "A is not equal to B")
        print "FooTest:test_B"

    # test routine C
    def test_C(self):
        """Test routine C"""
        fooA = 123
        fooB = None
        self.assertEqual(fooA, fooB, "A is not equal to B")
        print "FooTest:test_C"

    # test routine D
    def test_D(self):
        """Test routine D"""
        self.fail("FooTest:test_D:fail_")
        print "FooTest:test_D"

# Run the test case
# if __name__ == '__main__':
    # fooSuite = unittest.TestLoader().loadTestsFromTestCase(FooTest)
    # fooSuite = unittest.TestSuite()
    # fooSuite.addTest(FooTest('test_A'))
    # fooSuite.addTest(FooTest('test_B'))
    # fooRunner = unittest.TextTestRunner(descriptions=True)
    # fooResult = fooRunner.run(fooSuite)

    # print
    # print "---- START OF TEST RESULTS"
    # print fooResult
    # print
    # print "fooResult::errors"
    # print fooResult.errors
    # print
    # print "fooResult::failures"
    # print fooResult.failures
    # print
    # print "fooResult::skipped"
    # print fooResult.skipped
    # print
    # print "fooResult::successful"
    # print fooResult.wasSuccessful()
    # print
    # print "fooResult::test-run"
    # print fooResult.testsRun
    # print "---- END OF TEST RESULTS"
    # print
