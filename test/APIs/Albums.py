#!/usr/bin/env python
# This script is for albums-controller APIs
# Author: Rui Li
# Input: params

import sys, os, time, json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from Utils.Utils import writeToLog, apiCall

def albumsCreate(params):
    result = {}
    url = params['baseURL'] + "api/albums"
    method = "POST"
    header = {'Content-Type':'application/json'}
    body = {
    "title": params['title'],
    }
    # Set Album ID if specified in params
    if 'id' in params:
        body[u'id'] = params['id']
    # Set user ID if specified in params
    if 'userId' in params:
        body[u'userId'] = params['userId']

    apiCallResult = apiCall(url, method, body, header, 'json')
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'albumsCreate', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'albumsCreate', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'albumsCreate', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
        return response_body


def albumsDeleteByID(params):
    result = {}
    url = params['baseURL'] + "api/albums/" + str(params['id'])
    method = "DELETE"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'albumsDeleteByID', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'albumsDeleteByID', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'albumsDeleteByID', 'ERROR', 'API response error')
        return result
#    else:
#        writeToLog(params['logFile'], 'albumsDeleteByID', 'INFO', 'Album ID ' + str(params['id']) + ' deleted.')


def albumsGetAlbumPhotos(params):
    result = {}
    url = params['baseURL'] + "api/albums/" + str(params['id']) + '/photos'
    method = "GET"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'albumsGetAlbumPhotos', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'albumsGetAlbumPhotos', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'albumsGetAlbumPhotos', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
#        total_photos = len(response_body)
#        writeToLog(params['logFile'], 'albumsGetAlbumPhotos', 'INFO', 'Album ' + str(params['id']) + ' has ' + str(total_photos) + ' photos.')
        photoIdList = []
        for photo in response_body:
            photoIdList.append(photo['id'])
        return photoIdList


def albumsGetAll(params):
    result = {}
    url = params['baseURL'] + "api/albums"
    method = "GET"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'albumsGetAll', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'albumsGetAll', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'albumsGetAll', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
#        total_user = len(response_body)
#        writeToLog(params['logFile'], 'albumsGetAll', 'INFO', 'There are ' + str(total_user) + ' albums.')
        albumIdList = []
        for album in response_body:
            albumIdList.append(album['id'])
        return albumIdList


def albumsGetOne(params):
    result = {}
    url = params['baseURL'] + "api/albums/" + str(params['id'])
    method = "GET"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'albumsGetOne', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'albumsGetOne', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'albumsGetOne', 'ERROR', 'API response error')
        return result
    elif data == '':
        return data
    else:
        response_body = json.loads(data)
#        writeToLog(params['logFile'], 'albumsGetOne', 'INFO', 'Album ID: ' + str(response_body['id']) + ', Album Name: ' + str(response_body['title']) + ', User ID: ' + str(response_body['userId']) +'.')
        return response_body


def albumsUpdate(params):
    result = {}
    url = params['baseURL'] + "api/albums"
    method = "PUT"
    header = {'Content-Type':'application/json'}
    body = {
    "id": params['id'],
    "title": params['title'],
    "userId": params['userId']
    }

    apiCallResult = apiCall(url, method, body, header, 'json')
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'albumsUpdate', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'albumsUpdate', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'albumsUpdate', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
#        writeToLog(params['logFile'], 'albumsUpdate', 'INFO', 'Album ID ' + str(response_body['id']) + ' updated for user ' + str(response_body['userId']))
        return response_body
