
Name:           tofi
Version:        0.6.0
Release:        %autorelease
Summary:        An extremely fast and simple dmenu / rofi replacement for wlroots-based Wayland compositors
License:        MIT
URL:            https://github.com/philj56/tofi
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Conflicts:      tofi

Requires: harfbuzz
Requires: cairo
Requires: pango
Requires: libxkbcommon

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  scdoc
BuildRequires:  cargo

%description
%{summary}

%prep
%setup

%build
cargo build --release --features no-self-update --bin rustup-init

%install
cd target/release
./rustup-init --default-toolchain none -y

%files


%changelog
%autochangelog
