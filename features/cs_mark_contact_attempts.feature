@cs_mark_contact_attempts_test
Feature: CS Activities - Mark as Contact, manage call attempts, reset

  Background:
    Given launch Chrome browser

  Scenario: Login, open CS Activities, mark as contact, manage attempts, reset
    When go on page "https://lb11.mojosells.com/login/"
    And fill "g.torosyan@g-sg.net" in field "Email"
    And fill "password1" in field "Password"
    And click "Submit"
    And close Expired Data popup if it present
    Then wait until page be loaded in showing "Training Webinars" button

    Then go to Data Dialer page
    Then search contact "Knoxville2711"
    Then open CS Activities tab
    Then click Mark as Contact and verify Last Dial Date changed
    Then click plus Attempts and verify Attempts is 2
    Then click minus Attempts and verify Attempts is 1
    Then click Reset and verify Last Dial Date is N/A
    Then close CS
    Then logout
