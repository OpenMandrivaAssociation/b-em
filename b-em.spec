Name:		b-em
Summary:	B-em BBC Micro Emulator
Version:	2.2
Release:	4
Source0:	http://b-em.bbcmicro.com/B-emV%{version}Linux.tar.gz
Patch0:		gcc_error.patch
Patch1:		b-em-2.2-romloc.patch
URL:		http://b-em.bbcmicro.com/index.html
License:	Other
Group:		Emulators
BuildRequires:	freealut-devel 
BuildRequires:	openal-devel
BuildRequires:  allegro-devel

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

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=B-em
Comment=BBC Micro/Master Emulator
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Emulator;System;
EOF

%files
%_bindir/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
#%_iconsdir/%name.png
#%_liconsdir/%name.png
#%_miconsdir/%name.png

