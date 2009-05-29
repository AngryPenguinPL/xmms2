%define funny_version DrMattDestruction

%define major 0
%define libname %mklibname xmms2_ %{major}
%define develname %mklibname -d xmms2

%define libclient %mklibname xmmsclient 5
%define libclientglib %mklibname xmmsclient-glib 1
%define libclientecore %mklibname xmmsclient-ecore 1
%define libclientpp %mklibname xmmsclient++ 3
%define libclientppglib %mklibname xmmsclient++-glib 1

Summary:	Redesign of the XMMS music player
Name:		xmms2
Version:	0.6
Release:	%mkrel 0.%{funny_version}.1
Group:          Sound
License:        GPLv2+
URL:            http://xmms2.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/xmms2/%{name}-%{version}%{funny_version}.tar.bz2
Patch0:		xmms2-lib64_fix.diff
Patch1:		01_gcc4.3.patch
Patch3:		xmms2-0.6-prefer-pulse.patch
Patch5:		xmms2-0.5-string-format.diff
Patch6:		xmms2-0.6-lib64.patch
BuildRequires:	rpm-manbo-setup-build >= 2-12
BuildRequires:	alsa-lib-devel
BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	boost-devel
BuildRequires:	curl-devel >= 7.11.2
BuildRequires:	ecore-devel
BuildRequires:	expat-devel
BuildRequires:	fftw3-devel
BuildRequires:	glib2-devel >= 2.8.0
BuildRequires:	libao-devel
BuildRequires:	libavahi-common-devel
BuildRequires:	libavahi-glib-devel
BuildRequires:	libcdio-devel
BuildRequires:	libdbus-devel
BuildRequires:	libdbus-glib-devel
BuildRequires:	libdiscid-devel
BuildRequires:	libesound-devel
BuildRequires:	libffmpeg-devel
#BuildRequires:	libflac-devel
BuildRequires:	libgamin-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libgnome-vfs2-devel
BuildRequires:	libjack-devel
BuildRequires:	libmad-devel
BuildRequires:	libmms-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libmpg123-devel >= 1.5.1
BuildRequires:	libofa-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libshout-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libvisual-devel
BuildRequires:	libxml2-devel
BuildRequires:	mad-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	python-devel >= 2.3.0
BuildRequires:	python-pyrex >= 0.9.3
BuildRequires:	ruby-devel >= 1.8
BuildRequires:	SDL_ttf-devel
BuildRequires:	sidplay2-devel
BuildRequires:	speex-devel
BuildRequires:	sqlite3-devel >= 3.2.4
BuildRequires:	swig >= 1.3.25
BuildRequires:	zlib-devel
BuildRequires:  libflac-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

%package -n    %{libclient}
Summary:       Library associated with xmms2, needed for xmms2 and its plugins
Group:         System/Libraries
Obsoletes:     %{libname}

%description -n        %{libclient}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n    %{libclientglib}
Summary:       Library associated with xmms2, needed for xmms2 and its plugins
Group:         System/Libraries
Obsoletes:     %{libname}

%description -n        %{libclientglib}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n    %{libclientecore}
Summary:       Library associated with xmms2, needed for xmms2 and its plugins
Group:         System/Libraries
Obsoletes:     %{libname}

%description -n        %{libclientecore}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n    %{libclientpp}
Summary:       Library associated with xmms2, needed for xmms2 and its plugins
Group:         System/Libraries
Obsoletes:     %{libname}

%description -n        %{libclientpp}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n    %{libclientppglib}
Summary:       Library associated with xmms2, needed for xmms2 and its plugins
Group:         System/Libraries
Obsoletes:     %{libname}

%description -n        %{libclientppglib}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n	%{develname}
Summary:	Development package with static libs and headers
Group:		Development/C
Requires:	%{libclient} = %{version}-%{release}
Requires:	%{libclientglib} = %{version}-%{release}
Requires:	%{libclientecore} = %{version}-%{release}
Requires:	%{libclientpp} = %{version}-%{release}
Requires:	%{libclientppglib} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n	%{develname}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

Static libraries and header files required for compiling xmms2 plugins.

%package -n	python-%{name}
Summary:	Python bindings for XMMS2
Group:		Development/Python
#Requires:	%{name}-client = %{version}
Provides:	%{name}-python = %{version}
Obsoletes:	%{name}-python

%description -n	python-%{name}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This package contains files providing Python bindings for accessing XMM2.

%package -n	ruby-%{name}
Summary:	Ruby bindings for XMMS2
Group:		Development/Ruby
#Requires:	%{name}-client = %{version}
Provides:	%{name}-ruby = %{version}
Obsoletes:	%{name}-ruby

%description -n	ruby-%{name}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This package contains files providing Ruby bindings for accessing XMM2.

%package -n	perl-%{name}
Summary:	Perl bindings for XMMS2
Group:		Development/Perl
#Requires:	%{name}-client = %{version}

%description -n	perl-%{name}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This package contains files providing Perl bindings for accessing XMM2.

%prep
%setup -q -n %{name}-%{version}%{funny_version}
%patch1 -p1
%patch3 -p0
%patch5 -p0
%if "%_lib" = "lib64"
%patch6 -p0
%endif

