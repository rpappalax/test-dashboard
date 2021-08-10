Testrail tools
===========
Client tool for querying Testrail API.


suites.py
----------
Returns data for test suites.

```
<output snippet showing parameter help>
```

**Top Level**
At the top level, Testrail provides a list of "Test Suites & Cases."

Examples

Test Suite: "Full Functional Tests Suite"

Within a test suite, Testrail provides a number of filters. This tool will only make use 
of the following ones listed (see NOTES below for comprehensive list of filters avail. thru 
API)

```
Automation [Any, Untriaged, Suitable, Unsuitable, Completed, Disabled]
References [list of test names]
Test Objective [use for 'AUTOMATION_MISSING_STEPS' flag]
Title
Type [Functional, Smoke & Sanity]

```


NOTES
Additional first level filters listed here for reference only

```
Automation
Automation Type
Created By
Created On
Estimate
Forecast
Owner
Priority
References
Section
Template
Test Area
Test Objective
Title
Type
Updated By
Updated On
```


runs.py
--------
Returns data for test runs

TBD

```
<output snippet showing parameter help>
```
