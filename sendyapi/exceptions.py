# -*- coding: utf-8 -*-
class SendyException(Exception):
    """Base class for exceptions in Sendy module."""
    pass


class HttpRequestError(SendyException):
    """Exception raised for errors in the HTTP Response.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):

        # Call the base class constructor with the parameters it needs
        super(HttpRequestError, self).__init__(msg)
        self.msg = msg


class SubscriptionError(SendyException):
    """Exception raised for errors in the Subscription.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):

        # Call the base class constructor with the parameters it needs
        super(SubscriptionError, self).__init__(msg)
        self.msg = msg


class UnsubscriptionError(SendyException):
    """Exception raised for errors in the Unsubscription.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):

        # Call the base class constructor with the parameters it needs
        super(UnsubscriptionError, self).__init__(msg)
        self.msg = msg


class SubscriberCountError(SendyException):
    """Exception raised for errors in the Subscriber Count.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):

        # Call the base class constructor with the parameters it needs
        super(SubscriberCountError, self).__init__(msg)
        self.msg = msg
