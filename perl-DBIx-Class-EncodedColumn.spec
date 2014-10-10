%define upstream_name    DBIx-Class-EncodedColumn
%define upstream_version 0.00011

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Encrypt columns using Crypt::OpenPGP
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Dir::Self)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(SQL::Translator)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
This the DBIx::Class manpage component can be used to automatically encode
a column's contents whenever the value of that column is set.

This module is similar to the existing the DBIx::Class::DigestColumns
manpage, but there is some key differences:

* 'DigestColumns' performs the encode operation on 'insert' and 'update',
  and 'EncodedColumn' performs the operation when the value is set, or on
  'new'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.110-1mdv2011.0
+ Revision: 654061
- update to new version 0.00011

* Tue Aug 31 2010 Jérôme Quelin <jquelin@mandriva.org> 0.0.100-1mdv2011.0
+ Revision: 574800
- adding missing buildrequires:
- update to 0.00010

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.0.90-1mdv2011.0
+ Revision: 554272
- update to 0.00009

* Sat Jan 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.0.60-1mdv2010.1
+ Revision: 492158
- update to 0.00006

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.0.50-1mdv2010.1
+ Revision: 471085
- import perl-DBIx-Class-EncodedColumn


* Sun Nov 29 2009 cpan2dist 0.00005-1mdv
- initial mdv release, generated with cpan2dist
