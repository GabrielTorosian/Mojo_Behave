@navigation_account_section
Feature: Navigation Account pages

    Background:
        Given launch Chrome browser with saved session

    Scenario: Successfull login
        Then go to Account-Profile

        And go to Account-Manage Payments
        And go to Account-Agents
        And go to Account-Subscriptions
        And go to Account-Refer-A-Friend Invites

        And logout
        And close browser
