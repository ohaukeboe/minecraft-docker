#!/usr/bin/python3.9

import os
import tarfile
import shutil
import time
import subprocess as sb
import websockets as ws
import asyncio as asy
from multiprocessing import Process

verbose = os.environ.get("VERBOSE")


def verbosePrint(string):
    if verbose:
        print(string, flush=True)


lines = open("/minecraft/properties", "r").readlines()
serverProperties = open("/minecraft/server.properties", "w")

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
if not os.path.exists("/minecraft/config"):
    os.mkdir("/minecraft/config")

if not os.path.exists("/minecraft/config/usercache.json"):
    fp = open("/minecraft/config/usercache.json", "w")
    fp.close()

if not os.path.exists("/minecraft/config/whitelist.json"):
    fp = open("/minecraft/config/whitelist.json", "w")
    fp.close()

if not os.path.exists("/minecraft/usercache.json"):
    os.symlink("/minecraft/config/usercache.json", "/minecraft/usercache.json")
if not os.path.exists("/minecraft/whitelist.json"):
    os.symlink("/minecraft/config/whitelist.json", "/minecraft/whitelist.json")
if not os.path.exists("/minecraft/ops.json"):
    os.symlink("/minecraft/config/ops.json", "/minecraft/ops.json")

verbosePrint("Starting minecraft server")
server_start_cmd = "java -cp /minecraft -Xmx${JAVA_MEMORY} -Xms${JAVA_MEMORY} -Dfml.queryResult=confirm -jar forge-*.jar nogui"
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
        os.system("./backup.py")
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


async def restore(websocket, path):
    async for task in websocket:
        verbosePrint(task)
        if task == "stop":
            stop()
        elif task == "start":
            start()
        await websocket.send("ack")


async def startSocket():
    verbosePrint("starting websocket")
    async with ws.serve(restore, "127.0.0.1", 18080):
        await asy.Future()


asy.run(startSocket())
