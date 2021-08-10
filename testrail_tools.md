# Testrail API Client Tools

Client tool for querying Testrail API.


## suites.py

Returns data for test suites.


### Summary 

To run a query of test suite data, you'll need to provide the following
1. Project name
2. Test Suite
3. Test case filter (see below)

```
<output snippet showing parameter help>
```

### Constructing Queries 

#### Project Name**

TBD


#### Test Suite

At the top level, Testrail provides a list of "Test Suites & Cases."


#### Test Case Filters

Within a test suite, Testrail provides a number of filters. This tool will only make use 
of the following ones listed (see NOTES below for comprehensive list of filters avail. thru 
API)


> Automation [Any, Untriaged, Suitable, Unsuitable, Completed, Disabled]  <br />
  References [list of test names]  <br />
  Test Objective [us for 'AUTOMATION_MISSING_STEPS' flag]  <br />
  Title  <br />
  Type [Functional, Smoke & Sanity]  <br />


NOTE

Additional first level filters listed here for reference only

> Automation <br />
  Automation Type <br />
  Created By <br />
  Created On <br />
  Estimate <br />
  Forecast <br />
  Owner <br />
  Priority <br />
  References <br />
  Section <br />
  Template <br />
  Test Area <br />
  Test Objective <br />
  Title <br />
  Type <br />
  Updated By <br />
  Updated On <br />


### Example Queries

```
python ./suite.py --project=fenix --test-suites=full_functional --filters=xxxxxxx
```

## runs.py

Returns data for test runs

TBD

```
<output snippet showing parameter help>
```
