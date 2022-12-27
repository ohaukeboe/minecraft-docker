
FROM openjdk:17-slim

WORKDIR /minecraft


# Set defaults for environment variables
ENV MINECRAFT_PORT 25565
ENV RCON_PORT 27015
ENV JAVA_MEMORY 1G
ENV RCON_ENABLED false
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
#ENV SERVER_IP
ENV ALLOW_FLIGHT true
ENV LEVEL_NAME world
ENV VIEW_DISTANCE 10
ENV GENERATE_STRUCTURES true
ENV ONLINE_MODE true
ENV MAX_BUILD_HEIGHT 256
#ENV LEVEL_SEED
ENV PREVENT_PROXY_CONNECTION false

EXPOSE 25565

RUN apt-get update && apt-get install -y libfreetype6 curl wget python3 python3-wget && \
    # Install rcon
    curl -L -o rcon-cli.tar.gz https://github.com/itzg/rcon-cli/releases/download/1.5.1/rcon-cli_1.5.1_linux_amd64.tar.gz && \
    tar -xzf rcon-cli.tar.gz && \
    rm rcon-cli.tar.gz && \
    mv rcon-cli /usr/local/bin && \
    # Setup the server
    curl -L -o fabric-installer.jar https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.1/fabric-installer-0.11.1.jar && \
    java -jar fabric-installer.jar server -downloadMinecraft -mcversion 1.16.5 && \
    useradd minecraft

USER minecraft

# Copy the signed eula
COPY --chown=minecraft:minecraft ./eula.txt eula.txt

# Add the entrypoint
COPY --chown=minecraft:minecraft ./entrypoint.py entrypoint.py
COPY --chown=minecraft:minecraft ./server.properties server.properties


ENTRYPOINT [ "./entrypoint.py" ]
