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



%changelog
* Thu Dec 22 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.1.14-3mdv2011.0
+ Revision: 744505
- version update 0.1.14

* Mon Feb 28 2011 Joao Victor Duarte Martins <jvdm@mandriva.com.br> 0.1.10-3
+ Revision: 640696
- Fix missing require (pygtk2.0-libglade)

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.1.10-2mdv2011.0
+ Revision: 592392
- rebuild for python 2.7

* Wed Jul 08 2009 Frederik Himpe <fhimpe@mandriva.org> 0.1.10-1mdv2010.0
+ Revision: 393629
- BuildRequires: python-setuptools
- Update to new version 1.10.0
- Fix source URL

* Tue Jan 27 2009 Guillaume Bedot <littletux@mandriva.org> 0.1.8-2mdv2009.1
+ Revision: 333947
- bump rel, submit again
- First package of D-Feet for Mandriva
- create d-feet

