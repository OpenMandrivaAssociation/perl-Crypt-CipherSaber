%define module	Crypt-CipherSaber

Name:		perl-%{module}
Version:	1.00
Release:	12
Summary:	Perl module implementing CipherSaber encryption
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{module}-%{version}.tar.bz2
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::Simple) >= 0.60
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl-devel
BuildRequires:	perl(JSON::PP)
BuildConflicts:	perl(Module::Signature)
BuildArch:	noarch

%description
The Crypt::CipherSaber module implements CipherSaber encryption, described at
http://ciphersaber.gurus.com. It is simple, fairly speedy, and relatively
secure algorithm based on RC4.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/Crypt
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.00-10mdv2012.0
+ Revision: 765123
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.00-8
+ Revision: 667057
- mass rebuild

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 1.00-7mdv2011.0
+ Revision: 563897
- build conflicts with perl(Module::Signature), otherwise test will fail

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.00-7mdv2010.0
+ Revision: 426441
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.00-6mdv2009.0
+ Revision: 223580
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.00-5mdv2008.1
+ Revision: 136699
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-5mdv2007.0
- spec cleanup
- fix directory ownership

* Mon Aug 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-4mdk
- real buildrequires fix (thx spurtle)

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-3mdk
- Revert previous uncessary fix...

* Sun Jul 31 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.00-2mdk
- Fix BuildRequires

* Mon Jul 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdk
- New release 1.00
- make test
- spec cleanup

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.61-3mdk
- fix buildrequires in a backward compatible way

* Wed Jul 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.61-2mdk 
- rpmbuildupdate aware

* Tue Dec 16 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.61-1mdk
- first mdk release

