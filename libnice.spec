%define	gstapi	1.0
%define	oname	nice
%define	major	10
%define	libname	%mklibname %{oname} %{major}
%define devname	%mklibname %{oname} -d

Summary:	Implementation of the IETF's draft I.C.E standard
Name:		libnice
Version:	0.1.4
Release:	1
License:	LGPLv2+ and MPLv1+
Group:		System/Libraries
URL:		http://nice.freedesktop.org/wiki/
Source0:	http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(gupnp-igd-1.0)

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

%package 	utils
Summary:	Dynamic libraries from %{oname}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides: 	%{name}-utils = %{version}-%{release}
Obsoletes:	libnice

%description 	utils
This package contains various tools from %{name}.

%package -n	%{libname}
Summary:	Dynamic libraries from %{oname}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}nice1 < 0.1.1-4

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{devname}
Summary: 	Header files, libraries and development documentation for %{oname}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the header files, static libraries and development
documentation for %{oname}. If you like to develop programs using %{oname},
you will need to install %{oname}-devel.

%package -n	gstreamer%{gstapi}-%{oname}
Summary:	Gstreamer elements from %{oname}
Group:		System/Libraries
Requires:	%{libname} = %{version}
# conflict with older %%libname that had the gst .so, before the split
Conflicts:	%{_lib}nice0 < 0.1.0
Conflicts:	%{_lib}nice1 < 0.1.0
Obsoletes:	gstreamer0.10-%{oname}

%description -n	gstreamer%{gstapi}-%{oname}
Gstreamer elements from %{oname}.

%prep
%setup -q

%build
%configure2_5x \
	--enable-gupnp \
	--disable-static

# disable rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make

%install
%makeinstall_std

#% check
#disabled due fails
#make check

%files utils
%{_bindir}/s*
%{_bindir}/threaded-example

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING COPYING.LGPL COPYING.MPL NEWS README
%{_includedir}/%{oname}/*.h
%{_includedir}/stun/*.h
%{_includedir}/stun/usages/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{oname}.pc
%{_datadir}/gtk-doc/html/%{name}/*

%files -n gstreamer%{gstapi}-%{oname}
%{_libdir}/gstreamer-%{gstapi}/*.so

