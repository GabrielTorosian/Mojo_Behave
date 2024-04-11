@navigation_settings_pages
Feature: Navigation Settings pages

    Background:
        Given launch Chrome browser

    Scenario: Successfull login
        When go on page "https://lb11.mojosells.com/login/"
        And fill "g.torosyan@g-sg.net" in field "Email"
        And fill "password1" in field "Password"
        And click "Submit"
        And close Expired Data popup if it present
        Then wait until page be loaded in showing "Training Webinars" title

        Then go to Settings
        And go to Dialer-Callback Messages
        And go to Dialer-Drop Voicemail
        And go to Dialer-Dialer Settings
        And go to Email Settings
        And go to Email-SMTP
        And go to Email-Notifications
        And go to Email-General
        And go to Email-Gmail API
        And go to Letter Templates
        And go to Action Plans
        And go to Scripts-Lead Sheet
        And go to Scripts-Calling Scripts
        And go to Scripts-Lead Capture Forms
        And go to Scripts-Checklists
        And go to Data Management-Misc Fields
        And go to Data Management-Import history
        And go to Data Management-Restore Deleted Data
        And go to Data Management-Export history
        And go to Data Management-DNC Scrubbing
        And go to Data Management-DNC Export
        And go to Data Management-DNC History
        And go to Data Management-Contact Source
        And go to Appearance

        And logout
        And close browser