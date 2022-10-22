%define githash 44cee0f5f84caf093871ccbc74778c9497ac8bbd

%define shorthash %(c=%{githash}; echo ${c:0:10})

Name:           hyprland
Version:        1.git.%{shorthash}%{?dist}
Release:        %autorelease
Summary:        Dynamic tiling Wayland compositor that doesn't sacrifice on its looks

# main source code is BSD-3-Clause
# subprojects/wlroots is MIT
License:        BSD-3-Clause and MIT
URL:            https://github.com/hyprwm/Hyprland
Source:         %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)

# bundled wlroots build requirements
BuildRequires:  glslang
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  libdrm-devel
BuildRequires:  git


%description
Hyprland is a dynamic tiling Wayland compositor based on wlroots that doesn't
sacrifice on its looks.  It supports multiple layouts, fancy effects, has a
very flexible IPC model allowing for a lot of customization, and more.


%prep
%autosetup -p 1 -c


%build
meson -Dprefix=%{_prefix} -Dbuildtype=release _build
ninja -C _build/

%install
export DESTDIR=%{buildroot}
ninja -C _build/ install

# remove wlroots development files
rm -r %{buildroot}%{_includedir}/wlr
rm -r %{buildroot}%{_libdir}/libwlroots.a
rm -r %{buildroot}%{_libdir}/pkgconfig/wlroots.pc


%files
%{_bindir}/Hyprland
%{_bindir}/hyprctl
%{_mandir}/man1/Hyprland.1*
%{_mandir}/man1/hyprctl.1*
%{_datadir}/hyprland
%{_datadir}/wayland-sessions/hyprland.desktop



%changelog
%autochangelog
