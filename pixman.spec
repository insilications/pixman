#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pixman
Version  : 0.34.0
Release  : 16
URL      : http://cairographics.org/releases/pixman-0.34.0.tar.gz
Source0  : http://cairographics.org/releases/pixman-0.34.0.tar.gz
Summary  : The pixman library (version 1)
Group    : Development/Tools
License  : MIT
Requires: pixman-lib
BuildRequires : pkgconfig(libpng)
Patch1: fmv.patch

%description
Pixman is a library that provides low-level pixel manipulation
features such as image compositing and trapezoid rasterization.

%package dev
Summary: dev components for the pixman package.
Group: Development
Requires: pixman-lib
Provides: pixman-devel

%description dev
dev components for the pixman package.


%package lib
Summary: lib components for the pixman package.
Group: Libraries

%description lib
lib components for the pixman package.


%prep
%setup -q -n pixman-0.34.0
%patch1 -p1

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -O3 "
export FCFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -O3 "
export FFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -O3 "
export CXXFLAGS="$CXXFLAGS -falign-functions=32 -fno-semantic-interposition -O3 "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=pgo "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=pgo "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=pgo "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=pgo "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" %configure --disable-static --disable-gtk
make V=1  %{?_smp_mflags}

make check
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" %configure --disable-static --disable-gtk
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pixman-1/pixman-version.h
/usr/include/pixman-1/pixman.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
