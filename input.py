import random
import utils

def fillInput(max, mandatory, multiple, minAnwsers, maxAnswers):
    ''' Range for checkboxes (multiple choice)
        For 3 checkboxes:
        - With at least 1, 2 or all checked:        checkbox(1, 3) or checkbox(max=3)
        - With none of them, 1, 2, or all checked:  checkbox(0, 3)
    '''
    min = 1
    max += 1 # make inclusive to be more logical
    if not mandatory:
        min = 0 # allow no answer
    if not multiple and maxAnswers != 0:
        print("Warning: since multiple responses are disabled for this question, maxAnswers is gonna be 0 anyway")
    if minAnwsers == 0:
        minAnwsers = 1
    if maxAnswers == 0:
        maxAnswers = max
    if multiple:
        maxAnswers += 1
        res = set() # avoid duplicate
        utils.checkMinMax(min, max)
        if (minAnwsers + 1 == maxAnswers): # exact number of answers
            loop = maxAnswers
            minAnwsers = 1
        else:
            loop = random.randrange(minAnwsers + 1, maxAnswers + 1)
        for i in range(minAnwsers, loop): #inclusive
            rand = str(random.randrange(min, max))
            while rand in res:
                rand = str(random.randrange(min, max))
            res.add(rand)
        return list(res) # convert set to list
    else:
        res = []
        utils.checkMinMax(min, max)
        rand = str(random.randrange(min, max))
        res.append(rand) # avoid splitting double digits
        return list(res)

def checkbox(max=2, mandatory=True, multiple=False, minAnwsers=0, maxAnswers=0):
    return fillInput(max, mandatory, multiple, minAnwsers, maxAnswers)

def postit(max=2, mandatory=True, multiple=False, minAnwsers=0, maxAnswers=0):
    return fillInput(max, mandatory, multiple, minAnwsers, maxAnswers) # list = await sequence

def smiley(max=2, mandatory=True):
    return fillInput(max, mandatory)

def images(max=2, mandatory=True, multiple=False, minAnwsers=0, maxAnswers=0):
    return fillInput(max, mandatory, multiple, minAnwsers, maxAnswers)

def dropdown(max=2, mandatory=True):
    return fillInput(max, mandatory)

def graduated(max=2, mandatory=True):
    return fillInput(max, mandatory)

def stars(max=2, mandatory=True):
    return fillInput(max, mandatory)

def ranking(max=2, mandatory=True, multiple=False, minAnwsers=0, maxAnswers=0):
    return utils.listToStrWithComas((fillInput(max, mandatory, multiple, minAnwsers, maxAnswers)))

def imageRanking(max=2, mandatory=True, multiple=False, minAnwsers=0, maxAnswers=0):
    return fillInput(max, mandatory, multiple, minAnwsers, maxAnswers)

def dragAndDrop(max=2, mandatory=True, multiple=False, minAnwsers=0, maxAnswers=0):
    return fillInput(max, mandatory, multiple, minAnwsers, maxAnswers)

def imageDragAndDrop(max=2, mandatory=True, multiple=False, minAnwsers=0, maxAnswers=0):
    return fillInput(max, mandatory, multiple, minAnwsers, maxAnswers)

def number(min=0, max=1, positive=True, negative=False):
    ''' Range for number input (single choice)
        utils.checkMinMax will check if max and min are positive, negative and both
        0 count as a positive number
    '''
    max += 1 # make inclusive to be more logical
    utils.checkMinMax(min, max, positive, negative)
    # decimal to do
    return str(random.randrange(min, max))

def text(min=1, max=2, textlist=None):
    ''' Range for text input (single or multiple words)
        To enable the none outcome (no words): text(list, 0, ...)
        It will not duplicate a word
    '''
    max += 1
    res = []
    utils.checkMinMax(min, max)
    for i in range(0, random.randrange(min, max)): # number of words to be inserted
        elem = random.choice(textlist)
        res.append(elem)
        textlist.remove(elem)
    return utils.listToStrWithComas(res)

def email(min=1, max=2, emailList=None):
    utils.checkEmailList(emailList)
    return  text(min, max, emailList)

def code(min=1, max=2, codeList=None):
    return text(min, max, codeList)

def datetime():
    # todo
    return

def draggable(min=1, max=2, nbchoice=None):
    ''' Range for text input (single or multiple words)
        To drag all choice (ie: 7 draggable elements): draggable(1, 7, 7)
        To enable the none choice outcome: draggable(0, ..., ...)
    '''
    max += 1
    res = []
    utils.checkMinMax(min, max)
    if max > nbchoice + 1:
        print('Error: Draggable max values has to be lower than the number of choice')
        exit(1)
    draglist = list(range(1, nbchoice + 1)) # create list from 0 to nbchoice, needed to avoid duplicate
    for i in range(0, random.randrange(min, max)): # number of element to drag
        elem = random.choice(draglist)
        res.append(elem)
        draglist.remove(elem)
    return utils.listToStrWithComas(res)
