from zope.interface import implements
from zope.component import getUtility
from interfaces import ISelectedChoice
from sparc.common import SPARCMessageFactory as _

class cliSelectedChoice(object):
    """Identify a selected choice"""
    implements(ISelectedChoice)
    
    @classmethod
    def selection(cls):
        """Returns selected choice"""
        return raw_input()

def askQuestion(question, required = True, answers = dict(), tries = 3):
    """Ask a question to STDOUT and return answer from STDIN
    
    Args:
        question: A string question that will be printed to stdout
    
    Kwargs:
        required: True indicates the question must be answered
        answers: A sequence of dicts with key value pairs where the key will
            be a user-selectable choice menu item with the value as its related
            description.
        tries: Integer value of maximum amount of attempts users may exercise
            to select a valid answer
    
    Returns:
        A user specified string when required is False and answers was not
        provided. A user selected key from answers when required is True and
        answers was provided.  None if required was false and user did not
        enter a answer.  None if required was True and user reached reached
        maximum limit of tries.
    """
    print question
    
    if not answers:
        # we get the user's answer via a named utility because direct calls to
        # raw_input() are hard to test (this way, tests can provide their own
        # implementation of ISelectedChoice without calls to raw_input())
        answer = getUtility(ISelectedChoice, 'sparc.common.cli_selected_choice').selection()
        _attempts = 0
        while True:
            if tries and _attempts > tries:
                print (u"Too many attempts")
                return None
            if not required or answer:
                return answer if answer else None
            print (u"Invalid input, please try again.")
            answer = getUtility(ISelectedChoice, 'sparc.common.cli_selected_choice').selection()
            _attempts += 1
    for selection_pair in answers:
        for key, potential_answer in selection_pair.iteritems():
            print "(" + key + ") " + potential_answer
            break # only process the first dict entry for the sequence
    _attempts = 0
    while True:
        answer = getUtility(ISelectedChoice, 'sparc.common.cli_selected_choice').selection()
        if tries and _attempts > tries:
            print _(u"Too many attempts")
            return None
        if not answer and not required:
            return None
        for selection_pair in answers:
            if answer in selection_pair:
                return answer
        print (u"Invalid selection: {}, please try again.".format(answer))
        answer = getUtility(ISelectedChoice, 'sparc.common.cli_selected_choice').selection()
        _attempts += 1

