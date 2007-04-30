%define name	gnurobbo
%define version	0.57
%define release	5mdk

Summary: GNU Robbo is logic game ported from ATARI XE/XL
Name:      %{name}
Version:   %{version}
Release:   %{release}
License: GPL
Group: Games/Arcade
Source: http://prdownloads.sourceforge.net/gnurobbo/%{name}-%{version}.tar.bz2
Source10: %{name}.16.png.bz2
Source11: %{name}.32.png.bz2
Source12: %{name}.48.png.bz2

URL: http://gnurobbo.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-buildroot

BuildRequires: libSDL-devel
BuildRequires: libSDL_ttf-devel
Requires: libSDL1.2 >= 1.2.5
Requires: SDL_ttf >= 2.0.5

%description
GNU Robbo is very addictive logic game. You must help
little robot to get out of unfriendly planet, collecting
parts of emergency capsule.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT/%{_menudir}

cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%{name}
?package(%{name}):\ 
        needs="x11" \
        section="More Applications/Games/Arcade" \
        title="GNU Robbo" \
        longtitle="Logic game" \
        command="%{_bindir}/%{name}" \
        icon="%{name}.png"
EOF

mkdir -p $RPM_BUILD_ROOT/%{_miconsdir}
mkdir -p $RPM_BUILD_ROOT/%{_liconsdir}
bzcat %{SOURCE10} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
bzcat %{SOURCE11} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
bzcat %{SOURCE12} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%{name}
%{_menudir}/*
%defattr(644,root,root,755)
%doc README COPYING ChangeLog AUTHORS INSTALL
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
