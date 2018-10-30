%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME Search tool
Name:		gnome-search-tool
Version:	3.6.0
Release:	12
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(sm)
Conflicts:	gnome-utils < 1:3.3.1

%description
Search tool for Gnome desktop.

%prep
%setup -q

%build
%configure2_5x \
	--disable-schemas-compile \
	--disable-schemas-install \
	--disable-scrollkeeper
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/gsearchtool/thumbnail_frame.png
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-search-tool.gschema.xml
%{_datadir}/GConf/gsettings/gnome-search-tool.convert
%{_mandir}/man1/%{name}.1*

