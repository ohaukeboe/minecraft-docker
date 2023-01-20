#! /bin/bash

cd /app/minecraft

if ["$MOD_LOADER" == "fabric"]
then
	curl -OJ $LOADER_LINK
else if ["$MOD_LOADER" == "forge"]
then
	$installer_path=/app/minecraft.installer.jar
	curl -L -o $installer_path $LOADER_LINK
	java -jar $installer_path --installerServer