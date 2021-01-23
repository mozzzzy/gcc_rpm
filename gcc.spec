Name:           gcc
Version:        10.2.0
Release:        1%{?dist}
Summary:        Various compilers (C, C++, Objective-C, Java, ...)

License:        GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
URL:            http://cppunit.sourceforge.net/
Source0:        gcc.tar.gz

BuildRequires:  make
BuildRequires:  flex

# Avoid "No build ID note found" error
%undefine _missing_build_ids_terminate_build
# Avoid "'check-rpaths' detected a broken RPATH and will cause 'rpmbuild' to fail." error
%undefine __arch_install_post

%description
The gcc package contains the GNU Compiler Collection version 10.2.
You'll need this package in order to compile C code.

%prep
%setup -q


%build
./contrib/download_prerequisites
mkdir build
pushd build
../configure --enable-languages=c,c++ --prefix=/opt --disable-bootstrap --disable-multilib
make %{?_smp_mflags}


%install
pushd build
%make_install


%files
/opt/share/man/*
/opt/bin/*
/opt/include/c++/*
/opt/lib/gcc/*
/opt/lib64/*
/opt/libexec/*
/opt/share/*

%changelog
