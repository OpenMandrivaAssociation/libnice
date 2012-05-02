%define	major		10
%define	oname		nice
%define	libname		%mklibname %{oname} %major
%define develname	%mklibname %{oname} -d

Name:		libnice
Version:	0.1.1
Release:	%mkrel 5
Summary:	Implementation of the IETF's draft I.C.E standard
License:	LGPLv2+ and MPLv1+
Group:		System/Libraries
URL:		http://nice.freedesktop.org/wiki/
Source0:	http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRequires:	glib2-devel
BuildRequires:	libgupnp-igd-devel >= 0.1.2
BuildRequires:	libgstreamer-plugins-base-devel

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

%package -n	%{libname}
Summary:	Dynamic libraries from %{oname}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}nice1 < 0.1.1-4

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary: 	Header files, libraries and development documentation for %{oname}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}
Provides:       lib%{oname}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the header files, static libraries and development
documentation for %{oname}. If you like to develop programs using %{oname},
you will need to install %{oname}-devel.

%package 	utils
Summary:	Dynamic libraries from %{oname}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides: 	%{name}-utils = %{version}-%{release}
Obsoletes:	libnice

%description 	utils
This package contains various tools from %{name}.

%package -n	gstreamer0.10-%{oname}
Summary:	Gstreamer elements from %{oname}
Group:		System/Libraries
Requires:	%{libname} = %{version}
# conflict with older %%libname that had the gst .so, before the split
Conflicts:	%{_lib}nice0 < 0.1.0
Conflicts:	%{_lib}nice1 < 0.1.0

%description -n	gstreamer0.10-%{oname}
Gstreamer elements from %{oname}.

%prep
%setup -q

%build
#autoreconf -fiv
%configure2_5x \
	--enable-gupnp \
	--disable-static

# disable rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make

%install
%makeinstall_std

# don't ship .la
find %{buildroot} -name "*.la" -delete

%check
make check

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING COPYING.LGPL COPYING.MPL NEWS README
%{_includedir}/%{oname}/*.h
%{_includedir}/stun/*.h
%{_includedir}/stun/usages/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{oname}.pc
%{_datadir}/gtk-doc/html/%{name}/*

%files utils
%{_bindir}/stun*

%files -n gstreamer0.10-%{oname}
%{_libdir}/gstreamer-0.10/*.so
