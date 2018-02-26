#!/usr/bin/env python
# This script is for albums-controller getAlbumPhotos API
# Author: Rui Li
# Input: params
# Required parameters in params: baseURL, logFile

import sys, os, time, json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from Utils.Utils import writeToLog, apiCall

stepName = os.path.splitext(os.path.basename(__file__))[0]

def albumsGetAlbumPhotos(params):
    startTime = time.time()
    result = {}
    url = params['baseURL'] + "api/albums/" + str(params['id']) + '/photos'
    method = "GET"
    apiCallResult = apiCall(url, method)
    if apiCallResult['errorCode'] == 0:
        data = apiCallResult['response'].read()
        code = apiCallResult['response'].getcode()
        result['errorCode'] = 0
        result['responseTime'] = apiCallResult['responseTime']
        writeToLog(params['logFile'], stepName, 'INFO', 'Call API Succeeded')
    else:
        result['errorCode'] = 1
        result['errorMessage'] = apiCallResult['errorMessage']
        writeToLog(params['logFile'], stepName, 'ERROR', 'Call API failed\n' + result['errorMessage'])
        return result
    if code != 200:
        result['errorCode'] = 1
        writeToLog(params['logFile'], stepName, 'ERROR', 'API response error')
        return result
    else:
        response_body = json.loads(data)
        total_photos = len(response_body)
        writeToLog(params['logFile'], stepName, 'INFO', 'Album ' + str(params['id']) + ' has ' + str(total_photos) + ' photos.')


if __name__ == '__main__':
    logFolder = os.path.dirname(__file__)
    #if not os.path.exists(logFolder):
    #    os.makedirs(logFolder)
    logFile = os.path.join(logFolder, stepName + '_' + time.strftime("%Y%m%d%H%M%S") + '.log')
    params = {
    'baseURL': 'http://10.27.18.140:8080/',
    'logFile': logFile,
    'id': 1
    }

    albumsGetAlbumPhotos(params)
