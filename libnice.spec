%define	major	0
%define	oname	nice
%define	libname		%mklibname %{oname} %major
%define develname	%mklibname %{oname} -d

Name:		libnice
Version:	0.0.6
Release:	%mkrel 1
Summary:	Implementation of the IETF's draft Interactive Connectivity Establishment standard
License:	GPLv2+
Group:		System/Libraries
URL:		http://nice.freedesktop.org/wiki/
Source:		http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	libgstreamer-plugins-base-devel
Buildrequires:	gtk-doc
Requires:	%{libname} = %{version}


%description
Nice is an implementation of the IETF's draft Interactive Connectivity Establishment
standard (ICE). It provides GLib-based library, libnice.

ICE is useful for applications that want to establish peer-to-peer UDP data streams.
It automates the process of traversing NATs and provides security against some attacks.

Existing standards that use ICE include the Session Initiation Protocol (SIP) and Jingle,
XMPP extension for audio/video calls.

Nice includes integration with GStreamer. It is used by Farsight for RTP transport. 

%package -n	%{libname}
Summary:	Dynamic libraries from %{oname}
Group:		System/Libraries
Provides: 	%{name} = %{version}-%{release}

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary: 	Header files, libraries and development documentation for %{oname}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{oname}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the header files, static libraries and development
documentation for %{oname}. If you like to develop programs using %{oname},
you will need to install %{oname}-devel.

%prep
%setup -q 

%build
#autoreconf -fiv
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/stun*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
%{_libdir}/gstreamer-0.10/*.so

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/%{oname}/*.h
%{_includedir}/stun/*.h
%{_includedir}/stun/usages/*.h
%{_libdir}/%{name}.a
%{_libdir}/%{name}.la
%{_libdir}/%{name}.so
%{_libdir}/gstreamer-0.10/*.a
%{_libdir}/gstreamer-0.10/*.la
%{_libdir}/pkgconfig/%{oname}.pc
%{_datadir}/gtk-doc/html/%{name}/*

