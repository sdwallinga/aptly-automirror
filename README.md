## automirror

Collection of scripts and tooling working towards painless apt repository management.

### Adding a new software source
Follow the schema in `mirror.json`, adding a new entry to the `repositories` array.

### TODOs
* Make it work!
* Add PPA-specific support
* Add support for multi-component publishing, such as Canonical's partner repository
* Actual Vault integration
* Add error handling
* Finer granularity of actions, i.e. don't just do all the steps
