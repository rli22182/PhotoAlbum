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
    writeToLog(params['logFile'], 'TestCase', 'INFO', '1. Get all photos')
    response = photosGetAll(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'There are ' + str(len(response)) + ' photos.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '2. Create new photo without specifying Photo ID and Album ID')
    photoInfo = initPhoto()
    params.update(photoInfo)
    response = photosCreate(params)
    if 'id' in response:
        result = responseCheck(photoInfo, response, params)
        if result:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Photo ID ' + str(response['id']) + ' is created but not associated with any album.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '3. Create new photo for existing album, let the system set Photo ID')
    photoInfo = initPhoto()
    albumIdList = albumsGetAll(params)
    photoInfo['albumId'] = random.choice(albumIdList)
    params.update(photoInfo)
    response = photosCreate(params)
    if 'id' in response:
        result = responseCheck(photoInfo, response, params)
        if result:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Photo ID ' + str(response['id']) + ' created for Album ' + str(response['albumId']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '4. Delete an existing photo')
    # Use the previously created new photo
    albumParams = params
    albumParams['id'] = response['albumId']
    photoInfo[u'id'] = response['id']
    params.update(photoInfo)
    response = photosDeleteByID(params)
    photoIdList = albumsGetAlbumPhotos(albumParams)
    if response != None:
        if 'code' in response:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')
    else:
        if photoInfo['id'] in photoIdList:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Photo ID ' + str(photoInfo['id']) + ' is not deleted. API did not return error.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Photo ID ' + str(photoInfo['id']) + ' deleted.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '5. Get a non-existing photo')
    response = photosGetOne(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Photo ID ' + str(photoInfo['id']) + ' is not deleted.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    elif response == '':
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Cannot find Photo ID ' + str(photoInfo['id']) + '. API did not return error.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Cannot find Photo ID ' + str(photoInfo['id']) + '.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '6. Delete a non-existing photo')
    # Use the previous photo
    response = photosDeleteByID(params)
    if response != None:
        if 'code' in response:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Cannot find Photo ID ' + str(photoInfo['id']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '7. Update a non-existing photo')
    response = photosUpdate(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Photo ID ' + str(photoInfo['id']) + ' does not exist. API did not return error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '8. Create new photo with specific ID, and the ID does not exist in system')
    # Use the previously deleted photo
    response = photosCreate(params)
    if 'id' in response:
        result = responseCheck(photoInfo, response, params)
        if result:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Photo ID ' + str(photoInfo['id']) + ' created.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '9. Create new photo with specific ID, and the ID already exists in system')
    photoInfo = initPhoto()
    # Use the previously created photo
    photoInfo[u'id'] = response['id']
    params.update(photoInfo)
    response = photosCreate(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Photo ID ' + str(photoInfo['id']) + ' already exists, but API did not return error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '10. Get an existing photo')
    response = photosGetOne(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Photo ID ' + str(response['id']) + ' found.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '11. Update an existing photo')
    photoInfo = initPhoto()
    photoInfo[u'id'] = response['id']
    params.update(photoInfo)
    response = photosUpdate(params)
    if 'id' in response:
        result = responseCheck(photoInfo, response, params)
        if result:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Photo ID ' + str(photoInfo['id']) + ' updated.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')
