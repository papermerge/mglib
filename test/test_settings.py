import os
from pathlib import Path
import unittest

from mglib.conf.settings import (
    MgLibSettings,
    DefaultSettings
)

DATA_DIR = os.path.join(
    Path(__file__).parent,
    'data'
)


class TestMgLibSettings(unittest.TestCase):

    def setUp(self):
        self.settings = MgLibSettings(DefaultSettings())

    def test_settings_outside_django_should_work(self):
        """
        Without django there should be default values
        for settings
        """
        # check default value for pdfinfo
        self.assertEqual(
            "/usr/bin/pdfinfo",
            self.settings.BINARY_PDFINFO
        )

    def test_settings_are_configurable(self):
        """
        User should be able to reconfigure mglibsettings
        on the go (i.e. change default values).
        """
        # check default value for pdfinfo
        self.settings.configure(
            BINARY_PDFINFO="/usr/bin/xyz"
        )
        self.assertEqual(
            "/usr/bin/xyz",
            self.settings.BINARY_PDFINFO
        )

