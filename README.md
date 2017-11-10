# automirror

Collection of scripts and tooling working towards painless apt repository management.

### Requirements
For Vault lookups to work properly (over TLS), `VAULT_TOKEN` and `VAULT_CACERT` environment variables must be set, and the token must have access to `secret/eng`.

Requires `aptly >= 1.1`

### Adding a new software source
Follow the schema in `mirror.json`, adding a new entry to the `repositories` array.

### TODOs
* Add error handling
* Document required aptly config

### Feature wishlist:
* Control flags for atomic actions -- i.e. *just* update, *just* snapshot
* GPG key import prompt when remote repo key not already present
* Extend JSON object/logic to handle repository components (rather than grabbing all of them per default Aptly behavior)
* Multi-component publishing from the above
