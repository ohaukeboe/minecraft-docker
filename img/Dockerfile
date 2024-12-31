# args to determine versions
ARG JAVA_VER=17
FROM openjdk:${JAVA_VER}-slim

# Set defaults for environment variables
ENV MINECRAFT_PORT=25565
ENV JAVA_MEMORY=2G
ENV WHITELIST_ENABLED=true
ENV ALLOW_NETHER=true
ENV GAME_MODE=survival
ENV ENABLE_QUERY=false
ENV PLAYER_IDLE_TIMEOUT=0
ENV DIFFICULTY=hard
ENV SPAWN_MONSTERS=true
ENV SPAWN_ANIMALS=true
ENV SPAWN_NPCS=true

ENV LEVEL_TYPE=default
ENV PVP=false
ENV BROADCAST_CONSOLE_TO_OPS=true
ENV SPAWN_PROTECTION=16
ENV MAX_TICK_TIME=60000
ENV FORCE_GAMEMODE=true
#ENV GENERATOR_SETTINGS
ENV OP_PERMISSION_LEVEL=4
ENV SNOOPER_ENABLED=true
ENV HARDCORE=false
ENV ENABLE_COMMAND_BLOCK=false
ENV MAX_PLAYERS=10
ENV NETWORK_COMPRESSION_THRESHOLD=256
#ENV RESOURCE_PACK_SHA1
ENV MAX_WORLD_SIZE=29999984
ENV SERVER_IP=0.0.0.0
ENV ALLOW_FLIGHT=true
ENV LEVEL_NAME=world
ENV VIEW_DISTANCE=10
ENV GENERATE_STRUCTURES=true
ENV ONLINE_MODE=true
ENV MAX_BUILD_HEIGHT=256
#ENV LEVEL_SEED
ENV PREVENT_PROXY_CONNECTION=false

ENV BACKUP_LENGTH=7
ENV VERBOSE=True

EXPOSE 25565

COPY setup.py ./

ARG MOD_LOADER
ARG LOADER_LINK
ARG USER_ID

RUN mkdir /app && \
    mkdir /app/config /app/minecraft/ /app/minecraft/mods /app/minecraft/world /app/minecraft/config && \
    # Upgrade and install server
    apt-get update && apt-get install -y libfreetype6 vim curl wget python3 python3-requests python3-wget python3-websockets && \
    python3 ./setup.py && \
    # chmod +x ./setup.py; ./setup.py && \
    rm setup.py && \
    # Make user and give permission
    useradd -rUm -u ${USER_ID} minecraft && \
    chown -Rh minecraft:minecraft /app

WORKDIR /app/minecraft

USER minecraft

COPY --chown=minecraft:minecraft ./files/ ./
