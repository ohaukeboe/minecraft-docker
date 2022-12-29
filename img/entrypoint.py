#!/usr/bin/python3.9

import os
import wget
import tarfile

verbose = os.environ.get('VERBOSE')

def verbosePrint (string):
    if verbose:
        print(string)

bkup = os.environ.get('WORLD_BACKUP')
mods = os.environ.get('MODS_BACKUP')
plug = os.environ.get('PLUGINS_BACKUP')

lines = open('/minecraft/properties', 'r').readlines()
serverProperties = open('/minecraft/server.properties', 'w')

verbosePrint('Generating server.properties')
for line in lines:
    line = line.strip('\n')
    if not line[0]=='#':
        line = line.split('=')
        verbosePrint('Looking for: ' + line[0].upper().replace('-', '_'))
        environ = os.environ.get(line[0].upper().replace('-', '_'))
        if not environ:
            environ = line[1]
        verbosePrint('writing ' + environ)
        newLine = line[0]+'='+environ
        serverProperties.write(newLine+'\n')
    else:
        serverProperties.write(line+'\n')

serverProperties.close()
verbosePrint('server.properties generated')

# Add default world
if bkup:
    if not os.path.exists('/minecraft/world'):
        verbosePrint ('Installing default world', bkup)
        os.mkdir('/minecraft/world')

        wget.download(bkup, out='/tmp/world.tar.gz')
        tarfile.extractall('/tmp/world.tar.gz')
        os.remove('/tmp/world.tar.gz')
        verbosePrint ('Done installing default world', bkup)

# Add plugins
# if plug:
#     if not os.path.exists('/minecraft/plug'):
#         verbosePrint ('Installing default plug', plug)
#         os.mkdir('/minecraft/plug')

#         wget.download(plug, out='/tmp/plug.tar.gz')
#         tarfile.extractall('/tmp/plug.tar.gz')
#         os.remove('/tmp/plug.tar.gz')
#         verbosePrint('Done installing plug')

# add mods
if mods:
    if not os.path.exists('/minecraft/mods'):
        verbosePrint ('Installing default mods', mods)
        os.mkdir('/minecraft/mods')

        wget.download(mods, out='/tmp/mods.tar.gz')
        tarfile.extractall('/tmp/mods.tar.gz')
        os.remove('/tmp/mods.tar.gz')
        verbosePrint('Done installing mods')

# add config
if not os.path.exists('/minecraft/config'):
    os.mkdir('/minecraft/config')

if not os.path.exists('/minecraft/config/usercache.json'):
    fp = open('/minecraft/config/usercache.json', 'w')
    fp.close()

if not os.path.exists('/minecraft/config/whitelist.json'):
    fp = open('/minecraft/config/whitelist.json', 'w')
    fp.close()

if not os.path.exists('/minecraft/usercache.json'):
    os.symlink('/minecraft/config/usercache.json', '/minecraft/usercache.json')
if not os.path.exists('/minecraft/whitelist.json'):
    os.symlink('/minecraft/config/whitelist.json', '/minecraft/whitelist.json')
if not os.path.exists('/minecraft/ops.json'):
    os.symlink('/minecraft/config/ops.json', '/minecraft/ops.json')

os.system('java -cp /minecraft -Xmx${JAVA_MEMORY} -Xms${JAVA_MEMORY} -Dfml.queryResult=confirm -jar forge-*.jar nogui')