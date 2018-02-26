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
    writeToLog(params['logFile'], 'TestCase', 'INFO', '1. Create new album without specifying Album ID and User ID')
    albumInfo = initAlbum()
    params.update(albumInfo)
    response = albumsCreate(params)
    if 'id' in response:
        result = responseCheck(albumInfo, response, params)
        if result:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Album ID ' + str(response['id']) + ' is created but not associated with any user.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '2. Create new album for existing user, let the system set album ID')
    albumInfo = initAlbum()
    userIdList = usersGetAll(params)
    albumInfo['userId'] = random.choice(userIdList)
    params.update(albumInfo)
    response = albumsCreate(params)
    if 'id' in response:
        result = responseCheck(albumInfo, response, params)
        if result:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Album ID ' + str(response['id']) + ' created for User ' + str(response['userId']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '3. Delete an existing album with no photo')
    # Use the previously created new album, which has no photo
    albumInfo[u'id'] = response['id']
    params.update(albumInfo)
    response = albumsDeleteByID(params)
    albumIdList = albumsGetAll(params)
    if response != None:
        if 'code' in response:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')
    else:
        if albumInfo['id'] in albumIdList:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Album ID ' + str(albumInfo['id']) + ' is not deleted. API did not return error.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Album ID ' + str(albumInfo['id']) + ' deleted.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '4. Create new album with specific ID, and the ID does not exist in system')
    # Use the previously deleted album
    if albumInfo['id'] not in albumIdList:
        response = albumsCreate(params)
        if 'id' in response:
            result = responseCheck(albumInfo, response, params)
            if result:
                writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Album ID ' + str(albumInfo['id']) + ' created.\n')
            else:
                writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
        elif 'code' in response:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '5. Create new album with specific ID, and the ID already exists in system')
    albumInfo = initAlbum()
    # Randomly pick an existing album
    albumIdList = albumsGetAll(params)
    albumInfo[u'id'] = random.choice(albumIdList)
    params.update(albumInfo)
    response = albumsCreate(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Album ID ' + str(albumInfo['id']) + ' already exists, but API did not return error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '6. Find an existing album with photos and return the list of photos')
    while True:
        albumInfo[u'id'] = random.choice(albumIdList)
        params.update(albumInfo)
        response = albumsGetAlbumPhotos(params)
        if len(response) != 0:
            break
    writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Album ID ' + str(albumInfo['id']) + ' has ' + str(len(response)) + ' photos: ' + str(response) +'.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '7. Delete an existing album with photos')
    response = albumsDeleteByID(params)
    if response != None:
        if 'code' in response:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Album ID ' + str(albumInfo['id']) + ' with photos cannot be deleted.\n')
    else:
        # Get the updated albumIdList
        albumIdList = albumsGetAll(params)
        if albumInfo['id'] in albumIdList:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Album ID ' + str(albumInfo['id']) + ' with photos is not deleted. API did not return error.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Album ID ' + str(albumInfo['id']) + ' with photos is deleted. API did not return error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '8. Get a non-existing album')
    albumIdList = albumsGetAll(params)
    albumInfo['id'] = max(albumIdList) + 1
    params.update(albumInfo)
    response = albumsGetOne(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    elif response == '':
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Cannot find Album ID ' + str(albumInfo['id']) + '. API did not return error.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Cannot find Album ID ' + str(albumInfo['id']) + '.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '9. Delete a non-existing album')
    # Use the previous album
    response = albumsDeleteByID(params)
    if response != None:
        if 'code' in response:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Cannot find Album ID ' + str(albumInfo['id']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '10. Update a non-existing album')
    response = albumsUpdate(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Album ID ' + str(albumInfo['id']) + ' does not exist. API did not return error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '11. Get an existing album')
    albumInfo[u'id'] = random.choice(albumIdList)
    params.update(albumInfo)
    response = albumsGetOne(params)
    if 'id' in response:
        writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Album ID ' + str(response['id']) + ' found.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '12. Update an existing album')
    albumInfo = initAlbum()
    albumInfo[u'id'] = random.choice(albumIdList)
    params.update(albumInfo)
    response = albumsUpdate(params)
    if 'id' in response:
        result = responseCheck(albumInfo, response, params)
        if result:
            writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Album ID ' + str(albumInfo['id']) + ' updated.\n')
        else:
            writeToLog(params['logFile'], 'TestCase', 'ERROR', 'Response check returned error.\n')
    elif 'code' in response:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned code ' + str(response['code']) + '.\n')
    else:
        writeToLog(params['logFile'], 'TestCase', 'ERROR', 'API call returned error.\n')


    #--------------------------#
    writeToLog(params['logFile'], 'TestCase', 'INFO', '13. Return a list of all albums, with the photos associated with those albums')
    params = readParams(configFile)
    params['logFile'] = logFile
    albumPhotos = []
    albumIdList = albumsGetAll(params)
    for album in albumIdList:
        params['id'] = album
        photoIdList = albumsGetAlbumPhotos(params)
        albumPhotos.append({'album': album, 'photoIdList': photoIdList})
    writeToLog(params['logFile'], 'TestCase', 'SUCCESS', 'Existing albums and photos: ' + str(albumPhotos) + '.\n')
