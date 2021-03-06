from zope.interface import Interface
from zope.interface import Attribute


class ISelectedChoice(Interface):
    """Identify a selected choice"""
    def selection():
        """Returns selected choice"""

class ICallable(Interface):
    """Object that is callable"""
    def __call__(*args, **kwargs):
        """Call the object with optional arguments"""
