# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from training.myaddon.testing import TRAINING_MYADDON_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that training.myaddon is properly installed."""

    layer = TRAINING_MYADDON_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if training.myaddon is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'training.myaddon'))

    def test_browserlayer(self):
        """Test that ITrainingMyaddonLayer is registered."""
        from training.myaddon.interfaces import (
            ITrainingMyaddonLayer)
        from plone.browserlayer import utils
        self.assertIn(ITrainingMyaddonLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TRAINING_MYADDON_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['training.myaddon'])

    def test_product_uninstalled(self):
        """Test if training.myaddon is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'training.myaddon'))

    def test_browserlayer_removed(self):
        """Test that ITrainingMyaddonLayer is removed."""
        from training.myaddon.interfaces import ITrainingMyaddonLayer
        from plone.browserlayer import utils
        self.assertNotIn(ITrainingMyaddonLayer, utils.registered_layers())
