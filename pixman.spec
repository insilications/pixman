#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pixman
Version  : 0.38.2
Release  : 33
URL      : http://cairographics.org/releases/pixman-0.38.2.tar.gz
Source0  : http://cairographics.org/releases/pixman-0.38.2.tar.gz
Summary  : The pixel-manipulation library for X and cairo
Group    : Development/Tools
License  : MIT
Requires: pixman-lib = %{version}-%{release}
Requires: pixman-license = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libpng-dev32
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(32pixman-1)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : zlib-dev32
Patch1: fmv.patch
Patch2: avx2.patch
Patch3: avx2-2.patch

%description
Pixman is a library that provides low-level pixel manipulation
features such as image compositing and trapezoid rasterization.

%package dev
Summary: dev components for the pixman package.
Group: Development
Requires: pixman-lib = %{version}-%{release}
Provides: pixman-devel = %{version}-%{release}
Requires: pixman = %{version}-%{release}

%description dev
dev components for the pixman package.


%package dev32
Summary: dev32 components for the pixman package.
Group: Default
Requires: pixman-lib32 = %{version}-%{release}
Requires: pixman-dev = %{version}-%{release}

%description dev32
dev32 components for the pixman package.


%package lib
Summary: lib components for the pixman package.
Group: Libraries
Requires: pixman-license = %{version}-%{release}

%description lib
lib components for the pixman package.


%package lib32
Summary: lib32 components for the pixman package.
Group: Default
Requires: pixman-license = %{version}-%{release}

%description lib32
lib32 components for the pixman package.


%package license
Summary: license components for the pixman package.
Group: Default

%description license
license components for the pixman package.


%prep
%setup -q -n pixman-0.38.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a pixman-0.38.2 build32
popd
pushd ..
cp -a pixman-0.38.2 buildavx2
popd
pushd ..
cp -a pixman-0.38.2 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554694229
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" %reconfigure --disable-static --disable-gtk \
--disable-mmx \
--disable-sse2 \
--disable-ssse3
make  %{?_smp_mflags}

make check || :
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" %reconfigure --disable-static --disable-gtk \
--disable-mmx \
--disable-sse2 \
--disable-ssse3
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%reconfigure --disable-static --disable-gtk \
--disable-mmx \
--disable-sse2 \
--disable-ssse3  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%reconfigure --disable-static --disable-gtk \
--disable-mmx \
--disable-sse2 \
--disable-ssse3
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export CXXFLAGS="$CXXFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export LDFLAGS="$LDFLAGS -m64 -march=skylake-avx512"
%reconfigure --disable-static --disable-gtk \
--disable-mmx \
--disable-sse2 \
--disable-ssse3
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :
cd ../buildavx2;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :
cd ../buildavx512;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1554694229
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pixman
cp COPYING %{buildroot}/usr/share/package-licenses/pixman/COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx512/
%make_install_avx512
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pixman-1/pixman-version.h
/usr/include/pixman-1/pixman.h
/usr/lib64/haswell/avx512_1/libpixman-1.so
/usr/lib64/haswell/libpixman-1.so
/usr/lib64/libpixman-1.so
/usr/lib64/pkgconfig/pixman-1.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpixman-1.so
/usr/lib32/pkgconfig/32pixman-1.pc
/usr/lib32/pkgconfig/pixman-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libpixman-1.so.0
/usr/lib64/haswell/avx512_1/libpixman-1.so.0.38.2
/usr/lib64/haswell/libpixman-1.so.0
/usr/lib64/haswell/libpixman-1.so.0.38.2
/usr/lib64/libpixman-1.so.0
/usr/lib64/libpixman-1.so.0.38.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpixman-1.so.0
/usr/lib32/libpixman-1.so.0.38.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pixman/COPYING
