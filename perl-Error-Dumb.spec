#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Error
%define		pnam	Dumb
Summary:	Error::Dumb Perl module for simple error management for simple classes
Summary(pl):	Modu³ Perla Error::Dumb do uproszczonego zarz±dzania b³êdami w prostych klasach
Name:		perl-Error-Dumb
Version:	0.02
Release:	1
License:	-
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
#URL:		-
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Error::Dumb Perl module is a base class that is meant to be inherited
by other classes. All this class provides is an interface for setting
and retrieving error messages.

%description -l pl
Modu³ Perla Error::Dumb jest klas± bazow±, po której dziedzicz± inne
klasy. Klasa ta udostêpnia jedynie interfejs do definiowania i
odczytywania komunikatów o b³êdach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Error/Dumb.pm
%{_mandir}/man3/*
