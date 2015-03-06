%define	name	b-em
%define bin_name B-em
%define	version	2.2
%define	release	1
%define	summary B-em BBC Micro Emulator

Name:		%{name}
Summary:	%{summary}
Version:	%{version}
Release:	%{release}
Source0:	http://b-em.bbcmicro.com/%{bin_name}V%{version}Linux.tar.gz
Patch0:		gcc_error.patch
Patch1:		b-em-2.2-romloc.patch
URL:		http://b-em.bbcmicro.com/index.html
License:	Other
Group:		Emulators
BuildRoot:	 %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	freealut-devel 
BuildRequires:	openal-devel
BuildRequires:  allegro-devel

%description
A Freeware BBC Micro Emulator for DOS, Windows and Mac OS X.

%prep
%setup -q -c %{name}-%{version}
%patch0
%patch1 -p1

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -R roms %{buildroot}/%{_datadir}/%{name}
cp -R tapes %{buildroot}/%{_datadir}/%{name}
cp -R discs %{buildroot}/%{_datadir}/%{name}
cp -R ddnoise %{buildroot}/%{_datadir}/%{name}
chmod -R 755 %{buildroot}/%{_datadir}/%{name}

# Mandriva menu entry

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=B-em
Comment=BBC Micro/Master Emulator
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Emulator;System;
EOF

%clean
rm -rf %{buildroot}

%files
%_bindir/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/mandriva-%{name}.desktop
#%_iconsdir/%name.png
#%_liconsdir/%name.png
#%_miconsdir/%name.png

