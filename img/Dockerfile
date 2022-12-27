
FROM openjdk:8-slim

# Set defaults for environment variables
ENV MINECRAFT_PORT 25565
ENV JAVA_MEMORY 1G
ENV WHITELIST_ENABLED true
ENV ALLOW_NETHER true
ENV GAME_MODE survival
ENV ENABLE_QUERY false
ENV PLAYER_IDLE_TIMEOUT 0
ENV DIFFICULTY hard
ENV SPAWN_MONSTERS true
ENV SPAWN_ANIMALS true
ENV SPAWN_NPCS true

ENV LEVEL_TYPE default
ENV PVP false
ENV BROADCAST_CONSOLE_TO_OPS true
ENV SPAWN_PROTECTION 16
ENV MAX_TICK_TIME 60000
ENV FORCE_GAMEMODE true
#ENV GENERATOR_SETTINGS
ENV OP_PERMISSION_LEVEL 4
ENV SNOOPER_ENABLED true
ENV HARDCORE false
ENV ENABLE_COMMAND_BLOCK false
ENV MAX_PLAYERS 10
ENV NETWORK_COMPRESSION_THRESHOLD 256
#ENV RESOURCE_PACK_SHA1
ENV MAX_WORLD_SIZE 29999984
ENV SERVER_IP 127.0.0.1
ENV ALLOW_FLIGHT true
ENV LEVEL_NAME world
ENV VIEW_DISTANCE 10
ENV GENERATE_STRUCTURES true
ENV ONLINE_MODE true
ENV MAX_BUILD_HEIGHT 256
#ENV LEVEL_SEED
ENV PREVENT_PROXY_CONNECTION false

EXPOSE 25565

RUN mkdir /minecraft && \
    mkdir /minecraft/config && \
    apt-get update && apt-get install -y libfreetype6 curl wget python3 python3-wget && \
    useradd -rUm -u 966 minecraft && \
    chown -Rh minecraft:minecraft /minecraft



# Setup the server
RUN curl -L -o /minecraft/installer.jar https://maven.minecraftforge.net/net/minecraftforge/forge/1.16.5-36.2.34/forge-1.16.5-36.2.34-installer.jar && \
    cd /minecraft; java -jar /minecraft/installer.jar --installServer

USER minecraft

WORKDIR /minecraft

# Copy the signed eula
COPY --chown=minecraft:minecraft ./eula.txt eula.txt

# Add the entrypoint
COPY --chown=minecraft:minecraft ./entrypoint.py entrypoint.py
COPY --chown=minecraft:minecraft ./server.properties server.properties


#ENTRYPOINT [ "./entrypoint.py" ]
