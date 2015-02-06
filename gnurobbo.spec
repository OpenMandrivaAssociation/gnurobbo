Summary:	Logic game ported from ATARI XE/XL
Name:		gnurobbo
Version:	0.66
Release:	3
License:	GPLv2+
Group:		Games/Arcade
Url:		http://gnurobbo.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/gnurobbo/%{name}-%{version}-source.tar.gz
Source10:	%{name}.16.png.bz2
Source11:	%{name}.32.png.bz2
Source12:	%{name}.48.png.bz2
Patch0:		gnurobbo-0.66.libm.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)

%description
GNU Robbo is very addictive logic game. You must help little robot to get out
of unfriendly planet, collecting parts of emergency capsule.

%files
%doc README ChangeLog AUTHORS
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%make PACKAGE_DATA_DIR=%{_datadir}/%{name}

%install
%makeinstall \
	BINDIR=%{buildroot}%{_bindir} \
	PACKAGE_DATA_DIR=%{buildroot}%{_datadir}/%{name} \
	DOCDIR=%{buildroot}%{_docdir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=GNU Robbo
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

mkdir -p %{buildroot}%{_miconsdir}
mkdir -p %{buildroot}%{_liconsdir}
bzcat %{SOURCE10} > %{buildroot}%{_miconsdir}/%{name}.png
bzcat %{SOURCE11} > %{buildroot}%{_iconsdir}/%{name}.png
bzcat %{SOURCE12} > %{buildroot}%{_liconsdir}/%{name}.png

