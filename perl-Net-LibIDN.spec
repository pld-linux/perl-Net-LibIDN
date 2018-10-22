#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Net
%define		pnam	LibIDN
%include	/usr/lib/rpm/macros.perl
Summary:	This module provides Perl bindings for GNU Libidn
Summary(pl.UTF-8):	Wiązania Libidn dla Perla	
Name:		perl-Net-LibIDN
Version:	0.12
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c3e4de2065009d67bcb1df0afb473e12
URL:		http://search.cpan.org/dist/Net-LibIDN/
BuildRequires:	libidn-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl bindings for GNU Libidn by Simon Josefsson
(http://www.gnu.org/software/libidn/)

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/*.pm
%dir %{perl_vendorarch}/auto/Net/LibIDN
%{perl_vendorarch}/auto/Net/LibIDN/*.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Net/LibIDN/*.so
%{_mandir}/man3/*
