#!/usr/bin/env python
# This script is for users-controller APIs
# Author: Rui Li
# Input: params

import sys, os, time, json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from Utils.Utils import writeToLog, apiCall

def usersCreate(params):
    result = {}
    url = params['baseURL'] + "api/users"
    method = "POST"
    header = {'Content-Type':'application/json'}
    body = {
    u"address": params['address'],
    u"company": params['company'],
    u"email": params['email'],
    u"name": params['name'],
    u"phone": params['phone'],
    u"username": params['username'],
    u"website": params['website']
    }
    # Set user ID if specified in params
    if 'id' in params:
        body[u'id'] = params['id']

    apiCallResult = apiCall(url, method, body, header, 'json')
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'usersCreate', 'SUCCESS', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'usersCreate', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'usersCreate', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
        return response_body


def usersDeleteByID(params):
    result = {}
    url = params['baseURL'] + "api/users/" + str(params['id'])
    method = "DELETE"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'usersDeleteByID', 'SUCCESS', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'usersDeleteByID', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'usersDeleteByID', 'ERROR', 'API response error')
        return result
#    else:
#        response_body = json.loads(data)
#        writeToLog(params['logFile'], 'usersDeleteByID', 'SUCCESS', 'User ID ' + str(params['id']) + ' deleted.')
#        return response_body


def usersGetAll(params):
    result = {}
    url = params['baseURL'] + "api/users"
    method = "GET"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'usersGetAll', 'SUCCESS', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'usersGetAll', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'usersGetAll', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
        #total_user = len(response_body)
        #writeToLog(params['logFile'], 'usersGetAll', 'SUCCESS', 'There are ' + str(total_user) + ' users.')
        userIdList = []
        for user in response_body:
            userIdList.append(user['id'])
        return userIdList


def usersGetOne(params):
    result = {}
    url = params['baseURL'] + "api/users/" + str(params['id'])
    method = "GET"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'usersGetOne', 'SUCCESS', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'usersGetOne', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'usersGetOne', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
        #writeToLog(params['logFile'], 'usersGetOne', 'SUCCESS', 'User ID ' + str(response_body['id']) + ' Info: ' + str(response_body) +'.')
        return response_body


def usersGetUserAlbums(params):
    result = {}
    url = params['baseURL'] + "api/users/" + str(params['id']) + '/albums'
    method = "GET"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        #writeToLog(params['logFile'], 'usersGetUserAlbums', 'SUCCESS', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'usersGetUserAlbums', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'usersGetUserAlbums', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
#        total_albums = len(response_body)
#        writeToLog(params['logFile'], 'usersGetUserAlbums', 'SUCCESS', 'User ' + str(params['id']) + ' has ' + str(total_albums) + ' albums.')
        albumIdList = []
        for album in response_body:
            albumIdList.append(album['id'])
        return albumIdList


def usersUpdate(params):
    result = {}
    url = params['baseURL'] + "api/users"
    method = "PUT"
    header = {'Content-Type':'application/json'}
    body = {
    u"address": params['address'],
    u"company": params['company'],
    u"email": params['email'],
    u"id": params['id'],
    u"name": params['name'],
    u"phone": params['phone'],
    u"username": params['username'],
    u"website": params['website']
    }

    apiCallResult = apiCall(url, method, body, header, 'json')
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['code'] = code
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], 'usersUpdate', 'SUCCESS', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], 'usersUpdate', 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], 'usersUpdate', 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
        #writeToLog(params['logFile'], 'usersUpdate', 'SUCCESS', 'User ID ' + str(params['id']) + ' updated. New User Info: ' + str(response_body))
        return response_body
