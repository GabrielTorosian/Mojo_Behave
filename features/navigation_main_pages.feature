@navigation_main_pages_test
Feature: Navigation on main pages

    Background:
        Given launch Chrome browser with saved session

    Scenario: Navigation on main pages
        Then go to Data Dialer page
        Then go to Calendar page
        Then go to Reports page
        And go to Session Report
        And go to Call Recording Report
        And go to Recurring Events Report
        And go to Posting Report
        And go to Agent Timesheet Report
        And go to Email Status Report
        And go to Neighborhood Search Update Report
        Then go to Leadstore page

        Then go to AI Tools page

        Then go to Settings page
        Then go to Settings Callback
        Then go to Settings Voicemail
        Then go to Dialer Settings
        Then go to Settings Email
        Then go to Settings Email Templates
        Then go to Settings Email Notifications
        Then go to Settings Email Connect To Gmail
        Then go to Settings Email SMTP
        Then go to Settings Letter
        Then go to Settings Action Plan
        Then go to Settings Calling Scripts
        Then go to Settings Lead Sheet
        Then go to Settings Lead Capture Forms
        Then go to Settings Checklists
        Then go to Settings Do Not Call
        Then go to Settings Misc Fields
        Then go to Settings Data Management
        Then go to Settings Export History
        Then go to Settings Contact Source
        Then go to Settings Restore Deleted Data
        Then go to Settings Appearance

        And go to Integrations-Boomtown
        And go to Integrations-CINC
        And go to Integrations-Constant Contact
        And go to Integrations-Follow up boss
        And go to Integrations-Google
        And go to Integrations-Mailchimp
        And go to Integrations-Middleware-API Nation
        And go to Integrations-Middleware-CRM HQ
        And go to Integrations-Middleware-Zapier
        And go to Integrations-Posting services
        And go to Integrations-Realgeeks
        And go to Integrations-Top producer
        And go to Integrations-Wise Agent
        And go to Integrations-Zillow

        And logout
        And close browser