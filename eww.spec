
%define githash 52e9603dd8c79cbc267a4733389c1f7e7625b352

%define shorthash %(c=%{githash}; echo ${c:0:10})

Name:          eww
Version:       0.4.0
Release:       5.git.%{shorthash}%{?dist}
Summary:       ElKowars wacky widgets
License:       MIT
URL:           https://github.com/elkowar/eww
Source:        %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz


BuildRequires:  make gcc
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)

#For rustup
BuildRequires:  curl


%description
Elkowars Wacky Widgets is a standalone widget system made in Rust that allows you to implement your own, custom widgets in any window manager.

%prep
%autosetup -n %{name}

%build
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source $HOME/.cargo/env
cargo build --release --no-default-features --features=wayland


%install
install -p -D -m755 target/release/eww          %{buildroot}%{_bindir}/eww
mkdir -p %{buildroot}%{_sysconfdir}/xdg/%{name}
mv examples/eww-bar  %{buildroot}%{_sysconfdir}/xdg/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_sysconfdir}/xdg/%{name}/*

%changelog
%autochangelog
