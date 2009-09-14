# $Id$
# Authority: dag
# Upstream: Aaron Crane <cpan$aaroncrane,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-PgPP

Summary: Perl module provides a pure Perl PostgreSQL driver for DBI
Name: perl-DBD-PgPP
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-PgPP/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-PgPP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(DBI) >= 1.59
BuildRequires: perl(Test::More)


%description
perl-DBD-PgPP is a Perl module provides a pure Perl PostgreSQL driver for DBI.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/DBD::PgPP.3pm*
%dir %{perl_vendorlib}/DBD/
%{perl_vendorlib}/DBD/PgPP.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.07-1
- Updated to version 0.07.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 0.06-1
- Updated to version 0.06.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
