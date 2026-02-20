@st_one_time_lookup_test
Feature: Create new list from DataDialer. Skip Tracer. One time lookup, delete contact from CS. Search list from DataDialer. Delete list from DataDialer.

    Background:
        Given launch Chrome browser with saved session

    Scenario: Successfull login, create new new contact in new group, find contact, delete contact, delete group
        Then go to Data Dialer page
        Then create list "01 ST onetime lookup autotest"
        Then press ST one time lookup with "18891 Shoshonee Rd Apple Valley, CA 92307" in "01 ST onetime lookup autotest"
        Then delete list "01 ST onetime lookup autotest" from DataDialer

        And logout
        And close browser
