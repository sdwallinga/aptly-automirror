#!/bin/bash
# Publishes the current date's snapshot for an argument-specified mirror
# Accepts two args: [$1] mirror name [$2] filesystem endpoint (repo-specific package directory to serve)
aptly publish snapshot -passphrase="`vault read -field=passphrase secret/eng/mirror-apt-signing`" -batch=true $1-`date +%m.%d` filesystem:mirror:$2
