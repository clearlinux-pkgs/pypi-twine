#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-twine
Version  : 4.0.0
Release  : 28
URL      : https://files.pythonhosted.org/packages/35/8d/1b61752e1c3036ce36155d1a5144444e0134d5b9624a7f7ef5b6b1ac61d1/twine-4.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/35/8d/1b61752e1c3036ce36155d1a5144444e0134d5b9624a7f7ef5b6b1ac61d1/twine-4.0.0.tar.gz
Summary  : Collection of utilities for publishing packages on PyPI
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-twine-bin = %{version}-%{release}
Requires: pypi-twine-license = %{version}-%{release}
Requires: pypi-twine-python = %{version}-%{release}
Requires: pypi-twine-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(keyring)
BuildRequires : pypi(pkginfo)
BuildRequires : pypi(py)
BuildRequires : pypi(readme_renderer)
BuildRequires : pypi(requests)
BuildRequires : pypi(requests_toolbelt)
BuildRequires : pypi(rfc3986)
BuildRequires : pypi(rich)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://img.shields.io/pypi/v/twine.svg
:target: https://pypi.org/project/twine

%package bin
Summary: bin components for the pypi-twine package.
Group: Binaries
Requires: pypi-twine-license = %{version}-%{release}

%description bin
bin components for the pypi-twine package.


%package license
Summary: license components for the pypi-twine package.
Group: Default

%description license
license components for the pypi-twine package.


%package python
Summary: python components for the pypi-twine package.
Group: Default
Requires: pypi-twine-python3 = %{version}-%{release}

%description python
python components for the pypi-twine package.


%package python3
Summary: python3 components for the pypi-twine package.
Group: Default
Requires: python3-core
Provides: pypi(twine)
Requires: pypi(importlib_metadata)
Requires: pypi(keyring)
Requires: pypi(pkginfo)
Requires: pypi(readme_renderer)
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)
Requires: pypi(rfc3986)
Requires: pypi(rich)
Requires: pypi(urllib3)

%description python3
python3 components for the pypi-twine package.


%prep
%setup -q -n twine-4.0.0
cd %{_builddir}/twine-4.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648739424
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-twine
cp %{_builddir}/twine-4.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-twine/7f6eb21389a5af4de0e7927a25fe236bc0cd3a75
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/twine

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-twine/7f6eb21389a5af4de0e7927a25fe236bc0cd3a75

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
