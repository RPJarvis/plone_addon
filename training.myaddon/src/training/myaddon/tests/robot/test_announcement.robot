# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s training.myaddon -t test_announcement.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src training.myaddon.testing.TRAINING_MYADDON_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_announcement.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Announcement
  Given a logged-in site administrator
    and an add announcement form
   When I type 'My Announcement' into the title field
    and I submit the form
   Then a announcement with the title 'My Announcement' has been created

Scenario: As a site administrator I can view a Announcement
  Given a logged-in site administrator
    and a announcement 'My Announcement'
   When I go to the announcement view
   Then I can see the announcement title 'My Announcement'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add announcement form
  Go To  ${PLONE_URL}/++add++Announcement

a announcement 'My Announcement'
  Create content  type=Announcement  id=my-announcement  title=My Announcement


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the announcement view
  Go To  ${PLONE_URL}/my-announcement
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a announcement with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the announcement title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
