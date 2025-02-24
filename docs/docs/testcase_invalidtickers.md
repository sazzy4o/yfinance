# Test Case Document

**Purpose:** Prevent errors with:

    1. Invalid ticketer
    2. Invalid company

**Test Run Information:** 

**Tester Names:** Cameron and Ryan

**Date(s) of Test:** March 27, 2021

**Prerequisites for this test:** None

**Software Versions:**

	Current version of yfinance
	python 3

**Required Configuration:**

**Notes and Results:**


<table>
  <tr>
  <td><b>Step</b>
   </td>
   <td><b>Test Step/Input</b>
   </td>
   <td><b>Expected Results</b>
   </td>
   <td><b>Actual Results</b>
   </td>
   <td><b>Requirements Validation</b>
   </td>
   <td><b>Pass/Fail</b>
   </td>
  </tr>
  <tr>
   <td colspan="6" >User Flow 1: Testing empty string
   </td>
  </tr>
  <tr>
   <td>Create Ticker
   </td>
   <td>Ticker(‘’)
   </td>
   <td>Ticker created
   </td>
   <td>Ticker created
   </td>
   <td>
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Get earnings
   </td>
   <td>Ticker.earnings
   </td>
   <td>Return error
   </td>
   <td>HTTPError
   </td>
   <td>Can't use an empty string for a ticker
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td colspan="6" >User Flow 2: Testing debunk company
   </td>
  </tr>
  <tr>
   <td>Create Ticker
   </td>
   <td>Ticker(‘LEHLQ’)
   </td>
   <td>Ticker created
   </td>
   <td>Ticker created
   </td>
   <td>
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Get earnings
   </td>
   <td>Ticker.earnings
   </td>
   <td>Return error
   </td>
   <td>KeyError
   </td>
   <td>Can't research debunct companies
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td colspan="6" >User Flow 3: Misspelled company (GOOE vs GOOG)
   </td>
  </tr>
  <tr>
   <td>Create Ticker
   </td>
   <td>Ticker(‘GOOE’)
   </td>
   <td>Ticker created
   </td>
   <td>Ticker created
   </td>
   <td>
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Get earnings
   </td>
   <td>Ticker.earnings
   </td>
   <td>Return error
   </td>
   <td>KeyError
   </td>
   <td>Does not allow spelling mistakes
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td colspan="6" >User Flow 4: White Space
   </td>
  </tr>
  <tr>
   <td>Create Ticker
   </td>
   <td>Ticker(‘ ’)
   </td>
   <td>Ticker created
   </td>
   <td>Ticker created
   </td>
   <td>
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Get earnings
   </td>
   <td>Ticker.earnings
   </td>
   <td>Return error
   </td>
   <td>InvalidURL
   </td>
   <td>Can't use white space
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td colspan="6" >User Flow 5: Numbers
   </td>
  </tr>
  <tr>
   <td>Create Ticker
   </td>
   <td>Ticker(‘123’)
   </td>
   <td>Ticker created
   </td>
   <td>Ticker created
   </td>
   <td>
   </td>
   <td>Pass
   </td>
  </tr>
  <tr>
   <td>Get earnings
   </td>
   <td>Ticker.earnings
   </td>
   <td>Return error
   </td>
   <td>KeyError
   </td>
   <td>Can not use numbers
   </td>
   <td>Pass
   </td>
  </tr>
</table>

