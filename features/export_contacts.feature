@export_contacts
Feature: test

    Background:
        Given launch Chrome browser with saved session

    Scenario: Search Group. Select group.
        Then go to Data Dialer page
        Then go to group "autotest_group"
        Then select all export contacts

        And logout
        And close browser