
# Minecraft Server Docker Project README

<!--toc:start-->
- [Minecraft Server Docker Project README](#minecraft-server-docker-project-readme)
  - [Overview](#overview)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
    - [Setup](#setup)
    - [Running](#running)
    - [Stopping](#stopping)
    - [Updating](#updating)
  - [Configuration](#configuration)
    - [Server Configuration](#server-configuration)
<!--toc:end-->

## Overview

This project provides a Dockerized solution for running a Minecraft server. It simplifies the process of setting up and managing a Minecraft server by using Docker, an open-source platform that automates the deployment of applications inside software containers.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)

## Usage

### Setup

Create a new directory for your Minecraft server and create a `docker-compose.yml` file inside it. Below is an example of a `docker-compose.yml` file for a fabric Minecraft server.

```yaml
version: "3.9"

services:
  minecraft:
    image: quteraz/minecraft-fabric:MINECRAFT_VERSION
    container_name: "minecraft"
    entrypoint: "./entrypoint.py"
    ports:
      - "25567:25565/tcp"
      - "25566:25566/udp"
    user: "969:969"
    volumes:
      - type: volume
        source: minecraft_fabric
        target: /app/config
      - type: volume
        source: world_fabric
        target: /app/minecraft/world
      - type: volume
        source: mods_fabric
        target: /app/minecraft/mods
      - type: volume
        source: mods_fabric_config
        target: /app/minecraft/config

volumes:
  minecraft:
  world:
  mods:
  minecraft_fabric:
  world_fabric:
  mods_fabric:
  minecraft_proxy_config:
  mods_fabric_config:
```

Replace `MINECRAFT_VERSION` with the version of Minecraft you want to run. For example, if you want to run a fabric Minecraft server on version 1.20.4, you would replace `MINECRAFT_VERSION` with `1.20.4`.

### Running

To start your Minecraft server, run the following command in the directory where your `docker-compose.yml` file is located.

```bash
docker-compose up -d
```


### Stopping

To stop your Minecraft server, run the following command in the directory where your `docker-compose.yml` file is located.

```bash
docker-compose down
```


### Updating

To update your Minecraft server, run the following command in the directory where your `docker-compose.yml` file is located.

```bash
docker-compose pull
docker-compose up -d
```

## Configuration

### Server Configuration

The following environment variables can be used to configure your Minecraft server.

| Environment Variable          | Default  | Description                                                                                                               |
| MINECRAFT_PORT                | 25565    | The port the server runs on.                                                                                              |
| JAVA_MEMORY                   | 2G       | The amount of memory allocated to the server.                                                                             |
| WHITELIST_ENABLED             | true     | Whether or not the server uses a whitelist.                                                                               |
| ALLOW_NETHER                  | true     | Whether or not the server allows players to travel to the Nether.                                                         |
| GAME_MODE                     | survival | The default game mode for players.                                                                                        |
| ENABLE_QUERY                  | false    | Whether or not the server responds to Minecraft query requests.                                                           |
| PLAYER_IDLE_TIMEOUT           | 0        | The amount of time (in minutes) a player can be idle before being kicked.                                                 |
| DIFFICULTY                    | hard     | The difficulty of the server.                                                                                             |
| SPAWN_MONSTERS                | true     | Whether or not monsters spawn.                                                                                            |
| SPAWN_ANIMALS                 | true     | Whether or not animals spawn.                                                                                             |
| SPAWN_NPCS                    | true     | Whether or not NPCs spawn.                                                                                                |
| LEVEL_TYPE                    | default  | The type of world the server uses.                                                                                        |
| PVP                           | false    | Whether or not players can deal damage each other.                                                                        |
| BROADCAST_CONSOLE_TO_OPS      | true     | Whether or not messages from the console are sent to ops.                                                                 |
| SPAWN_PROTECTION              | 16       | The radius (in blocks) around the spawn where players cannot build.                                                       |
| MAX_TICK_TIME                 | 60000    | The maximum amount of time (in milliseconds) a single tick may take.                                                      |
| FORCE_GAMEMODE                | true     | Whether or not players are forced to use the default game mode.                                                           |
| OP_PERMISSION_                | LEVEL 4  | The permission level required to use operator commands.                                                                   |
| SNOOPER_ENABLED               | true     | Whether or not the server sends data to Mojang.                                                                           |
| HARDCORE                      | false    | Whether or not the server is in hardcore mode.                                                                            |
| ENABLE_COMMAND_BLOCK          | false    | Whether or not command blocks are enabled.                                                                                |
| MAX_PLAYERS                   | 10       | The maximum number of players allowed on the server.                                                                      |
| NETWORK_COMPRESSION_THRESHOLD | 256      | The minimum size (in bytes) of a packet before it is compressed.                                                          |
| MAX_WORLD_SIZE                | 29999984 | The maximum size (in blocks) of the world.                                                                                |
| SERVER_IP                     | 0.0.0.0  | The IP address the server listens on.                                                                                     |
| ALLOW_FLIGHT                  | true     | Whether or not to kick players who attempt to fly.                                                                        |
| LEVEL_NAME                    | world    | The name of the world.                                                                                                    |
| VIEW_DISTANCE                 | 10       | The maximum number of chunks sent to the client.                                                                          |
| GENERATE_STRUCTURES           | true     | Whether or not structures (e.g. villages) generate.                                                                       |
| ONLINE_MODE                   | true     | Whether or not the server checks connecting players against Mojang's servers to make sure they are using a valid account. |
| MAX_BUILD_HEIGHT              | 256      | The maximum height (in blocks) a player can build.                                                                        |
| PREVENT_PROXY_CONNECTION      | false    | Whether or not the server prevents connections from proxies.                                                              |
| BACKUP_LENGTH                 | 7        | The number of backups to keep.                                                                                            |
| VERBOSE                       | True     | Whether or not the server outputs extra information to the console.                                                       |
