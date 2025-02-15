%define gstapi 1.0
%define oname nice
%define major 10
%define libname %mklibname %{oname} %{major}
%define devname %mklibname %{oname} -d

Summary:	Implementation of the IETF's draft I.C.E standard
Name:		libnice
Version:	0.1.21
Release:	5
License:	LGPLv2+ and MPLv1+
Group:		System/Libraries
Url:		https://nice.freedesktop.org/wiki/
Source0:	http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
Patch0:		https://cgit.freedesktop.org/libnice/libnice/commit/?id=f4e2838f664f4007838f4c635d7a4fe653aae68b.patch
Patch1:		libnice-0.1.21-gupnp-igd-1.6.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(gupnp-igd-1.6)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	meson

%description
Nice is an implementation of the IETF's draft Interactive Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

ICE is useful for applications that want to establish peer-to-peer UDP
data streams. It automates the process of traversing NATs and provides
security against some attacks.

Existing standards that use ICE include the Session Initiation Protocol
(SIP) and Jingle, XMPP extension for audio/video calls.

Nice includes integration with GStreamer. It is used by Farsight for RTP
transport. 

%package utils
Summary:	Dynamic libraries from %{oname}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-utils = %{version}-%{release}
Obsoletes:	libnice < 0.1.21-1

%description utils
This package contains various tools from %{name}.

%package -n %{libname}
Summary:	Dynamic libraries from %{oname}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}nice1 < 0.1.1-4

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{devname}
Summary:	Header files, libraries and development documentation for %{oname}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the header files, static libraries and development
documentation for %{oname}. If you like to develop programs using %{oname},
you will need to install %{oname}-devel.

%package -n gstreamer%{gstapi}-%{oname}
Summary:	Gstreamer elements from %{oname}
Group:		System/Libraries
Requires:	%{libname} = %{version}
# conflict with older %%libname that had the gst .so, before the split
Conflicts:	%{_lib}nice0 < 0.1.0
Conflicts:	%{_lib}nice1 < 0.1.0
Obsoletes:	gstreamer0.10-%{oname} < 0.1.21-1

%description -n gstreamer%{gstapi}-%{oname}
Gstreamer elements from %{oname}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

#% check
#disabled due fails
#make check

%files utils
%{_bindir}/s*

%files -n %{libname}
%{_libdir}/libnice.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING COPYING.LGPL COPYING.MPL NEWS README
%{_includedir}/%{oname}/*.h
%{_includedir}/stun/*.h
%{_includedir}/stun/usages/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{oname}.pc
%{_libdir}/girepository-1.0/Nice-0.1.typelib
%{_datadir}/gir-1.0/Nice-0.1.gir

%files -n gstreamer%{gstapi}-%{oname}
%{_libdir}/gstreamer-%{gstapi}/*.so
