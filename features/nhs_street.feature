@nhs_street
Feature: Go to NHS page. Check NHS screen. Street search. Import contacts.

    Background:
        Given launch Chrome browser

    Scenario: Successfull login, go to NHS page, check NHS screen(left menu, map legend(doesnt use)), street search,
    import Mojo Leadstore contacts.
    Check resulting popup: assert "Successfully" item, check count of imported contacts, that must be > 0
        When go on page "https://lb11.mojosells.com/login/"
        And fill "g.torosyan@g-sg.net" in field "Email"
        And fill "password1" in field "Password"
        And click "Submit"
        And close Expired Data popup if it present
        Then wait until page be loaded in showing "Training Webinars" button

        Then go to Data Dialer page
        Then go to NHS  search address "Edgecroft Rd Kensington, CA 94707"

        And logout
        And close browser