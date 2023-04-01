class Utils:
    """
    A static class that provides formatting utilities for various types of data.
    """

    @staticmethod
    def format_money(amount, currency="USD"):
        """
        Formats a given amount of money as a string with the currency code at the end.

        Args:
            amount: The amount of money to format.
            currency: The currency code to use (default is USD).

        Returns:
            A string representation of the formatted amount with the currency code at the end.
        """
        if not amount:
            return ''
        else:
            return '{:.2f} {}'.format(amount, currency)