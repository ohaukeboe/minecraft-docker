#! /usr/bin/python3.9

import sys
import asyncio as asy
import websockets as ws
import json

name = sys.argv[1]
operation = None

if sys.argv[2]:
    operation = sys.argv[2]

if operation != "op" and operation != "whitelist":
    print("2nd operation must be eiter whitelist or op")
    exit()

if name == "-h" or name == "help" or operation is None:
    print('./giveaccess [name] [op | whitelist]')
    exit()

async def send(name, operation):
    uri = "ws://127.0.0.1:18080"
    async with ws.connect(uri) as websocket:
        await websocket.send(json.dumps({"task" : operation, "name" : name}))
        await websocket.recv()
        print("Added to whitelist")


asy.run(send(name, operation))