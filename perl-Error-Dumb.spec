#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Error
%define		pnam	Dumb
Summary:	Error::Dumb - simple error management for simple classes
Summary(pl.UTF-8):	Error::Dumb - uproszczone zarządzanie błędami w prostych klasach
Name:		perl-Error-Dumb
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b5b6892b76d18c0ab9b316d553fc3cc2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Error::Dumb Perl module is a base class that is meant to be inherited
by other classes. All this class provides is an interface for setting
and retrieving error messages.

%description -l pl.UTF-8
Moduł Perla Error::Dumb jest klasą bazową, po której dziedziczą inne
klasy. Klasa ta udostępnia jedynie interfejs do definiowania i
odczytywania komunikatów o błędach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Error/Dumb.pm
%{_mandir}/man3/*
