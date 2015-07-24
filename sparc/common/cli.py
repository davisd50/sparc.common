def askQuestion(question, required = True, answers = dict(), tries = 3):
    """Ask a question and return answer
    
    Args:
        question: A string question that will be printed to stdout
    
    Kwargs:
        required: True indicates the question must be answered
        answers: a dictionary of potential answers with a related selection key.
            Potenial answers will be listed to stdout and user will be asked to
            select the key of the answer they wish to choose.
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
        answer = raw_input()
        _attempts = 0
        while True:
            if tries and _attempts > tries:
                print (u"Too many attempts")
                return None
            if not required or answer:
                return answer if answer else None
            print (u"Invalid input, please try again.")
            answer = raw_input()
            _attempts += 1
    
    answers = dict()
    for key, potential_answer in answers.iteritems():
        print "(" + key + ") " + potential_answer
    while True:
        answer = raw_input()
        _attempts = 0
        if tries and _attempts > tries:
            print _(u"Too many attempts")
            return None
        if not answer and not required:
            return None
        if answer in answers:
            return answer
        print (u"Invalid selection, please try again.")
        answer = raw_input()
        _attempts += 1

