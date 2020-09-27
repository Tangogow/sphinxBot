# Disable every delay and only fill one survey, testing purpose
debug = False

# Enable HTML debug print
debugHTML = False

# Link url (the one with sphinx-campus.com/d/s/...)
url = 'https://sphinx-campus.com/d/s/94zqtg'

# Number of fake survey to submit
loopMax = 200

''' Range of seconds to answer the survey
will choose randomly between the 2 values
Otherwise it will look like the survey was done in 0 sec, so not so legit '''
answerMin = 80
answerMax = 150

'''Range of minutes between each survey filling
will choose randomly between the 2 values
Otherwise it will look like all the survey answers where done at the same time, not so legit also '''
surveyMin = 1
surveyMax = 2
