@create_activities
Feature: Creation of App, Task, FU call activies. Deleting this activities from Calendar

    Background:
        Given launch Chrome browser with saved session

    Scenario: Successfull login
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