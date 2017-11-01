# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from stripe import CardError, StripeError, six
from tests.helper import StripeTestCase


class StripeErrorTests(StripeTestCase):

    def test_formatting(self):
        err = StripeError(u'öre')
        self.assertEqual(u'öre', six.text_type(err))
        if six.PY2:
            self.assertEqual('\xc3\xb6re', str(err))
        else:
            self.assertEqual(u'öre', str(err))

    def test_formatting_with_request_id(self):
        err = StripeError(u'öre', headers={'request-id': '123'})
        self.assertEqual(u'Request 123: öre', six.text_type(err))
        if six.PY2:
            self.assertEqual('Request 123: \xc3\xb6re', str(err))
        else:
            self.assertEqual(u'Request 123: öre', str(err))

    def test_formatting_with_message_none_and_request_id(self):
        err = StripeError(None, headers={'request-id': '123'})
        self.assertEqual(u'Request 123: <empty message>', six.text_type(err))
        if six.PY2:
            self.assertEqual('Request 123: <empty message>', str(err))
        else:
            self.assertEqual('Request 123: <empty message>', str(err))

    def test_formatting_with_message_none_and_request_id_none(self):
        err = StripeError(None)
        self.assertEqual(u'<empty message>', six.text_type(err))
        if six.PY2:
            self.assertEqual('<empty message>', str(err))
        else:
            self.assertEqual('<empty message>', str(err))

    def test_repr(self):
        err = StripeError(u'öre', headers={'request-id': '123'})
        if six.PY2:
            self.assertEquals(repr(err), (
                "StripeError(message=u'\\xf6re', http_status=None, "
                "request_id='123')"))
        else:
            self.assertEquals(repr(err), (
                "StripeError(message='öre', http_status=None, "
                "request_id='123')"))


class StripeErrorWithParamCodeTests(StripeTestCase):

    def test_repr(self):
        err = CardError(u'öre', param='cparam', code='ccode', http_status=403,
                        headers={'request-id': '123'})
        if six.PY2:
            self.assertEquals(repr(err), (
                "CardError(message=u'\\xf6re', param='cparam', code='ccode', "
                "http_status=403, request_id='123')"))
        else:
            self.assertEquals(repr(err), (
                "CardError(message='öre', param='cparam', code='ccode', "
                "http_status=403, request_id='123')"))
