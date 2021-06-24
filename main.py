#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: MitsuhaYuki
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get('/')
def get_main():
    return {'status': 200, 'msg': 'emby validation server successfully start'}


@app.get('/admin/service/registration/validateDevice')
@app.post('/admin/service/registration/validateDevice')
def post_validate_device():
    return {"cacheExpirationDays": 365, "message": "Device Valid", "resultCode": "GOOD"}


@app.get('/admin/service/registration/validate')
@app.post('/admin/service/registration/validate')
def post_validate():
    return {"featId": "", "registered": True, "expDate": "2099-01-01", "key": ""}


@app.get('/admin/service/registration/getStatus')
@app.post('/admin/service/registration/getStatus')
def post_get_status():
    return {"deviceStatus": "0", "planType": "Lifetime", "subscriptions": {}}


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Method"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response


if __name__ == '__main__':
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=443,
        workers=1,
        ssl_certfile='./cert/server.crt',
        ssl_keyfile='./cert/server.key'
    )
