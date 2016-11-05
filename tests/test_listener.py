import unittest
from unittest import mock

from betfairlightweight.streaming.listener import BaseListener, StreamListener


class BaseListenerTest(unittest.TestCase):

    def setUp(self):
        self.base_listener = BaseListener()

    def test_init(self):
        assert self.base_listener.market_stream is None
        assert self.base_listener.order_stream is None

    @mock.patch('betfairlightweight.streaming.listener.BaseListener._add_stream', return_value=123)
    @mock.patch('sys.stdout')
    def test_register_stream(self, mock_print, mock_add_stream):
        self.base_listener.register_stream(1, 'authentication')

        self.base_listener.register_stream(2, 'marketSubscription')
        mock_add_stream.assert_called_with(2, 'marketSubscription')
        assert self.base_listener.market_stream == 123

        self.base_listener.market_stream = 'test'
        self.base_listener.register_stream(2, 'marketSubscription')
        mock_add_stream.assert_called_with(2, 'marketSubscription')
        assert self.base_listener.market_stream == 123

        self.base_listener.register_stream(3, 'orderSubscription')
        mock_add_stream.assert_called_with(3, 'orderSubscription')
        assert self.base_listener.order_stream == 123

        self.base_listener.order_stream = 'test'
        self.base_listener.register_stream(3, 'orderSubscription')
        mock_add_stream.assert_called_with(3, 'orderSubscription')
        assert self.base_listener.order_stream == 123

    @mock.patch('sys.stdout')
    def test_on_data(self, mock_print):
        self.base_listener.on_data({})

    @mock.patch('sys.stdout')
    def test_add_stream(self, mock_print):
        self.base_listener._add_stream(1, 'operation')

    def test_str(self):
        assert str(self.base_listener) == '<BaseListener>'

    def test_repr(self):
        assert repr(self.base_listener) == '<BaseListener>'


class StreamListenerTest(unittest.TestCase):

    def setUp(self):
        self.output_queue = mock.Mock()
        self.stream_listener = StreamListener(self.output_queue)

    def test_init(self):
        assert self.stream_listener.output_queue == self.output_queue

    def test_register_stream(self):
        pass

    def test_on_data(self):
        pass

    def test_on_connection(self):
        self.stream_listener._on_connection({'connectionId': 1234}, 1)
        assert self.stream_listener.connection_id == 1234

    def test_on_status(self):
        self.stream_listener._on_status({}, 1)

    def test_on_change_message(self):
        pass

    def test_add_stream(self):
        pass

    def test_error_handler(self):
        pass

    def test_str(self):
        assert str(self.stream_listener) == '<StreamListener>'

    def test_repr(self):
        assert repr(self.stream_listener) == '<StreamListener>'
