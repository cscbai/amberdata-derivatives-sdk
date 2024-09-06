# ======================================================================================================================

# pylint: disable=line-too-long, missing-class-docstring, missing-function-docstring, missing-module-docstring

import unittest

from tests.base_test_case import BaseTestCase
from tests.error_message import ErrorMessage


# ======================================================================================================================

class EndpointFuturesPerpetualsVolumesTestCase(BaseTestCase):
    # pylint: disable-next=arguments-differ
    def setUp(self):
        super().setUp(function_name='get_futures_perpetuals_volumes')

    # ==================================================================================================================

    def test_default(self):
        response = self.call_endpoint(asset='BTC')
        self.validate_response_schema(response, schema=self.schema)
        self.validate_response_200(response, min_elements=200)
        self.validate_response_field(response, 'underlying', 'BTC')

    def test_historical(self):
        response = self.call_endpoint(asset='BTC', startDate='2024-04-01T00:00:00', endDate='2024-05-01T00:00:00')
        self.validate_response_data(response)
        self.validate_response_schema(response, schema=self.schema)
        self.validate_response_200(response, num_elements=240)
        self.validate_response_field(response, 'underlying', 'BTC')

    def test_historical_timeformat_default(self):
        response = self.call_endpoint(asset='BTC', startDate='2024-04-01T00:00:00', endDate='2024-05-01T00:00:00')
        self.validate_response_data(response)
        self.validate_response_schema(response, schema=self.schema)
        self.validate_response_200(response, num_elements=240)
        self.validate_response_field(response, 'underlying', 'BTC')
        self.validate_response_field_timestamp(response, 'timestamp', is_milliseconds=True)

    def test_historical_timeformat_hr(self):
        response = self.call_endpoint(asset='BTC', startDate='2024-04-01T00:00:00', endDate='2024-05-01T00:00:00', timeFormat='hr')
        self.validate_response_data(response)
        self.validate_response_schema(response, schema=self.schema)
        self.validate_response_200(response, num_elements=240)
        self.validate_response_field(response, 'underlying', 'BTC')
        self.validate_response_field_timestamp(response, 'timestamp', is_hr=True, is_minutely=True)

    def test_historical_timeformat_iso(self):
        response = self.call_endpoint(asset='BTC', startDate='2024-04-01T00:00:00', endDate='2024-05-01T00:00:00', timeFormat='iso')
        self.validate_response_data(response)
        self.validate_response_schema(response, schema=self.schema)
        self.validate_response_200(response, num_elements=240)
        self.validate_response_field(response, 'underlying', 'BTC')
        self.validate_response_field_timestamp(response, 'timestamp', is_iso=True, is_minutely=True)

    def test_historical_timeframe_days(self):
        response = self.call_endpoint(asset='BTC', startDate='2024-04-01T00:00:00', endDate='2024-05-01T00:00:00', timeFormat='hr', timeFrame='7d')
        self.validate_response_data(response)
        self.validate_response_schema(response, schema=self.schema)
        self.validate_response_200(response, num_elements=40)
        self.validate_response_field(response, 'underlying', 'BTC')
        self.validate_response_field_timestamp(response, 'timestamp', is_hr=True, is_daily=True)

    def test_historical_timeframe_hours(self):
        response = self.call_endpoint(asset='BTC', startDate='2024-04-01T00:00:00', endDate='2024-05-01T00:00:00', timeFormat='hr', timeFrame='12h')
        self.validate_response_data(response)
        self.validate_response_schema(response, schema=self.schema)
        self.validate_response_200(response, num_elements=480)
        self.validate_response_field(response, 'underlying', 'BTC')
        self.validate_response_field_timestamp(response, 'timestamp', is_hr=True, is_hourly=True)

    # ==================================================================================================================

    def test_invalid_parameter(self):
        response = self.call_endpoint(asset='BTC', invalid='parameter')
        self.validate_response_data(response)
        self.validate_response_400(response, ErrorMessage.INVALID_PARAMETER)

    def test_invalid_timestamp(self):
        response = self.call_endpoint(asset='BTC', startDate='<timestamp>')
        self.validate_response_data(response)
        self.validate_response_400(response, ErrorMessage.INVALID_PARAMETER_TIMESTAMP)

    # TODO: this endpoint should return 404 instead
    def test_unknown_asset(self):
        response = self.call_endpoint(asset='<asset>')
        self.validate_response_data(response)
        self.validate_response_200(response, num_elements=0)


# ======================================================================================================================

if __name__ == '__main__':
    unittest.main()

# ======================================================================================================================
