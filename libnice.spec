%define	major	10
%define	oname	nice
%define	libname		%mklibname %{oname} %major
%define develname	%mklibname %{oname} -d -s

Name:		libnice
Version:	0.1.0
Release:	3
Summary:	Implementation of the IETF's draft Interactive Connectivity Establishment standard
License:	GPLv2+
Group:		System/Libraries
URL:		http://nice.freedesktop.org/wiki/
Source0:	http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRequires:	libgstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	gtk-doc
BuildRequires:	libgupnp-igd-devel >= 0.1.2
Requires:	%{libname} = %{version}


%description
Nice is an implementation of the IETF's
draft Interactive Connectivity Establishment
standard (ICE). It provides GLib-based
library, libnice.

ICE is useful for applications that want
to establish peer-to-peer UDP data streams.
It automates the process of traversing NATs
and provides security against some attacks.

Existing standards that use ICE include the
Session Initiation Protocol (SIP) and Jingle,
XMPP extension for audio/video calls.

Nice includes integration with GStreamer.
It is used by Farsight for RTP transport. 

%package -n	%{libname}
Summary:	Dynamic libraries from %{oname}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary:	Header files, libraries and development documentation for %{oname}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{oname}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the header files, static libraries and development
documentation for %{oname}. If you like to develop programs using %{oname},
you will need to install %{oname}-devel.

%package	utils
Summary:	Dynamic libraries from %{oname}
Group:		Networking/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-utils = %{version}-%{release}
Obsoletes:	libnice

%description 	utils
This package contains various tools from %{name}.

%package -n gstreamer0.10-libnice
Summary: Gstreamer element for ICE support
Group: System/Libraries
Requires: %{libname} = %{version}
Conflicts: %{mklibname nice 0}

%description -n gstreamer0.10-libnice
Nice is an implementation of the IETF's draft Interactive Connectivity Establishment
standard (ICE). It provides GLib-based library, libnice.

ICE is useful for applications that want to establish peer-to-peer UDP data streams.
It automates the process of traversing NATs and provides security against some attacks.

Existing standards that use ICE include the Session Initiation Protocol (SIP) and Jingle,
XMPP extension for audio/video calls.

This package provides integration with GStreamer. It is used by
Farsight for RTP transport.

%prep
%setup -q 

%build
#autoreconf -fiv
%configure2_5x --enable-gupnp
%make

%install
%makeinstall
rm -f %buildroot%_libdir/gstreamer-0.10/lib*a

%files utils
%doc COPYING README
%{_bindir}/stun*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n gstreamer0.10-libnice
%{_libdir}/gstreamer-0.10/*.so

%files -n %{develname}
%{_includedir}/%{oname}/*.h
%{_includedir}/stun/*.h
%{_includedir}/stun/usages/*.h
%{_libdir}/%{name}.a
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{oname}.pc
%{_datadir}/gtk-doc/html/%{name}/*

