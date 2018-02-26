import sys, os, time, json, uuid, urllib, urllib2, random, string


def apiCall(url, method, body = {}, header = {}, content_type = ''):
    apiCallResult = {}
    startTime = time.time()

    # This is a DELETE
    if method == "DELETE":
        req = urllib2.Request(url)
        req.get_method = lambda: method
    # This is a POST
    elif body:
        if 'json' in content_type:
            params = json.dumps(body)
            header['Content-Type'] = 'application/json'
        else:
            params = urllib.urlencode(body)
        if header:
            req = urllib2.Request(url, data = params, headers = header)
        else:
            req = urllib2.Request(url, data = params)
    # This is a GET
    elif header:
        req = urllib2.Request(url, headers = header)
    else:
        req = urllib2.Request(url)

    try:
        apiCallResult['response'] = urllib2.urlopen(req)
        apiCallResult['responseTime'] = time.time() - startTime
        apiCallResult['errorCode'] = 0
        return apiCallResult
    except Exception, e:
        errorMessage = 'Error while calling url: ' + url
        if hasattr(e, 'code'):
            errorMessage += '\nError Code: ' + str(e.code)
        if hasattr(e, 'read'):
            errorMessage += '\nResponse: ' + str(e.read())
        apiCallResult['errorCode'] = 1
        apiCallResult['errorMessage'] = errorMessage
        return apiCallResult


'''
def getConfigFile():
    path = os.path.dirname(os.path.abspath(__file__))
    fileName = os.path.splitext(os.path.basename(__file__))[0]
    full_file = os.path.join(path, 'TestCases', file_name)
    return full_file
'''


'''
def initialTest(testCase, configFile):
    try:
        params = readParams(paramsFilePath)
        testId = uuid.uuid4().hex
        testName = os.path.splitext(os.path.basename(testCasePath))[0]
        logFolder = os.path.join(os.path.dirname(testCasePath), 'Results', testName)
        if not os.path.exists(logFolder):
            os.makedirs(logFolder)

        logFile = os.path.join(logFolder, testId + '.log')
        params['logFolder'] = logFolder
        params['logFile'] = logFile
        params['errorCode'] = 0
        params['testId'] = testId
    except Exception, e:
        params['errorCode'] = 1
        print 'Initialization failed' + str(e)
        writeToLog(params['logFile'], 'Test Initialization', 'ERROR', e = 'Initialization failed. ' + str(e))
    return params
'''


def initUser():
    name = "".join(random.choice(string.lowercase) for _ in range(4)) + " " + "".join(random.choice(string.lowercase) for _ in range(4))
    username = "".join(name.split())
    companyName = "".join(random.choice(string.lowercase) for _ in range(10))
    userInfo = {
    u"address": {
        u"street": unicode("".join(random.choice(string.digits) for _ in range(3)) + " " + "".join(random.choice(string.lowercase + string.whitespace) for _ in range(8))),
        u"suite": unicode("".join(random.choice(string.digits) for _ in range(3))),
        u"city": unicode("".join(random.choice(string.lowercase) for _ in range(8))),
        u"zipcode": unicode(random.randint(10000,99999)),
        u"geo": {
            u"lat": random.uniform(-180, 180),
            u"lng": random.uniform(-90, 90)
        }
    },
    u"company":{
        u"bs": unicode("".join(random.choice(string.lowercase) for _ in range(8))),
        u"catchPhrase": unicode("".join(random.choice(string.lowercase) for _ in range(16))),
        u"name": unicode(companyName)
    },
#    u"id": ,
    u"name": unicode(name),
    u"phone": unicode("".join(random.choice(string.digits) for _ in range(10))),
    u"username": unicode(username),
    u"email": unicode(username + "@" + companyName + ".com"),
    u"website": unicode(username + "." + companyName + ".com")
    }
    return userInfo


def initAlbum():
    albumInfo = {
#    u"id": ,
#    u"userId": ,
    u"title": unicode("".join(random.choice(string.lowercase) for _ in range(8)))
    }
    return albumInfo


def initPhoto():
    hexId = "".join(random.choice(string.lowercase + string.digits) for _ in range(6))
    photoInfo = {
#    u"id": ,
#    u"albumId": ,
    u"title": unicode("".join(random.choice(string.lowercase) for _ in range(16))),
    u"url": unicode("http://placehold.it/600/" + hexId),
    u"thumbnailUrl": unicode("http://placehold.it/150/" + hexId)
    }
    return photoInfo


def readParams(file_name):
    output = {}
    with open(file_name, 'r') as f:
        output = json.loads(f.read())
    return output


def responseCheck(request, response, params):
    passResponseCheck = True
    for key in request:
        if response[key] != request[key]:
            writeToLog(params['logFile'], 'responseCheck', 'ERROR', str(key) + ' value ' + str(response[key]) + ' in response does not match the value ' + str(request[key]) + ' in request.')
            passResponseCheck = False
    return passResponseCheck


def writeToLog(log_file, component='', level='', e=''):
    message = '[' + time.strftime("%m/%d/%Y %H:%M:%S") + ']' + '[' + component + ']' + '[' + level + ']' + e + '\n'
    with open(log_file, 'a') as f:
        f.write(message)
    print message
    return
