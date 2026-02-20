@nhs_street
Feature: Go to NHS page. Check NHS screen. Street search. Import contacts.

    Background:
        Given launch Chrome browser with saved session

    Scenario: Successfull login, go to NHS page, check NHS screen(left menu, map legend(doesnt use)), street search,
    import Mojo Leadstore contacts.
    Check resulting popup: assert "Successfully" item, check count of imported contacts, that must be > 0
        Then go to Data Dialer page
        Then go to NHS  search address "Edgecroft Rd Kensington, CA 94707"

        And logout
        And close browser