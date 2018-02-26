#!/usr/bin/env python
#
# Author: Rui Li

import sys, os, time, json, string, random
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from Utils.Utils import *
from APIs.Users import *
from APIs.Albums import *
from APIs.Photos import *


if __name__ == '__main__':
    # Find and read config file
    testCaseFolder = os.path.dirname(__file__)
    testCaseName = os.path.splitext(os.path.basename(__file__))[0]
#    configFileName = testCaseName + '.ini'
    configFile = os.path.join(testCaseFolder, "config.json")
    params = readParams(configFile)

    # Set log file
    logFile = os.path.join(testCaseFolder, testCaseName + '_' + time.strftime("%Y%m%d%H%M%S") + '.log')
    params['logFile'] = logFile

    # Start Test Cases

    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '1. Create new user without specifying ID, let the system set user ID')
    userInfo = initUser()
    params.update(userInfo)
    response = usersCreate(params)
    if 'id' in response:
        result = responseCheck(userInfo, response, params)
        if result:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'User ID ' + str(response['id']) + ' created.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '2. Delete an existing user with no album')
    # Use the previously created new user, who has no albums
    userInfo[u'id'] = response['id']
    params.update(userInfo)
    response = usersDeleteByID(params)
    userIdList = usersGetAll(params)
    if response != None:
        if 'code' in response:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')
    else:
        if userInfo['id'] in userIdList:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'User ID ' + str(userInfo['id']) + ' is not deleted. API did not return error.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'User ID ' + str(userInfo['id']) + ' deleted.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '3. Create new user with specific ID, and the ID does not exist in system')
    # Use the previously deleted user
    if userInfo['id'] not in userIdList:
        response = usersCreate(params)
        if 'id' in response:
            result = responseCheck(userInfo, response, params)
            if result:
                writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'User ID ' + str(userInfo['id']) + ' created.\n')
            else:
                writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
        elif 'code' in response:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '4. Create new user with specific ID, and the ID already exists in system')
    userInfo = initUser()
    # Randomly pick an existing user
    userIdList = usersGetAll(params)
    userInfo[u'id'] = random.choice(userIdList)
    params.update(userInfo)
    response = usersCreate(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'User ID ' + str(userInfo['id']) + ' already exists, but API did not return error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '5. Find an existing user with albums')
    while True:
        userInfo[u'id'] = random.choice(userIdList)
        params.update(userInfo)
        response = usersGetUserAlbums(params)
        if len(response) != 0:
            break
    writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'User ID ' + str(userInfo['id']) + ' has ' + str(len(response)) + ' albums.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '6. Delete an existing user with albums')
    response = usersDeleteByID(params)
    if response != None:
        if 'code' in response:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'User ID ' + str(userInfo['id']) + ' with albums cannot be deleted.\n')
    else:
        # Get the updated userIdList
        userIdList = usersGetAll(params)
        if userInfo['id'] in userIdList:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'User ID ' + str(userInfo['id']) + ' with albums is not deleted. API did not return error.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'User ID ' + str(userInfo['id']) + ' with albums is deleted. API did not return error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '7. Get a non-existing user')
    userIdList = usersGetAll(params)
    userInfo['id'] = max(userIdList) + 1
    params.update(userInfo)
    response = usersGetOne(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Cannot find User ID ' + str(userInfo['id']) + '.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '8. Delete a non-existing user')
    # Use the previous user
    response = usersDeleteByID(params)
    if response != None:
        if 'code' in response:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Cannot find User ID ' + str(userInfo['id']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '9. Update a non-existing user')
    response = usersUpdate(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'User ID ' + str(userInfo['id']) + ' does not exist. API did not return error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '10. Get an existing user')
    userInfo[u'id'] = random.choice(userIdList)
    params.update(userInfo)
    response = usersGetOne(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'User ID ' + str(response['id']) + ' found.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '11. Update an existing user')
    userInfo = initUser()
    userInfo[u'id'] = random.choice(userIdList)
    params.update(userInfo)
    response = usersUpdate(params)
    if 'id' in response:
        result = responseCheck(userInfo, response, params)
        if result:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'User ID ' + str(userInfo['id']) + ' updated.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')
