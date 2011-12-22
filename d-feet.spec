Name:		d-feet
Version:	0.1.14
Release:	%mkrel 3

Summary:	D-Feet is a D-Bus debugger
License:	GPLv2+
Group:		Emulators
URL:		http://fedorahosted.org/d-feet/
Source0:		http://download.gnome.org/sources/d-feet/0.1/%{name}-%{version}.tar.xz
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
%{_datadir}/dfeet/
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/applications/dfeet.desktop

