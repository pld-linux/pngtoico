Summary: PNG to ICO converter
Name: pngtoico
Version: 1.0
Release: 1
Source: pngtoico-%{version}.tar.bz2
License: GPL
Group: Applications/Multimedia

%description
pngtoico is a small utility to convert a set of PNG images to
Microsoft ICO format. Transparency is supported.

%prep
%setup -q

%build
make

%install
make prefix=/usr install

%files
%defattr(-,root,root)
/usr/bin/pngtoico
/usr/man/man1/pngtoico.1

%changelog
* Wed Jan 16 2002 Wesley Tanaka <wtanaka@users.sourceforge.net>
- initial packaging
