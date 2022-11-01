# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/

%define debug_package %{nil}

Name: pamixer
Version: 1.6
Release: 2%{?dist}
Summary: Pulseaudio command line mixer

License: GPL3
URL: https://github.com/cdemoulins/pamixer
Source0: https://github.com/cdemoulins/pamixer/archive/%{version}.tar.gz

BuildRequires: gcc-c++ pulseaudio-libs-devel boost-devel
#Requires:

%description
pamixer is like amixer but for pulseaudio. It can control the volume levels of the sinks.

%prep
%setup -q

%build
%meson_build

%install
%meson_install

%files
%doc README.rst
%license COPYING
%{_bindir}/pamixer

%changelog
* Mon Feb 03 2020 Johan Swensson <kupo@kupo.se>- 1.4-2
- rebuilt

* Mon Nov 11 2019 Johan Swensson <kupo@kupo.se> - 1.4-1
- initial build

