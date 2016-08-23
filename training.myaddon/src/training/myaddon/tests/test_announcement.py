# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from training.myaddon.testing import TRAINING_MYADDON_INTEGRATION_TESTING  # noqa
from training.myaddon.interfaces import IAnnouncement

import unittest2 as unittest


class AnnouncementIntegrationTest(unittest.TestCase):

    layer = TRAINING_MYADDON_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Announcement')
        schema = fti.lookupSchema()
        self.assertEqual(IAnnouncement, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Announcement')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Announcement')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IAnnouncement.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Announcement', 'Announcement')
        self.assertTrue(
            IAnnouncement.providedBy(self.portal['Announcement'])
        )
