@import_file_test
Feature: Import file csv

    Background:
        Given launch Chrome browser

    Scenario: Successfull login, create new list 0101 auto new1, import file, delete list 0101 auto new1
        When go on page "https://lb11.mojosells.com/login/"
        And fill "g.torosyan@g-sg.net" in field "Email"
        And fill "password1" in field "Password"
        And click "Submit"
        And close Expired Data popup if it present
        Then wait until page be loaded in showing "Training Webinars" button

        Then go to Data Dialer page
        Then press Import file button
        And choose file for import
        Then Step2 create new list "0101 auto new1" for import
        Then Step3 mapping fields
        Then Step 4 check for duplicates
        Then Step 5 finish import
        Then close Share agent popup if it present
        Then close Skip Tracer popup if it present
        #Then go to Data Dialer page
        And search imported contacts
        Then delete list "0101 auto new1" created during import

        And logout
        And close browser