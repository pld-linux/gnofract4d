Summary:	gnofract4d - GNOME-based program to draw fractals
Summary(pl):	gnofract4d - program do rysowania fraktali pod GNOME
Name:		gnofract4d
Version:	2.2
Release:	2
License:	BSD
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/gnofract4d/%{name}-%{version}.tar.gz
# Source0-md5:	358a769076292dd443daec668621a18f
# Source0-size:	424918
URL:		http://gnofract4d.sourceforge.net/
Patch0:		%{name}-desktop.patch
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
Requires:	python-pygtk-gtk >= 1:2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnofract 4D is a GNOME-based program to draw fractals. What sets it
apart from other fractal programs (and makes it "4D") is the way that
it treats the Mandelbrot and Julia sets as different views of the same
four-dimensional fractal object.

%description -l pl
Gnofract 4D jest program do rysowania fraktali pod GNOME. To, co
odró¿nia ten go od innych programów do fraktali (i czyni go "4D"), to
sposób, w jaki traktuje zbiory Mandelbrota i Julia - jako ró¿ne widoki
tego samego, czterowymiarowego obiektu fraktalnego.

%prep
%setup -q
%patch0 -p1

echo 'Categories=Graphics;' >> gnofract4d.desktop

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

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Graphics/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/gnofract4d-%{version}
%{_datadir}/formulas
%{_datadir}/maps
%{_pixmapsdir}/gnofract4d
%{_desktopdir}/gnofract4d.desktop
