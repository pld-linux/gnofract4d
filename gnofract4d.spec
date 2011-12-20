Summary:	gnofract4d - GNOME-based program to draw fractals
Summary(pl.UTF-8):	gnofract4d - program do rysowania fraktali pod GNOME
Name:		gnofract4d
Version:	3.11
Release:	6
License:	BSD
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/gnofract4d/%{name}-%{version}.tar.gz
# Source0-md5:	c038702003c47fe58b7db1023302b855
URL:		http://gnofract4d.sourceforge.net/
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-libpng.patch
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires:	python-pygtk-gtk >= 1:2.0
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
%patch1 -p1

%build
sed -i -e "s#/usr/lib/%{name}-%{version}#%{_libdir}/%{name}-%{version}#g" \
	setup.cfg gnofract4d

CFLAGS="%{rpmcflags}" \
	python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database

%postun
%update_desktop_database_post
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*fract*
%{_datadir}/%{name}
%{_datadir}/mime/packages/*
%{_pixmapsdir}/gnofract4d
%{_pixmapsdir}/gnofract4d-logo.png
%{_desktopdir}/gnofract4d.desktop
