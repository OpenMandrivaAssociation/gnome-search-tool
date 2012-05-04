%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-search-tool
Version:	3.4.0
Release:	%mkrel 1
Summary:	GNOME Search tool
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(sm)
Conflicts:	gnome-utils < 1:3.3.1

%description
Search tool for Gnome desktop.

%prep
%setup -q

%build
%configure2_5x \
	--disable-rpath \
	--disable-schemas-compile \
	--disable-schemas-install \
	--disable-scrollkeeper
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name} --with-gnome

for omf in %{buildroot}%{_datadir}/omf/*/*-*-*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%{buildroot}!!)" >> %{name}.lang
done

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%doc NEWS AUTHORS
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/gsearchtool/thumbnail_frame.png
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/omf/%{name}/
%{_datadir}/omf/%{name}/%{name}-C.omf


