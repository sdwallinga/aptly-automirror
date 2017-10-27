#!/usr/bin/env python3
import os
import json

import hvac

from automirror import automirror

client = hvac.Client(url='https://plkvolxvault04.prd.5thc.co:8200', token=os.environ['VAULT_TOKEN'], verify=os.environ['VAULT_CACERT'])
signing = client.read('secret/eng/mirror-apt-signing')
signing = signing['data']['passphrase']

with open('mirror.json') as mirror_file:
  data = json.load(mirror_file)
  for repo in data['repositories']:
    for item in repo['dists']:
      a = automirror.AutoMirror(data['endpoint'], repo['name'], item['distribution'], item['uri'])
      a.build_mirror(signing)