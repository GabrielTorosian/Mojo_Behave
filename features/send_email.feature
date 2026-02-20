@send_email
Feature: Send email from CS (hasn't finished. problem with wait of success popup )

    Background:
        Given launch Chrome browser with saved session

    Scenario: Successfull login
        Then go to Data Dialer page

        Then search and open contact "Knoxville2711"
        Then send manual CS email

        And logout
        And close browser