%define githash 7a0e1b77f24ee89d627e552f9abc55eb636aaaa6

%define shorthash %(c=%{githash}; echo ${c:0:10})

Name:          eww
Version:       0.4.0
Release:       1.git.%{shorthash}%{?dist}
Summary:       ElKowars wacky widgets
License:       MIT
URL:           https://github.com/elkowar/eww
Source:        %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz

Requires: gtk3, gtk-layer-shell, pango, gdk-pixbuf2
Requires: cairo, glib2, libgcc, glibc

BuildRequires: gcc
BuildRequires: gtk3-devel, gtk-layer-shell-devel, pango-devel, gdk-pixbuf2-devel
BuildRequires: cairo-devel, glib2-devel, glibc-devel

%description
Elkowars Wacky Widgets is a standalone widget system made in Rust 
that allows you to implement your own, custom widgets in any window manager.

%global debug_package %{nil}

%prep
%setup -q -n %{name}-%{githash}
export RUSTUP_HOME=%{_builddir}/.rustup
export CARGO_HOME=%{_builddir}/.cargo
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain none -y
ls %{_builddir}/.rustup
export PATH=%{_builddir}/.cargo/bin:$PATH
rustup toolchain install nightly --allow-downgrade --profile minimal --component clippy

%build
export RUSTUP_HOME=%{_builddir}/.rustup
export CARGO_HOME=%{_builddir}/.cargo
export PATH=%{_builddir}/.cargo/bin:$PATH
cargo build --release --no-default-features --features=wayland

%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -m 755 %{_builddir}/%{name}-%{githash}/target/release/eww %{buildroot}%{_bindir}/eww

%files
%{_bindir}/eww
