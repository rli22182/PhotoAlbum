#!/usr/bin/env python
# This script is for photos-controller APIs
# Author: Rui Li
# Input: params

import sys, os, time, json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from Utils.Utils import writeToLog, apiCall

def photosCreate(params):
    result = {}
    url = params['baseURL'] + "api/photos"
    method = "POST"
    header = {'Content-Type':'application/json'}
    body = {
    "title": params['title'],
    "url": params['url'],
    "thumbnailUrl": params['thumbnailUrl']
    }
    # Set Photo ID if specified in params
    if 'id' in params:
        body[u'id'] = params['id']
    # Set Album ID if specified in params
    if 'albumId' in params:
        body[u'albumId'] = params['albumId']

    apiCallResult = apiCall(url, method, body, header, 'json')
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'photosCreate', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'photosCreate', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'photosCreate', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
#        writeToLog(params['logFile'], 'photosCreate', 'INFO', 'Photo ID ' + str(response_body['id']) + ' created for album ' + str(response_body['albumId']))
        return response_body


def photosDeleteByID(params):
    result = {}
    url = params['baseURL'] + "api/photos/" + str(params['id'])
    method = "DELETE"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'photosDeleteByID', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'photosDeleteByID', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'photosDeleteByID', 'ERROR', 'API response error')
        return result
#    else:
#        writeToLog(params['logFile'], 'photosDeleteByID', 'INFO', 'Photo ID ' + str(params['id']) + ' deleted.')


# This is not supported!!!
# "status":405,"error":"Method Not Allowed","exception":"org.springframework.web.HttpRequestMethodNotSupportedException","message":"Request method 'GET' not supported","path":"/api/photos"
def photosGetAll(params):
    result = {}
    url = params['baseURL'] + "api/photos"
    method = "GET"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'photosGetAll', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'photosGetAll', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'photosGetAll', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
#        total_user = len(response_body)
#        writeToLog(params['logFile'], 'albumsGetAll', 'INFO', 'There are ' + str(total_user) + ' albums.')
        photoIdList = []
        for photo in response_body:
            photoIdList.append(photo['id'])
        return photoIdList


def photosGetOne(params):
    result = {}
    url = params['baseURL'] + "api/photos/" + str(params['id'])
    method = "GET"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'photosGetOne', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'photosGetOne', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'photosGetOne', 'ERROR', 'API response error')
        return result
    elif data == '':
        return data
    else:
        response_body = json.loads(data)
#        writeToLog(params['logFile'], 'photosGetOne', 'INFO', 'Photo ID: ' + str(response_body['id']) + ', Album ID: ' + str(response_body['albumId']) + ', Photo Name: ' + str(response_body['title']) +'.')
        return response_body


def photosUpdate(params):
    result = {}
    url = params['baseURL'] + "api/photos"
    method = "PUT"
    header = {'Content-Type':'application/json'}
    body = {
    "id": params['id'],
    "albumId": params['albumId'],
    "title": params['title'],
    "url": params['url'],
    "thumbnailUrl": params['thumbnailUrl']
    }

    apiCallResult = apiCall(url, method, body, header, 'json')
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'photosUpdate', 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'photosUpdate', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'photosUpdate', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
#        writeToLog(params['logFile'], 'photosUpdate', 'INFO', 'Photo ID ' + str(response_body['id']) + ' updated for album ' + str(response_body['albumId']))
        return response_body
