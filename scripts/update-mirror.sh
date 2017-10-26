#!/bin/bash
# Updates all configured mirrors
aptly mirror list -raw | xargs -n 1 aptly mirror update
