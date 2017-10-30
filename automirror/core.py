#!/usr/bin/env python3
# It's automirror!
import json
import datetime
import os
import subprocess

class AutoMirror:
  def __init__(self, endpoint, name, dist, uri):
    self.endpoint = endpoint
    self.name = name
    self.dist = dist
    self.uri  = uri
    self.cname = name + '-' + dist
    self.datestamp = datetime.date.today()
    self.datestamp = self.datestamp.strftime('%m.%d')

  def mirror_create(self):
    args = [
      'aptly',
      'mirror',
      'create',
      self.cname,
      self.uri,
      self.dist,
    ]
    return subprocess.call(args)

  def mirror_update(self):
    args = [
      'aptly',
      'mirror',
      'update',
      self.cname,
    ]
    return subprocess.call(args)

  def snapshot_create(self):
    snapshot = self.cname + '-' + self.datestamp
    args = [
      'aptly',
      'snapshot',
      'create',
      snapshot,
      'from',
      'mirror',
      self.cname,
    ]
    return subprocess.call(args)

  def snapshot_publish(self, signing):
    fs_endpoint = 'filesystem:' + self.endpoint + ':' + self.name
    signing_key_passphrase = signing
    snapshot = self.cname + '-' + self.datestamp
    args = [
      'aptly',
      'publish',
      'snapshot',
      '-passphrase',
      signing_key_passphrase,
      '-batch=true',
      snapshot,
      fs_endpoint,
    ]
    return subprocess.call(args)

  def build_mirror(self, signing):
    self.mirror_create()
    self.mirror_update()
    self.snapshot_create()
    self.snapshot_publish(signing)