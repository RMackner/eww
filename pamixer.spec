%global debug_package %{nil}

Name:           pamixer
Version:        1.6
Release:        3%{?dist}
Summary:        PulseAudio command line mixer

License:        GPLv3
URL:            https://github.com/cdemoulins/%{name}
Source0:        https://github.com/cdemoulins/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cxxopts
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pulseaudio-libs-devel

%description
pamixer is like amixer but for PulseAudio. It can control the volume levels of the sinks.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.rst
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/pamixer.1.gz

%changelog
* Sat Aug 13 2022 - 1.6
- Update to latest release
- Use meson to build

* Mon Apr 25 2022 David Salomon <david35mm@disroot.org> - 1.5-1
- First pamixer package
