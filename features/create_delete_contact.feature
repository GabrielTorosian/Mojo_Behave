@create_delete_contact_test
Feature: Manual create, create note, edit note, delete note, delete contact

    Background:
        Given launch Chrome browser with saved session

    Scenario: Successfull login, create new new contact in new group, find contact, delete contact, delete group
        Then go to Data Dialer page
        Then click Create Contact button
        Then fill fields and create group for a new contact
        Then create note "this is an auto note_1"


        Then delete contact Autocreate Contact01
        Then delete created group Autotest CrContact group

        And logout
        And close browser
