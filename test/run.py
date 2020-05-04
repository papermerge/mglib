import os
import sys
import argparse
from unittest.loader import TestLoader
from unittest.runner import TextTestRunner

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

test_loader = TestLoader()
test_runner = TextTestRunner()

parser = argparse.ArgumentParser()

tests = test_loader.discover(
    start_dir=BASE_DIR,
)

result = test_runner.run(tests)

if not result.wasSuccessful():
    sys.exit(1)
