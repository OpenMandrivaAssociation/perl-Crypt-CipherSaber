%define module	Crypt-CipherSaber

Summary:	Perl module implementing CipherSaber encryption
Name:		perl-%{module}
Version:	1.00
Release:	16
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::Simple) >= 0.60
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl-devel
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(Digest::SHA)

%description
The Crypt::CipherSaber module implements CipherSaber encryption, described at
http://ciphersaber.gurus.com. It is simple, fairly speedy, and relatively
secure algorithm based on RC4.

%prep
%setup -qn %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#Remove the debug files which get created, causing failure of the contents check
rm debug*.list
make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/Crypt
%{_mandir}/man3/*

