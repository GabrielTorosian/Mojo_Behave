@export_contacts
Feature: test

    Background:
        Given launch Chrome browser

    Scenario: Search Group. Select group.
        When go on page "https://lb11.mojosells.com/login/"
        And fill "g.torosyan@g-sg.net" in field "Email"
        And fill "password1" in field "Password"
        And click "Submit"
        And close Expired Data popup if it present
        Then wait until page be loaded in showing "Training Webinars" button

        Then go to Data Dialer page
        Then go to group "autotest_group"
        Then select all export contacts

        And logout
        And close browser