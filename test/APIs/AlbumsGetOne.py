#!/usr/bin/env python
# This script is for albums-controller getOne API
# Author: Rui Li
# Input: params
# Required parameters in params: baseURL, logFile

import sys, os, time, json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from Utils.Utils import writeToLog, apiCall

stepName = os.path.splitext(os.path.basename(__file__))[0]

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


if __name__ == '__main__':
    logFolder = os.path.dirname(__file__)
    #if not os.path.exists(logFolder):
    #    os.makedirs(logFolder)
    logFile = os.path.join(logFolder, stepName + '_' + time.strftime("%Y%m%d%H%M%S") + '.log')
    params = {
    'baseURL': 'http://10.27.18.140:8080/',
    'logFile': logFile,
    'id': 110
    }

    albumsGetOne(params)
