Summary:	PNG to ICO converter
Summary(pl.UTF-8):   Konwerter PNG do ICO
Name:		pngtoico
Version:	1.0.1
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ftp.kernel.org/pub/software/graphics/pngtoico/%{name}-%{version}.tar.bz2
# Source0-md5:	991dfa42783f9b798051c04dccc7f36f
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pngtoico is a small utility to convert a set of PNG images to
Microsoft ICO format. Transparency is supported.

%description -l pl.UTF-8
pngtoico to małe narzędzie do konwertowania zestawu obrazków PNG do
formatu Microsoft ICO. Obsługuje przezroczystość.

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
