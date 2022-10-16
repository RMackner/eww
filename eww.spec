%global git_date  20220526
%global git_hash  0b0715f
%global git_ver  0.3.0
%global rel 1
%global src_name  %{name}-%{git_date}-%{git_hash}.tar.xz

%define debug_package %{nil}

Name:           eww
Version:        %{git_ver}.%{git_date}
Release:        %{rel}.%{git_hash}%{?dist}
Summary:        ElKowars wacky widgets

License:        MIT
URL:            https://github.com/elkowar/eww
Source0:        https://github.com/elkowar/eww/archive/refs/tags/v0.4.0.tar.gz

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
%autosetup -n %{name}-0.4.0

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

