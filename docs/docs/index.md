**TEST PLAN**

**Introduction**

yfinance is a pythonic way to scrape historical Yahoo! Finance market
data. This was originally developed to fix Yahoo! API but later became
a solution. yfinance is now a rewrite of the since decommissioned API
and implements many features from complete historical market data
retrieval to specific category retrievals (such as earnings).

<br>

1.1 Objectives

yfinance is a python-based data scraping tool used to retrieve
historical market data from Yahoo! Finance. This tool was written with
python to provide an easy alternative to a decommissioned Yahoo! API.
As a test team, we are specifically focusing on testing “.earnings”
and “.quarterly\_earnings” functions in the ticker.py file

<br>

1.2 Team Members

|   Name   | Role                          |
|:--------:|-------------------------------|
| Chelsea  | Test - Data tests             |
| Cameron  | Tester - Ticker tests         |
| Cam      | Tester- Data tests            |
| Spencer  | Tester - Test earnings values |
| Ryan     | Tester - Ticker Tests         |
<br>

**2 Scope**

For this assignment we want to test two specific functions,
“.earnings” and “.quarterly\_earnings”. These are getter functions
contained in ticker.py. These functions then call
“\_get\_fundamentals” in base.py. In order to test the two functions,
the testers must:

1.  Create mock data for the scraper to retrieve from

2.  Write a test function that calls the two specific functions

3.  Call the function and view how it runs

4.  View results and compare with mock data

 Testing will only be completed within the current scope of the two
given functions. Functions not part of this scope will likely be
ignored to reduce the complexity of tests.

<br>

**3 Assumptions / Risks**

<br>

3.1 Assumptions

Some assumptions that are related to the project:

1. Every other function not included in the scope of this project will
not impede testing results
2. Test expectations will be assumed by test creator (like how a
function should respond)

<br>

3.2 Risks

There are not many risks to be concerned with but there are a few. The
main issues arise with communication between the group members. Since
everything is online, planning and meetings require more effort to set
up. These risks are triggered by certain tasks and simple mitigation
plans are used to help combat these risks.

 | # | Risk                                                                          | Impact | Trigger                                | Mitigation Plan                                                                                                                                                                                  |
|---|-------------------------------------------------------------------------------|--------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Communication is all done online. Hard to have effective teamwork.            | High   | Planning a schedule. Divvying out work | Schedule team meetings in advance. Make sure everyone contributes to the meeting.                                                                                                                |
| 2 | Busy schedules among the team (other classes..etc)                            | Medium | Assignment deadline                    | Create documents outlining current progress and to-do-list among the team.                                                                                                                       |
| 3 | Tests do not cover all possibilities - could cause an issue with trading bots | Low    | Invalid data sent to the script        | Rigorous testing of all possible elements, in every possible way we can think of. Will never be 100% risk free though, as testing can only hope to find bugs, not prove correctness of software. |

<br>

**4 Test Approach**

The project will be following a test schedule of:

1.  Test plan creation

2.  Test case creation

3.  Test documentation and reporting

Steps 2 and 3 will be repeated as more tests need to be designed.

Exploring the product will be an important part of testing as the test
team is not familiar with using the software. Understanding the
overall code will likely be explored before writing of tests.

<br>

4.1 Problems Found

By searching the Github repository for yfinance, our team was able to
find many issues and pull requests that are linked to the
functionalities that we are testing. The problems that we found with
the codebase are as follows.

1.  Incorrect data being pulled. (Issue \#543)

2.  Data is not fetched, empty dataframe being returned (Issues \#489,
    \#475, \#191, \#423, \#328, \#291, \#254, \#181) This was fixed
    with PR \#480.

3.  Pandas Datareader is not compatible with yfinance (Issue \#400)

4.  Data is transformed incorrectly, get\_earnings() is broken
    (Issue \#223)

As can be seen, the majority of issues found were related to the empty
dataframe, which has since been fixed. We did not encounter the same
issues as described in issues \#543 and \#223, so we did not feel the
need to address them, as well, these issues are likely due to a deeper
error in the fetching of the data, or its transformation, which is not
part of the .earnings or .quarterly\_earnings properties. For issue
\#400, this is not described as a functionality issue, nor does the
yfinance page list itself as compatible with Pandas Datareader, so
this is a non-issue, at least as far as our testing is concerned.

<br>

4.2 Planned Tests

A focus on specific categories of tests was developed. This was to
help divvy out work and to create in depth tests.

| Test Category   | Testers       |
|-----------------|---------------|
| Earnings Values | Spencer       |
| Invalid Tickers | Cameron, Ryan |
| Data testing    | Cam, Chelsea  |

<br>

**5 Software Fixes**

a. Is there a pull request that implements a solution to the problems identified by your tests? 

No, all of the pull requests that we found related to our section of the code base were all closed/merged and fixed.

b. Is there a quick fix that could be proposed to the code so that the code passes the test? 

The tests that we ran successfully completed. The results that we received were what we had expected. For example, invalid tickers returned expected errors instead of producing bad data. This forces the user to input ticker information correctly. No quick fixes are needed to be proposed.
Since we didn’t find any serious problems with the functionalities that we were testing, we will not be suggesting any fixes, nor will we be linking pull requests. This is simply because we have no suggestions to make, as the code worked as intended.

<br>

**6 Test Environment**

Mock data will be used to conduct tests in order to quickly and
efficiently report test results. This mock data will be developed so
that the test returns can easily be verified and confirmed. The tests
will be written using python and libraries.

<br>

  **7 Milestones/Deliverables**                                                       

  7.1 Test Schedule
  | Task Name                            | Start     | Finish   | Effort | Comments                                                               |   |
|--------------------------------------|-----------|----------|--------|------------------------------------------------------------------------|---|
| Test Planning                        |  March 21 | March 28 |  2h    |  Ongoing development of test plan document                             |   |
| Review assignment document           |  March 21 | March 21 |  1h    |  First meeting, group went over this                                   |   |
| Create initial test plan documents   |  March 21 | March 21 |  1h    |  First meeting, group went over this                                   |   |
|  Review and understand initial code  |  March 21 | March 27 |  .5h   |  Testers created their own tests, thus went over code as they required |   |
| Create a mock server containing data |  March 21 | March 21 |  .5h   |  Spencer created mock data                                             |   |
| Test cases – Group 1                 |  March 21 | March 24 |  1h    |  Focused on earnings and quarterly_earnings values                     |   |
|     Report results                   |  March 24 | March 27 |  2h    |                                                                        |   |
| Test cases – Group 2                 |  March 27 | March 27 |  1h    |  Focused on invalid tickers                                            |   |
|     Report results                   |  March 27 | March 27 |  2h    |                                                                        |   |
| Test cases – Group 3                 |  March 21 | March 24 |  1h    |  Focused on data testing                                               |   |
|     Report results                   |  March 24 | March 27 |  2h    |                                                                        |   |

<br>

  7.2   Deliverables                                                                              
| Deliverable                     | Date / Milestone |
|---------------------------------|------------------|
| Text document with team info    | March 28th       |
| GitHub fork with documentation: | March 21st       |
|      Test plan                  | March 24th       |
|      Test cases                 | March 24th       |
|      Test report                | March 27th       |
