Summary:	gnofract4d - Gnome-based program to draw fractals
Summary(pl):	gnofract4d - program do rysowania fraktali pod Gnome
Name:		gnofract4d
Version:	1.4
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://download.sourceforge.net/pub/sourceforge/gnofract4d/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://gnofract4d.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Gnofract 4D is a Gnome-based program to draw fractals. What sets it
apart from other fractal programs (and makes it "4D") is the way that
it treats the Mandelbrot and Julia sets as different views of the same
four-dimensional fractal object.

%description -l pl
Gnofract 4D jest program do rysowania fraktali pod Gnome.

%prep
%setup -q
%patch -p1

%build
aclocal -I macros
autoconf
automake -a -c
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics

gzip -9nf README ChangeLog NEWS AUTHORS

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/maps
%{_pixmapsdir}/*
%{_applnkdir}/Graphics/gnofract4d.desktop
