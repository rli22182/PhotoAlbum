#!/usr/bin/env python
# This script is for users-controller save API
# Author: Rui Li
# Input: params
# Required parameters in params: baseURL, logFile

import sys, os, time, json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from Utils.Utils import writeToLog, apiCall

stepName = os.path.splitext(os.path.basename(__file__))[0]

def usersCreate(params):
    startTime = time.time()
    result = {}
    url = params['baseURL'] + "api/users"
    method = "POST"
    header = {'Content-Type':'application/json'}
    body = {
    "address": {
        "street": params['street'],
        "suite": params['suite'],
        "city": params['city'],
        "zipcode": params['zipcode'],
        "geo": {
            "lat": params['latitude'],
            "lng": params['longitude']
        }
    },
    "company":{
        "bs": params['bs'],
        "catchPhrase": params['catchPhrase'],
        "name": params['companyName']
    },
    "email": params['email'],
    #"id": params['id'],
    "name": params['name'],
    "phone": params['phone'],
    "username": params['username'],
    "website": params['website']
    }

    apiCallResult = apiCall(url, method, body, header, 'json')
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
        print response_body
        writeToLog(params['logFile'], stepName, 'INFO', 'User ID ' + str(response_body['id']) + ' created.')


if __name__ == '__main__':
    logFolder = os.path.dirname(__file__)
    #if not os.path.exists(logFolder):
    #    os.makedirs(logFolder)
    logFile = os.path.join(logFolder, stepName + '_' + time.strftime("%Y%m%d%H%M%S") + '.log')
    params = {
    'baseURL': 'http://10.27.18.140:8080/',
    'logFile': logFile,
    'street': 'street',
    'suite': 'suite',
    'city': 'city',
    'zipcode': 'zipcode',
    'latitude': 38.914993,
    'longitude': -77.220455,
    'bs': 'bs',
    'catchPhrase': 'catchPhrase',
    'companyName': 'companyName',
    'email': 'email',
    #'id': 11,
    'name': 'name',
    'phone': 'phone',
    'username': 'username',
    'website': 'website'
    }

    usersCreate(params)
