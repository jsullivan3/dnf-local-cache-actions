# libdnf5-local-cache-actions #

The purpose of this project is to provide the functionality of
python3-dnf-plugin-local for DNF5.  Since I'm lazy and have yet to
learn the DNF5 C-based API, this functionality is implemented as
libdnf actions, which itself is a plugin which provides hooks into the
DNF transaction.

The actions invoke the local cache script once after repositories are
loaded so it can present the local cache as a new repository, once for
each package to be copied into the cache, and then once at the end of
the transaction to rebuild the repository metadata.

## Logging ##

Messages are logged through `logger` and are available in the system
log.  Use the following commang to access them through the journal:

```
journalctl -t dnf-local-cache-actions
```

## Building ##

Use `mock`.  For example, to build this package for Fedora 41 x86_64:

```
mock -r fedora-41-x86_64 --buildsrpm --spec dnf-local-cache-actions.spec \
    --sources . --resultdir=f41-src && \
    mock -r fedora-41-x86_64 --rebuild --resultdir=f41 \
    f41-src/dnf-local-cache-actions-0.1-1.fc41.src.rpm
```

## License ##

This package is released under Gnu GPL v2.0, included as the file
LICENSE.txt for your reading pleasure.
