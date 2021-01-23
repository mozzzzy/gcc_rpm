# gcc_rpm
Config files to build rpm packages of gcc.

## Build
### Get source code of gcc
```bash
$ git submodule update --init
```

### Build rpm packages
```bash
$ make all
```
Then the rpm packages are created in `rpmbuild/RPMS/x86_64` and `rpmbuild/SRPMS`.
```bash
$ tree rpmbuild -I BUILD
rpmbuild
├── BUILDROOT
├── RPMS
│   └── x86_64
│       ├── gcc-10.2.0-1.el7.x86_64.rpm
│       └── gcc-debuginfo-10.2.0-1.el7.x86_64.rpm
├── SOURCES
│   └── gcc.tar.gz
├── SPECS
│   └── gcc.spec
└── SRPMS
    └── gcc-10.2.0-1.el7.src.rpm

    6 directories, 5 files
```
