Name:		b-em
Summary:	B-em BBC Micro Emulator
Version:	2.2
Release:	5
Source0:	http://b-em.bbcmicro.com/B-emV%{version}Linux.tar.gz
Source1:	b-em.png
Source2:	b-em.svg
Patch0:		gcc_error.patch
Patch1:		b-em-2.2-romloc.patch
Patch2:		b-em-2.2-cfg.patch
URL:		https://b-em.bbcmicro.com/index.html
License:	Other
Group:		Emulators
BuildRequires:	freealut-devel 
BuildRequires:	openal-devel
BuildRequires:  allegro-devel
BuildRequires:	zlib-devel

%description
A Freeware BBC Micro Emulator for DOS, Windows and Mac OS X.

%prep
%autosetup -p1 -c %{name}-%{version}

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
%make_build

%install
%old_makeinstall
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -R roms %{buildroot}/%{_datadir}/%{name}
cp -R tapes %{buildroot}/%{_datadir}/%{name}
cp -R discs %{buildroot}/%{_datadir}/%{name}
cp -R ddnoise %{buildroot}/%{_datadir}/%{name}
chmod -R 755 %{buildroot}/%{_datadir}/%{name}

# Mandriva menu entry

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=B-em
Comment=BBC Micro/Master Emulator
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Emulator;System;
EOF

install -D %SOURCE1 %{buildroot}%_iconsdir/hicolor/48x48/apps/%name.png
install -D %SOURCE2 %{buildroot}%_iconsdir/hicolor/scalable/apps/%name.svg


%files
%_bindir/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%_iconsdir/hicolor/*/apps/%name.*

