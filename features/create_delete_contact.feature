@create_delete_contact_test
Feature: Manual create, create note, edit note, delete note, delete contact

    Background:
        Given launch Chrome browser

    Scenario: Successfull login, create new new contact in new group, find contact, delete contact, delete group
        When go on page "https://lb11.mojosells.com/login/"
        And fill "g.torosyan@g-sg.net" in field "Email"
        And fill "password1" in field "Password"
        And click "Submit"
        And close Expired Data popup if it present
        Then wait until page be loaded in showing "Training Webinars" button

        Then go to Data Dialer page
        Then click Create Contact button
        Then fill fields and create group for a new contact
        Then create note "this is an auto note_1"


        Then delete contact Autocreate Contact01
        Then delete created group Autotest CrContact group

        And logout
        And close browser
