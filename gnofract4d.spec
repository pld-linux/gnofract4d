Summary:	gnofract4d - Gnome-based program to draw fractals
Summary(pl):	gnofract4d - program do rysowania fraktali pod Gnome
Name:		gnofract4d
Version:	1.6
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/gnofract4d/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-AM_CXXFLAGS.patch
URL:		http://gnofract4d.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnofract 4D is a Gnome-based program to draw fractals. What sets it
apart from other fractal programs (and makes it "4D") is the way that
it treats the Mandelbrot and Julia sets as different views of the same
four-dimensional fractal object.

%description -l pl
Gnofract 4D jest program do rysowania fraktali pod Gnome. To, co
odró¿nia ten go od innych programów do fraktali (i czyni go "4D"), to
sposób, w jaki traktuje zbiory Mandelbrota i Julia - jako ró¿ne widoki
tego samego, czterowymiarowego obiektu fraktalnego.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%{__gettextize}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/maps
%{_pixmapsdir}/*
%{_applnkdir}/Graphics/gnofract4d.desktop
