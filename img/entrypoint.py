#!/usr/bin/python3.9

import os
import wget
import tarfile

bkup = os.environ.get('WORLD_BACKUP')
mods = os.environ.get('MODS_BACKUP')
plug = os.environ.get('PLUGINS_BACKUP')

# Add default world
if bkup:
    if not os.path.exists('/minecraft/world'):
        print ('Installing default world', bkup)
        os.mkdir('/minecraft/world')

        wget.download(bkup, out='/tmp/world.tar.gz')
        tarfile.extractall('/tmp/world.tar.gz')
        os.remove('/tmp/world.tar.gz')
        print ('Done installing default world', bkup)

# Add plugins
# if plug:
#     if not os.path.exists('/minecraft/plug'):
#         print ('Installing default plug', plug)
#         os.mkdir('/minecraft/plug')

#         wget.download(plug, out='/tmp/plug.tar.gz')
#         tarfile.extractall('/tmp/plug.tar.gz')
#         os.remove('/tmp/plug.tar.gz')
#         print('Done installing plug')

# add mods
if mods:
    if not os.path.exists('/minecraft/mods'):
        print ('Installing default mods', mods)
        os.mkdir('/minecraft/mods')

        wget.download(mods, out='/tmp/mods.tar.gz')
        tarfile.extractall('/tmp/mods.tar.gz')
        os.remove('/tmp/mods.tar.gz')
        print('Done installing mods')

# add config
if not os.path.exists('/minecraft/config'):
    os.mkdir('/minecraft/config')

if not os.path.exists('/minecraft/config/usercache.json'):
    fp = open('/minecraft/config/usercache.json', 'w')
    fp.close()

if not os.path.exists('/minecraft/config/whitelist.json'):
    fp = open('/minecraft/config/whitelist.json', 'w')
    fp.close()

os.symlink('/minecraft/config/usercache.json', '/minecraft/usercache.json')
os.symlink('/minecraft/config/whitelist.json', '/minecraft/whitelist.json')
os.symlink('/minecraft/config/ops.json', '/minecraft/ops.json')
os.system('"echo \\"$(cat /minecraft/server.properties)\\""> /minecraft/server.properties')

os.system('java -cp /minecraft -Xmx${JAVA_MEMORY} -Xms${JAVA_MEMORY} -Dfml.queryResult=confirm -jar fabric-server-launch.jar nogui')
