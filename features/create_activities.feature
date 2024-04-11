@create_activities
Feature: Creation of App, Task, FU call activies. Deleting this activities from Calendar

    Background:
        Given launch Chrome browser

    Scenario: Successfull login
        When go on page "https://lb11.mojosells.com/login/"
        And fill "g.torosyan@g-sg.net" in field "Email"
        And fill "password1" in field "Password"
        And click "Submit"
        And close Expired Data popup if it present
        Then wait until page be loaded in showing "Training Webinars" title

        When create Appointment from CS
        And go to Calendar
        Then search App and delete it
        When create Task from CS
        And go to Calendar
        Then search Task and delete it
        When create FU call from CS
        And go to Calendar
        Then search FU call and delete it

        And logout
        And close browser