#/bin/bash
# Creates a daily snapshot for ALL registered aptly mirrors
aptly mirror list -raw | xargs -n 1 /home/ubuntu/.aptly/scripts/snap.sh
