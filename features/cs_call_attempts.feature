@create_call_attempts_cs_test
Feature: Search contact. Mark as contact. + call attempt. Reset call attempt


  Background:
        Given launch Chrome browser with saved session

  Scenario: Successfull login, find contact in group, mark as contact, +attempt, -attempt, reset
        Then go to Data Dialer page
        Then search contact "Knoxville2711"
        Then cs activities section