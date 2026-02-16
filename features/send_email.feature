@send_email
Feature: Send email from CS (hasn't finished. problem with wait of success popup )

    Background:
        Given launch Chrome browser

    Scenario: Successfull login
        When go on page "https://lb11.mojosells.com/login/"
        And fill "g.torosyan@g-sg.net" in field "Email"
        And fill "password1" in field "Password"
        And click "Submit"
        And close Expired Data popup if it present
        Then wait until page be loaded in showing "Training Webinars" button
        Then go to Data Dialer page

        Then search and open contact "Knoxville2711"
        Then send manual CS email

        And logout
        And close browser