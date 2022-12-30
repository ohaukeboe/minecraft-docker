#! /usr/bin/python3.9

import sys
import os
import shutil as sh
import asyncio as asy
import websockets as ws

backup_type = sys.argv[1]
backup_date = sys.argv[2]

filename = '/minecraft/config/backup/' + backup_type + '/' + backup_date + '.tar.gz'
extract_dir = '/minecraft/' + backup_type

async def send():
    uri = 'ws://127.0.0.1:18080'
    async with ws.connect(uri) as websocket:
        await websocket.send('stop')
        await websocket.recv()
        sh.rmtree('/minecraft/' + backup_type, ignore_errors=True)
        sh.unpack_archive(filename, '/minecraft')
        await websocket.send('start')
        await websocket.recv()

asy.run(send())

