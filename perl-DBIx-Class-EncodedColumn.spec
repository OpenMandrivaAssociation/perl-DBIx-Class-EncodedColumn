%define upstream_name    DBIx-Class-EncodedColumn
%define upstream_version 0.00006

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Encrypt columns using Crypt::OpenPGP
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBIx::Class)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(SQL::Translator)
BuildRequires: perl(Sub::Name)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


