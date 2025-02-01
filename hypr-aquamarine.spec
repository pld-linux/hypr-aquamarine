Summary:	Very light linux rendering backend library
Name:		hypr-aquamarine
Version:	0.7.2
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/hyprwm/aquamarine/releases
Source0:	https://github.com/hyprwm/aquamarine/archive/v%{version}/aquamarine-v%{version}.tar.gz
# Source0-md5:	61c6a668d792276872a1721752719a49
Patch0:		flags.patch
URL:		https://hyprland.org/
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGLESv2-devel
BuildRequires:	cmake >= 3.19
BuildRequires:	hwdata
BuildRequires:	hyprutils-devel >= 0.2.3
BuildRequires:	hyprwayland-scanner >= 0.4.0
BuildRequires:	libdisplay-info-devel
BuildRequires:	libdrm-devel
BuildRequires:	libinput-devel >= 1.26.0
BuildRequires:	libseat-devel >= 0.8.0
BuildRequires:	libstdc++-devel >= 6:11
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	udev-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols
Requires:	hyprutils >= 0.2.3
Requires:	libinput >= 1.26.0
Requires:	libseat >= 0.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aquamarine is a very light linux rendering backend library. It
provides basic abstractions for an application to render on a Wayland
session (in a window) or a native DRM session.

It is agnostic of the rendering API (Vulkan/OpenGL) and designed to be
lightweight, performant, and minimal.

Aquamarine provides no bindings for other languages. It is C++-only.

%package devel
Summary:	Header files for aquamarine
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for aquamarine.

%prep
%setup -q -n aquamarine-%{version}
%patch0 -p1

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libaquamarine.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaquamarine.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaquamarine.so
%{_includedir}/aquamarine
%{_pkgconfigdir}/aquamarine.pc
