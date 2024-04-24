#!/bin/bash

# URL of the file to be downloaded
URL="https://github.com/RamVasuthevan/TorontoLobbyistRegistryData/raw/main/Lobbyist%20Registry%20Activity.zip"

# Download the file using curl and save it to the data directory
curl -L "$URL" -o data/LobbyistRegistryActivity.zip

# Print a message to indicate success
echo "File downloaded successfully to data/LobbyistRegistryActivity.zip"

python -m build.build_db