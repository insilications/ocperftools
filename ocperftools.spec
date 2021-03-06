#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : ocperftools
Version  : 1.0.0
Release  : 22
URL      : file:///aot/build/clearlinux/packages/ocperftools/ocperftools-v1.0.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/ocperftools/ocperftools-v1.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: ocperftools-bin = %{version}-%{release}
Requires: parallel
BuildRequires : bash
BuildRequires : buildreq-cmake
BuildRequires : ca-certs
BuildRequires : cpio-bin
BuildRequires : curl
BuildRequires : curl-bin
BuildRequires : curl-dev
BuildRequires : curl-lib
BuildRequires : findutils
BuildRequires : mlocate
BuildRequires : openssl-dev
BuildRequires : openssl-lib
BuildRequires : p11-kit
BuildRequires : parallel
BuildRequires : pcre-dev
BuildRequires : pcre-extras
BuildRequires : sd
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the ocperftools package.
Group: Binaries

%description bin
bin components for the ocperftools package.


%prep
%setup -q -n ocperftools-clr
cd %{_builddir}/ocperftools-clr

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653975325
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
%cmake ..
make  %{?_smp_mflags}    V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1653975325
rm -rf %{buildroot}
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ocperf2bolt
/usr/bin/ocperfrun
/usr/bin/ocperfrunsettings
