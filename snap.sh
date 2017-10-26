#/bin/bash
# Creates a daily snapshot for an argument-specified mirror
aptly snapshot create $1-`date +%m.%d` from mirror $1
