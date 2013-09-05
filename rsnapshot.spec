%include	/usr/lib/rpm/macros.perl

Summary:	Local and remote filesystem snapshot utility
Name:		rsnapshot
Version:	1.3.1
Release:	3
License:	GPL v2+
Group:		Daemons
Source0:	http://www.rsnapshot.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	588f92995dcf60a6ea6df8d94a017e7e
Patch0:		%{name}-config.patch
Patch1:		%{name}-configure.patch
URL:		http://www.rsnapshot.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpm-perlprov
BuildArch:	noarch
Requires:	perl-lchown
Requires:	rsync
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Local and remote filesystem snapshot utility.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-rsync=%{_bindir}/rsync	\
	--with-ssh=%{_bindir}/ssh
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf{.default,}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/rsnapshot
%attr(755,root,root) %{_bindir}/rsnapshot-diff
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rsnapshot.conf
%{_mandir}/man1/rsnapshot.1*
%{_mandir}/man1/rsnapshot-diff.1*

