@navigation_account_section
Feature: Navigation Account pages

    Background:
        Given launch Chrome browser

    Scenario: Successfull login
        When go on page "https://lb11.mojosells.com/login/"
        And fill "g.torosyan@g-sg.net" in field "Email"
        And fill "password1" in field "Password"
        And click "Submit"
        And close Expired Data popup if it present
        Then wait until page be loaded in showing "Training Webinars" button

        Then go to Account-Profile

        And go to Account-Manage Payments
        And go to Account-Agents
        And go to Account-Subscriptions
        And go to Account-Refer-A-Friend Invites

        And logout
        And close browser
