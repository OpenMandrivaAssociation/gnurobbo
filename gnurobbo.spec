Summary:	Logic game ported from ATARI XE/XL
Name:		gnurobbo
Version:	0.68
Release:	1
License:	GPLv2+
Group:		Games/Arcade
Url:		https://gnurobbo.sourceforge.net
Source0:	https://downloads.sourceforge.net/project/gnurobbo/gnurobbo/gnurobbo%20%{version}/gnurobbo-%{version}-source.tar.gz
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)

%description
GNU Robbo is very addictive logic game. You must help little robot to get out
of unfriendly planet, collecting parts of emergency capsule.

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%doc %{_docdir}/gnurobbo

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}
sed -i -e 's|-Wall|-Wall %{optflags} -fcommon -Wno-error=format-security|' Makefile

%build
%make_build PACKAGE_DATA_DIR=%{_datadir}/%{name}

%install
%makeinstall \
	BINDIR=%{buildroot}%{_bindir} \
	PACKAGE_DATA_DIR=%{buildroot}%{_datadir}/%{name} \
	DOCDIR=%{buildroot}%{_docdir}/%{name}

for i in 16 32 48; do
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
	cp icons/gnurobbo.${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/gnurobbo.png
done

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
