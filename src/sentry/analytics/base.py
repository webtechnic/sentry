from __future__ import absolute_import


class Analytics(object):
    __all__ = ('record', 'validate')

    def record(self, event):
        """
        >>> record(Event())
        """

    def validate(self):
        """
        Validates the settings for this backend (i.e. such as proper connection
        info).

        Raise ``InvalidConfiguration`` if there is a configuration error.
        """
