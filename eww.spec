%define githash 52e9603dd8c79cbc267a4733389c1f7e7625b352

%define shorthash %(c=%{githash}; echo ${c:0:10})

Name:          eww
Version:       0.4.0
Release:       5.git.%{shorthash}%{?dist}
Summary:       ElKowars wacky widgets
License:       MIT
URL:           https://github.com/elkowar/eww
Source0:        %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz
Source1:       https://github.com/rust-lang/rustup.rs.git

Requires: gtk3, gtk-layer-shell, pango, gdk-pixbuf2
Requires: cairo, glib2, libgcc, glibc

BuildRequires: gcc
BuildRequires: gtk3-devel, gtk-layer-shell-devel, pango-devel, gdk-pixbuf2-devel
BuildRequires: cairo-devel, glib2-devel, glibc-devel
BuildRequires: git


%description
Elkowars Wacky Widgets is a standalone widget system made in Rust 
that allows you to implement your own, custom widgets in any window manager.

%global debug_package %{nil}

%prep
%setup -q -n %{name}-%{githash}
export RUSTUP_HOME=%{_builddir}/.rustup
export CARGO_HOME=%{_builddir}/.cargo

%build
export RUSTUP_HOME=%{_builddir}/.rustup
export CARGO_HOME=%{_builddir}/.cargo
export PATH=%{_builddir}/.cargo/bin:$PATH
cargo build --release --features no-self-update

%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -m 755 %{_builddir}/%{name}-%{githash}/target/release/eww %{buildroot}%{_bindir}/eww

%files
%{_bindir}/eww
