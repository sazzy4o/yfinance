'''
Module for testings earnings property
'''

import unittest
import yfinance as yf

from unittest import mock
from pathlib import Path

from mock import get_mocked_get_json

# Mock based on https://stackoverflow.com/a/28507806/3558475:
data_path = Path(__file__).parent/'data'

url_map ={
  # Protects againt tests failing because company is defunct
  'https://finance.yahoo.com/quote/GOOG':'fake_quote.json',
  'https://finance.yahoo.com/quote/ABNB':'fake_quote.json',
  'https://finance.yahoo.com/quote/ZERO':'fake_quote.json',

  'https://finance.yahoo.com/quote/GOOG/financials':'goog_financials.json',
  'https://finance.yahoo.com/quote/ABNB/financials':'abnb_financials.json',
  'https://finance.yahoo.com/quote/ZERO/financials':'zero_fake_financials.json'
}

class TestEarnings(unittest.TestCase):
  '''
  Class for testings earnings property
  '''
  @mock.patch('yfinance.utils.get_json',
    side_effect=get_mocked_get_json(url_map)
  )
  def test_positive_earnings(self,mock_get_json):
    '''
    Test positive earnings
    '''
    goog = yf.Ticker('GOOG')

    earnings = goog.earnings

    earnings_2017, earnings_2018, earnings_2019, earning_2020 = list(
        earnings['Earnings']
    )

    self.assertEqual(earnings_2017,12_662_000_000)
    self.assertEqual(earnings_2018,30_736_000_000)
    self.assertEqual(earnings_2019,34_343_000_000)
    self.assertEqual(earning_2020,40_269_000_000)

    self.assertEqual(len(mock_get_json.call_args_list), 2)

  @mock.patch('yfinance.utils.get_json',
    side_effect=get_mocked_get_json(url_map)
  )
  def test_positive_quarterly_earnings(self,mock_get_json):
    '''
    Test positive quarterly earnings
    '''
    goog = yf.Ticker('GOOG')

    quarterly_earnings = goog.quarterly_earnings

    earnings_q1, earnings_q2, earnings_q3, earning_q4 = list(
        quarterly_earnings['Earnings']
    )

    self.assertEqual(earnings_q1,6_836_000_000)
    self.assertEqual(earnings_q2,6_959_000_000)
    self.assertEqual(earnings_q3,11_247_000_000)
    self.assertEqual(earning_q4,15_227_000_000)

    self.assertEqual(len(mock_get_json.call_args_list), 2)

  @mock.patch('yfinance.utils.get_json',
    side_effect=get_mocked_get_json(url_map)
  )
  def test_negative_earnings(self,mock_get_json):
    '''
    Test negative earnings
    '''
    abnb = yf.Ticker('ABNB')

    earnings = abnb.earnings

    earnings_2017, earnings_2018, earnings_2019, earning_2020 = list(
        earnings['Earnings']
    )

    self.assertEqual(earnings_2017,-70_046_000)
    self.assertEqual(earnings_2018,-16_860_000)
    self.assertEqual(earnings_2019,-674_339_000)
    self.assertEqual(earning_2020,-4_584_716_000)

    self.assertEqual(len(mock_get_json.call_args_list), 2)

  @mock.patch('yfinance.utils.get_json',
    side_effect=get_mocked_get_json(url_map)
  )
  def test_negative_quarterly_earnings(self,mock_get_json):
    '''
    Test negative quarterly earnings
    '''
    abnb = yf.Ticker('ABNB')

    quarterly_earnings = abnb.quarterly_earnings

    earnings_q1, earnings_q2, earnings_q3, earning_q4 = list(
        quarterly_earnings['Earnings']
    )

    self.assertEqual(earnings_q1,266_650_000)
    self.assertEqual(earnings_q2,-351_538_000)
    self.assertEqual(earnings_q3,219_328_000)
    self.assertEqual(earning_q4,-3_887_851_000)

    self.assertEqual(len(mock_get_json.call_args_list), 2)

  @mock.patch('yfinance.utils.get_json',
    side_effect=get_mocked_get_json(url_map)
  )
  def test_zero_earnings(self,mock_get_json):
    '''
    Test zero earnings
    '''
    zero = yf.Ticker('ZERO')

    earnings = zero.earnings

    earnings_2017, earnings_2018, earnings_2019, earning_2020 = list(
        earnings['Earnings']
    )

    self.assertEqual(earnings_2017,0)
    self.assertEqual(earnings_2018,0)
    self.assertEqual(earnings_2019,0)
    self.assertEqual(earning_2020,0)

    self.assertEqual(len(mock_get_json.call_args_list), 2)

  @mock.patch('yfinance.utils.get_json',
    side_effect=get_mocked_get_json(url_map)
  )
  def test_zero_quarterly_earnings(self,mock_get_json):
    '''
    Test zero quarterly earnings
    '''
    zero = yf.Ticker('ZERO')

    quarterly_earnings = zero.quarterly_earnings

    earnings_q1, earnings_q2, earnings_q3, earning_q4 = list(
        quarterly_earnings['Earnings']
    )

    self.assertEqual(earnings_q1,0)
    self.assertEqual(earnings_q2,0)
    self.assertEqual(earnings_q3,0)
    self.assertEqual(earning_q4,0)

    self.assertEqual(len(mock_get_json.call_args_list), 2)

if __name__ == '__main__':
  unittest.main()
