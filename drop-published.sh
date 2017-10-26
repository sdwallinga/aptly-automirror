#!/bin/bash
# Drops all published repositories in preparation for publishing new collection of snapshots
aptly publish list -raw | awk '{ print $2 " " $1 }' | xargs -n 2 aptly publish drop
