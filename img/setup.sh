#! /bin/bash

cd /app/minecraft

echo ${MOD_LOADER}

if [[ "${MOD_LOADER}" == "fabric" ]]
then
	echo 'Downloading fabric'
	curl -OJ ${LOADER_LINK}
elif [[ "${MOD_LOADER}" == "forge" ]]
then
	echo 'Downloading forge'
	$installer_path="/app/minecraft/installer.jar"
	curl -L -o $installer_path ${LOADER_LINK}
	java -jar $installer_path --installServer
fi

echo 'Server downloaded'
