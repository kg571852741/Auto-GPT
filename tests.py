import unittest

import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import coverage

def run_tests():
    # Start coverage collection
    cov = coverage.Coverage()
    cov.start()

    # Load all tests from the 'autogpt/tests' package
    suite = unittest.defaultTestLoader.discover("./tests")

    # Run the tests
    result = unittest.TextTestRunner().run(suite)
    # Stop coverage collection
    cov.stop()
    cov.save()

    # Report the coverage
    cov.report(show_missing=True)

    # Exit with a non-zero code if any of the tests failed
    if not result.wasSuccessful():
        exit(1)
# import unittest

# import coverage

# if __name__ == "__main__":
#     # Start coverage collection
#     cov = coverage.Coverage()
#     cov.start()

#     # Load all tests from the 'autogpt/tests' package
#     suite = unittest.defaultTestLoader.discover("./tests")

#     # Run the tests
#     unittest.TextTestRunner().run(suite)

#     # Stop coverage collection
#     cov.stop()
#     cov.save()

#     # Report the coverage
#     cov.report(show_missing=True)