%build
%setup_compile_flags
./waf configure \
    --prefix=%{_prefix} \
    --with-libdir=%{_libdir} \
    --with-pkgconfigdir=%{_libdir}/pkgconfig \
    --destdir=%{buildroot} \
    --with-mandir=%{_mandir} \
    --with-ruby-archdir=%{ruby_sitearchdir} \
    --with-ruby-libdir=%{ruby_sitelibdir} \
    --with-perl-archdir=%{perl_vendorarch}

./waf build %{_smp_mflags}

%install
rm -rf %{buildroot}

./waf install \
    --destdir=%{buildroot}

# cleanup
#rm -f %{buildroot}%{_datadir}/xmms2/mind.in.a.box-lament_snipplet.ogg

# fix borked version
perl -pi -e "s|^Version:.*|Version: %{version} %{funny_version}|g" %{buildroot}%{_libdir}/pkgconfig/*.pc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %{_bindir}/vistest
%attr(0755,root,root) %{_bindir}/vistest-fft
%attr(0755,root,root) %{_bindir}/xmms2
%attr(0755,root,root) %{_bindir}/xmms2d
%attr(0755,root,root) %{_bindir}/xmms2-et
%attr(0755,root,root) %{_bindir}/xmms2-find-avahi
%attr(0755,root,root) %{_bindir}/xmms2-launcher
%attr(0755,root,root) %{_bindir}/xmms2-libvisual
%attr(0755,root,root) %{_bindir}/xmms2-mdns-avahi
%attr(0755,root,root) %{_bindir}/xmms2-mlib-updater
%attr(0755,root,root) %{_bindir}/xmms2-ripper

# plugins
%dir %{_libdir}/xmms2
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_airplay.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_alsa.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_ao.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_apefile.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_asf.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_asx.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_avcodec.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_cdda.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_cue.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_curl.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_daap.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_diskwrite.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_equalizer.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_file.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_flac.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_flv.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_gme.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_gvfs.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_html.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_ices.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_icymetaint.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_id3v2.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_jack.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_karaoke.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_m3u.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_mad.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_mms.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_modplug.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_mp4.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_mpg123.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_musepack.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_normalize.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_null.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_nulstripper.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_ofa.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_oss.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_pls.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_pulse.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_replaygain.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_rss.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_samba.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_sid.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_speex.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_tta.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_wave.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_vocoder.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_vorbis.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_xml.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_xspf.so

%dir %{_datadir}/xmms2
%dir %{_datadir}/xmms2/scripts
%dir %{_datadir}/xmms2/scripts/startup.d
%attr(0755,root,root) %{_datadir}/xmms2/scripts/startup.d/*sh
%attr(0644,root,root) %{_datadir}/xmms2/mind.in.a.box-lament_snipplet.ogg

%attr(0644,root,root) %{_datadir}/pixmaps/xmms2-128.png
%attr(0644,root,root) %{_datadir}/pixmaps/xmms2-16.png
%attr(0644,root,root) %{_datadir}/pixmaps/xmms2-32.png
%attr(0644,root,root) %{_datadir}/pixmaps/xmms2-48.png
%attr(0644,root,root) %{_datadir}/pixmaps/xmms2-black-on-white.svg
%attr(0644,root,root) %{_datadir}/pixmaps/xmms2-white-on-black.svg
%attr(0644,root,root) %{_datadir}/pixmaps/xmms2.svg

%{_mandir}/man1/xmms2.1*
%{_mandir}/man1/xmms2-et.1*
%{_mandir}/man1/xmms2-launcher.1*
%{_mandir}/man1/xmms2-mdns-avahi.1*
%{_mandir}/man1/xmms2d.1*

%files -n %{libclient}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/libxmmsclient.so.5*

%files -n %{libclientglib}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/libxmmsclient-glib.so.1*

%files -n %{libclientecore}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/libxmmsclient-ecore.so.1*

%files -n %{libclientpp}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/libxmmsclient++.so.3*

%files -n %{libclientppglib}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/libxmmsclient++-glib.so.1*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/xmms2
%attr(0755,root,root) %{_libdir}/lib*.so
%attr(0644,root,root) %{_libdir}/pkgconfig/*.pc

%files -n ruby-%{name}
%defattr(-,root,root,-)
%attr(0755,root,root) %dir %{ruby_sitelibdir}/xmmsclient
%attr(0644,root,root) %{ruby_sitelibdir}/xmmsclient/*.rb
%attr(0755,root,root) %{ruby_sitearchdir}/*.so
%attr(0644,root,root) %{ruby_sitelibdir}/xmmsclient.rb

%files -n python-%{name}
%defattr(-,root,root,-)
%attr(0755,root,root) %dir %{python_sitearch}/xmmsclient
%{python_sitearch}/xmmsclient/*.so
%{python_sitearch}/xmmsclient/*.py

%files -n perl-%{name}
%defattr(-,root,root,-)
%attr(0644,root,root) %{perl_vendorarch}/Audio/*.pm
%attr(0755,root,root) %{perl_vendorarch}/auto/Audio/XMMSClient/XMMSClient.so
