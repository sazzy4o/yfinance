'''
Module for testings earnings property
'''

import unittest
import yfinance as yf

from unittest import mock
from pathlib import Path

from mock import get_mocked_get_json

# Mocks based on https://stackoverflow.com/a/28507806/3558475
data_path = Path(__file__).parent/'data'

url_map0 ={
  'https://finance.yahoo.com/quote/GOOG/financials': 'goog_financials.json'
}

class TestEarnings(unittest.TestCase):
  '''
  Class for testings earnings property
  '''
  @mock.patch('yfinance.utils.get_json',
    side_effect=get_mocked_get_json(url_map0)
  )
  def test_mock(self,mock_get_json):
    goog = yf.Ticker('GOOG')

    earnings = goog.earnings

    earning_2017 = earnings['Earnings'].iloc[0]

    self.assertEqual(earning_2017,12662000000)

    self.assertEqual(len(mock_get_json.call_args_list), 2)


if __name__ == '__main__':
  unittest.main()
