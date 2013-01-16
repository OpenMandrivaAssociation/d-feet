%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	D-Feet is a D-Bus debugger
Name:		d-feet
Version:	0.3.3
Release:	1
License:	GPLv2+
Group:		Emulators
Url:		http://fedorahosted.org/d-feet/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/d-feet/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	python-setuptools
BuildRequires:	wxPythonGTK
Requires:	python-dbus
Requires:	pygtk2.0-libglade

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
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%files
%doc AUTHORS COPYING README
%{python_sitelib}/*
%{_bindir}/%{name}
%{_datadir}/applications/dfeet.desktop
%{_datadir}/dfeet/
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg

