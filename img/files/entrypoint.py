#!/usr/bin/python3.9

import os
import tarfile
import shutil
import time
import json
import subprocess as sb
import websockets as ws
import asyncio as asy
from multiprocessing import Process

verbose = os.environ.get("VERBOSE")


def verbosePrint(string):
    if verbose:
        print(string, flush=True)


lines = open("/app/minecraft/properties", "r").readlines()
serverProperties = open("/app/minecraft/server.properties", "w")

verbosePrint("Generating server.properties")
for line in lines:
    line = line.strip("\n")
    if not line[0] == "#":
        line = line.split("=")
        verbosePrint("Looking for: " + line[0].upper().replace("-", "_"))
        environ = os.environ.get(line[0].upper().replace("-", "_"))
        if not environ:
            environ = line[1]
        verbosePrint("writing " + environ)
        newLine = line[0] + "=" + environ
        serverProperties.write(newLine + "\n")
    else:
        serverProperties.write(line + "\n")

serverProperties.close()
verbosePrint("server.properties generated")

# add config
if not os.path.exists("/app/config"):
    os.mkdir("/app/config")

if not os.path.exists("/app/config/usercache.json"):
    fp = open("/app/config/usercache.json", "w")
    fp.close()

if not os.path.exists("/app/config/whitelist.json"):
    fp = open("/app/config/whitelist.json", "w")
    fp.close()

if not os.path.exists('/app/config/ops.json'):
    fp = open("/app/config/ops.json", "w")
    fp.close()

if not os.path.exists("/app/minecraft/usercache.json"):
    os.symlink("/app/config/usercache.json", "/app/minecraft/usercache.json")

if not os.path.exists("/app/minecraft/whitelist.json"):
    os.symlink("/app/config/whitelist.json", "/app/minecraft/whitelist.json")

if not os.path.exists("/app/minecraft/ops.json"):
    os.symlink("/app/config/ops.json", "/app/minecraft/ops.json")

verbosePrint("Starting minecraft server")
server_start_cmd = "java -cp /app/minecraft -Xmx${JAVA_MEMORY} -Xms${JAVA_MEMORY} -Dfml.queryResult=confirm -jar fabric-server-mc.*.jar nogui"
process = sb.Popen(server_start_cmd, stdin=sb.PIPE, shell=True)


def backup(process):
    verbosePrint("Going to sleep...")
    time.sleep(60)
    while True:
        verbosePrint("Stop save")
        mc_comm = process.stdin.write("save-off\n".encode())
        mc_comm = process.stdin.write("save-all\n".encode())
        process.stdin.flush()
        time.sleep(10)
        verbosePrint("Running backup")
        os.system("./helpers/backup.py")
        verbosePrint("Save on")
        mc_comm = process.stdin.write("save-on\n".encode())
        process.stdin.flush()
        verbosePrint("Going back to sleep...")
        time.sleep(60 * 60 * 24)


backup_process = Process(target=backup, args=(process,))
backup_process.start()


def stop():
    backup_process.terminate()
    process.communicate("stop\n".encode())


def start():
    global process
    global backup_process
    process = sb.Popen(server_start_cmd, stdin=sb.PIPE, shell=True)
    backup_process = Process(target=backup, args=(process,))
    backup_process.start()
    return (process, backup_process)

def addPrivilege(task):
    mc_comm = process.stdin.write("{task} {name}\n".format(task = task['task'], name = task['name']).encode())
    process.stdin.flush()

async def restore(websocket, path):
    async for task in websocket:
        verbosePrint(task)
        task = json.loads(task)
        ret = "ack"
        if (task['task'] == "stop"):
            stop(task)
        elif (task['task'] == "start"):
            start(task)
        elif (task['task'] == "whitelist"):
            task['task'] = "whitelist add"
            addPrivilege(task)
        elif (task['task'] == "op"):
            addPrivilege(task)
        else:
            print ("no valid task")
        await websocket.send(ret)


async def startSocket():
    verbosePrint("starting websocket")
    async with ws.serve(restore, "127.0.0.1", 18080):
        await asy.Future()


asy.run(startSocket())
