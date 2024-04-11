@navigation_main_pages_test
Feature: Navigation on main pages

    Background:
        Given launch Chrome browser

    Scenario: Navigation on main pages
        When go on page "https://lb11.mojosells.com/login/"
        And fill "g.torosyan@g-sg.net" in field "Email"
        And fill "password1" in field "Password"
        And click "Submit"
        And close Expired Data popup if it present
        Then wait until page be loaded in showing "Training Webinars" title
        Then go to Data Dialer page
        Then go to Calendar page
        Then go to Reports page
        And go to Session Report
        And go to Call Recording Report
        And go to Recurring Events Report
        And go to Posting Report
        And go to Mojo Voice Report
        And go to Agent Timesheet Report
        And go to Email Status Report
        And go to Neighborhood Search Update Report
        Then go to Leadstore page

        And logout
        And close browser