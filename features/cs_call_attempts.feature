@create_call_attempts_cs_test
Feature: Search contact. Mark as contact. + call attempt. Reset call attempt


  Background:
        Given launch Chrome browser

  Scenario: Successfull login, find contact in group, mark as contact, +attempt, -attempt, reset
        When go on page "https://lb11.mojosells.com/login/"
        And fill "g.torosyan@g-sg.net" in field "Email"
        And fill "password1" in field "Password"
        And click "Submit"
        And close Expired Data popup if it present
        Then wait until page be loaded in showing "Training Webinars" button

        Then go to Data Dialer page
        Then search contact "Knoxville2711"
        Then cs activities section