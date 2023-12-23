#!/bin/python3
import requests
import os

server_path = "/app/minecraft/"


def _fabric(minecraft_version):
    url = "https://meta.fabricmc.net/v2/versions/installer/"
    response = requests.get(url)

    installer_url = ""

    if response.status_code == 200:
        installer_url = response.json()[0]["url"]
    else:
        print("Error when fetching Fabric versions")
        exit(1)

    print("Downloading Fabric installer")
    os.system(f"curl -o fabric-installer.jar {installer_url}")

    install_cmd = f"java -jar fabric-installer.jar server -dir {server_path} -downloadMinecraft"
    if minecraft_version:
        install_cmd += minecraft_version

    os.system(install_cmd)


def _forge():
    # This is stupid
    url = os.environ["LOADER_LINK"]
    print("Downloading Forge installer")
    os.system(f"curl -o forge-installer.jar {url}")
    os.system(f"java -jar forge-installer.jar --installServer {server_path}")


if __name__ == "__main__":
    print(os.environ["MOD_LOADER"])

    minecraft_version = os.environ.get("MINECRAFT_VERSION")

    if os.environ["MOD_LOADER"] == "fabric":
        _fabric(minecraft_version)
    elif os.environ["MOD_LOADER"] == "forge":
        _forge()
