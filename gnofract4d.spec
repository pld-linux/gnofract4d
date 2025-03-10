Summary:	gnofract4d - GNOME-based program to draw fractals
Summary(pl.UTF-8):	gnofract4d - program do rysowania fraktali pod GNOME
Name:		gnofract4d
Version:	4.3
Release:	
License:	BSD
Group:		X11/Applications/Graphics
Source0:	https://github.com/fract4d/gnofract4d/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d815353c682eab9787e2fdad26f625ba
URL:		https://fract4d.github.io/gnofract4d/
Patch0:		%{name}-desktop.patch
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires:	python3-pygobject3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnofract 4D is a GNOME-based program to draw fractals. What sets it
apart from other fractal programs (and makes it "4D") is the way that
it treats the Mandelbrot and Julia sets as different views of the same
four-dimensional fractal object.

%description -l pl.UTF-8
Gnofract 4D jest program do rysowania fraktali pod GNOME. To, co
odróżnia ten go od innych programów do fraktali (i czyni go "4D"), to
sposób, w jaki traktuje zbiory Mandelbrota i Julia - jako różne widoki
tego samego, czterowymiarowego obiektu fraktalnego.

%prep
%setup -q
%patch0 -p1

%build
sed -i -e "s#/usr/lib/%{name}-%{version}#%{_libdir}/%{name}-%{version}#g" \
	setup.cfg gnofract4d

%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database

%postun
%update_desktop_database_post
%update_mime_database

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/*
%{py3_sitedir}/*fract*
%{_datadir}/%{name}
%{_datadir}/mime/packages/*
%{_pixmapsdir}/gnofract4d.png
%{_desktopdir}/gnofract4d.desktop
%{_iconsdir}/hicolor/*x*/apps/gnofract4d.png
