Summary:	PNG to ICO converter
Name:		pngtoico
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ftp.kernel.org/pub/software/graphics/pngtoico/%{name}-%{version}.tar.bz2
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pngtoico is a small utility to convert a set of PNG images to
Microsoft ICO format. Transparency is supported.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install pngtoico $RPM_BUILD_ROOT%{_bindir}
install pngtoico.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pngtoico
%{_mandir}/man1/pngtoico.1*
