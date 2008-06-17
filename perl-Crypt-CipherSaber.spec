%define module	Crypt-CipherSaber
%define name	perl-%{module}
%define version 1.00
%define release %mkrel 6

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Perl module implementing CipherSaber encryption
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}
Source:		    http://www.cpan.org/modules/by-module/Crypt/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Test::Warn)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
The Crypt::CipherSaber module implements CipherSaber encryption, described at
http://ciphersaber.gurus.com. It is simple, fairly speedy, and relatively
secure algorithm based on RC4.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Crypt
%{_mandir}/*/*

