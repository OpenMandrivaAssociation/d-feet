%define	debug_package %{nil}
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	D-Bus debugger
Name:		d-feet
Version:	0.3.14
Release:	1
License:	GPLv2+
Group:		Emulators
Url:		http://fedorahosted.org/d-feet/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/d-feet/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	gtk+3.0-devel >= 3.9.4
BuildRequires:	gobject-introspection-devel
BuildRequires:	python-setuptools
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	gnome-common
BuildRequires:	yelp-tools
BuildRequires:	yelp
Requires:	python-dbus
Requires:	typelib(Gtk) = 3.0
%description
D-Feet is a D-Bus debugger written in PyGtk by John (J5) Palmieri.

It allows :
* to view names on any bus,
* to view exported objects, interfaces, methods and signals,
* to view the full command line of services on the bus,
* and to execute methods with parameters on the bus and see their 
 return values.

%prep
%setup -q

%build
%configure --disable-tests
%make_build

%install
%make_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{python_sitelib}/*
%{_bindir}/%{name}
%{_datadir}/applications/d-feet.desktop
%{_datadir}/d-feet/
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_datadir}/appdata/d-feet.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.d-feet.gschema.xml
%{_iconsdir}/HighContrast/*/apps/*.svg

