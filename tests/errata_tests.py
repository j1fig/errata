from http import HTTPStatus
import json
import unittest

import errata


class ErrataTest(unittest.TestCase):

    def setUp(self):
        errata.app.testing = True
        self.c = errata.app.test_client()
        with errata.app.app_context():
            errata.clear_db()
            errata.init_db()

    def _public_api_request(self, method, url, *args, **kwargs):
        """
        Perform an API request.
        :param method: Method to use ('GET', 'POST' etc).
        :param url: Relative URL.
        """
        kwargs.setdefault('headers', {})
        kwargs['method'] = method
        res = self.c.open(url, *args, **kwargs)
        return res

    def _public_api_json_request(self, method, url, data, *args, **kwargs):
        """
        Perform an HTTP request with a JSON body payload.
        :param method: Method to use ('POST', 'PUT' etc).
        :param url: Relative URL.
        :param data: Dictionary containing data to send.
        """
        res = self._public_api_request(
            method,
            url,
            data=json.dumps(data),
            content_type='application/json',
            *args,
            **kwargs
        )
        return res


if __name__ == '__main__':
    unittest.main()
