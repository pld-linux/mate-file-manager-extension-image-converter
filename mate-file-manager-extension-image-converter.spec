Summary:	Caja (MATE file manager) extension to mass resize or rotate images
Summary(pl.UTF-8):	Rozszerzenie zarządcy plików Caja pozwalające masowo zmieniać rozmiar i obracać pliki graficzne
Name:		mate-file-manager-extension-image-converter
Version:	1.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.6/mate-file-manager-image-converter-%{version}.tar.xz
# Source0-md5:	9af61933104bf154219ee64a2649d154
URL:		http://www.bitron.ch/software/mate-file-manager-image-converter.php
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	mate-file-manager-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	ImageMagick
Requires:	glib2 >= 1:2.28.0
Requires:	gtk+2 >= 2:2.12.0
Requires:	mate-file-manager >= 1.1.0
Suggests:	ImageMagick-coder-jpeg
Suggests:	ImageMagick-coder-jpeg2
Suggests:	ImageMagick-coder-png
Suggests:	ImageMagick-coder-tiff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Caja-Image-Converter extension allows you to resize/rotate images
from Caja (MATE file manager).

Caja-Image-Converter is a fork of Nautilus-Image-Converter.

%description -l pl.UTF-8
Rozszerzenie Caja-Image-Converter pozwala na zmianę rozmiaru i
obracanie rozmiarów obrazów z poziomu zarządców plików Caja,
przeznaczonego dla środowiska MATE.

Caja-Image-Converter to odgałęzienie rozszerzenia
Nautilus-Image-Converter.

%prep
%setup -q -n mate-file-manager-image-converter-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la

%find_lang caja-image-converter

%clean
rm -rf $RPM_BUILD_ROOT

%files -f caja-image-converter.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja-image-converter
