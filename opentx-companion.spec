
Summary: OpenTX Companion
Name: opentx-companion

Version: 2.3.13
Release: 1%{?dist}
License: GPLv2
URL: http://www.open-tx.org
Source0: https://github.com/opentx/opentx/archive/release/%{version}.tar.gz#/opentx-%{version}.tar.gz
Source1: https://github.com/MikeBland/OpenRcBootloader/releases/download/V1.9/bootflash4.lbm
Source2: https://github.com/MikeBland/OpenRcBootloader/releases/download/V1.9/bootflash8.lbm
Patch1: opentx-cmake-2.2.1.patch
Patch2: opentx-desktop-2.2.0.patch
Patch3: opentx-OpenRcBootloader-local.patch

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: qt5-qttools-devel, qt5-qtsvg-devel, qt5-qtmultimedia-devel
BuildRequires: fox-devel
BuildRequires: SDL-devel
BuildRequires: arm-none-eabi-gcc-cs-c++
BuildRequires: arm-none-eabi-newlib
BuildRequires: python3-pillow
BuildRequires: llvm-googletest
Requires: dfu-util

%description
OpenTX Companion transmitter support software is used for many different
tasks like loading OpenTX firmware to the radio, backing up model
settings, editing settings and running radio simulators. 

%prep
%setup -n opentx-release-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
rm -rf build-debug
mkdir -p build-debug/radio/src
cp %SOURCE1 %SOURCE2 build-debug/radio/src/

%build
cd build-debug
CMAKE_OPTS="-DGVARS=YES -DLUA=YES -DDEBUG=YES -DCMAKE_BUILD_TYPE=Debug -DBUILD_SHARED_LIBS:BOOL=OFF -DGTEST_ROOT=%{_datarootdir}/llvm/src/utils/unittest/googletest"
%define __cmake_in_source_build 1
%cmake $CMAKE_OPTS ../
%make_build opentx-companion
%make_build opentx-simulator
%make_build all-simu-libs
%cmake $CMAKE_OPTS -DPCB=X10 -DPCBREV=T16 ../
%make_build libsimulator

%install
make -C build-debug install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/opentx-companion
%{_bindir}/opentx-simulator
%{_libdir}/opentx-companion-23/
%{_prefix}/lib/udev/rules.d/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*

%changelog
* Thu Jun 24 2021 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.13-1
- Rebase to 2.3.13.

* Tue Jun 15 2021 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.12-1
- Rebase to 2.3.12.

* Sat Jan 09 2021 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.11-1
- Rebase to 2.3.11.

* Fri Oct 16 2020 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.10-1
- Rebase to 2.3.10.

* Mon Jun 15 2020 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.9-1
- Rebase to 2.3.9.

* Sat Jun 13 2020 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.8-1
- Rebase to 2.3.8.

* Sat Apr 18 2020 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.7-3
- Enable building simulator of Jumper T16.

* Sun Mar 29 2020 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.7-1
- Rebase to 2.3.7.

* Sun Jan 19 2020 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.5-1
- Rebase to 2.3.5.

* Fri Dec 27 2019 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.4-1
- Rebase to 2.3.4.

* Sat Dec 21 2019 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.3-1
- Rebase to 2.3.3.

* Sat Nov 16 2019 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.2-2
- Rebase to 2.3.2.

* Sat Oct 05 2019 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.1-1
- Rebase to 2.3.1.

* Sat Sep 28 2019 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.0-1
- Rebase to 2.3.0 GA.

* Sun Sep 15 2019 Jan Pazdziora <jpx-opentx@adelton.com> - 2.3.0-RC3.1
- Test build of 2.3.0-RC3.

* Fri Jul 12 2019 Jan Pazdziora <jpx-opentx@adelton.com> - 2.2.4-1
- Rebase to 2.2.4 release.

* Fri Jul 12 2019 Jan Pazdziora <jpx-opentx@adelton.com> - 2.2.3-1
- Address compile errors on Fedora 30+.
- Rebase to 2.2.3 release.

* Sun Sep 30 2018 Jan Pazdziora <jpx-opentx@adelton.com> - 2.2.2-1
- Rebase to 2.2.2 release.

* Sun Sep 30 2018 Jan Pazdziora <jpx-opentx@adelton.com> - 2.2.1-1
- Rebase to 2.2.1 release.

* Sun Aug 20 2017 Jan Pazdziora <jpx-opentx@adelton.com> - 2.2.1-*
- Rebase to 2.2 master.

* Sat Aug 19 2017 Jan Pazdziora <jpx-opentx@adelton.com> - 2.2.0-1
- Rebase to 2.2.0.

* Sat Jul 15 2017 Jan Pazdziora <jpx-opentx@adelton.com> - 2.1.9-4
- Drive the build and installation by cmake and macros more.

* Fri Jul 14 2017 Jan Pazdziora <jpx-opentx@adelton.com> - 2.1.9-2
- Rebase to 2.1.9.

* Fri Jun 27 2014 Jan Pazdziora <jpx-opentx@adelton.com> - 2.0.5-1
- Use 2.0.5.

* Fri Jun 13 2014 Jan Pazdziora <jpx-opentx@adelton.com> - 2.0.2-0.1
- Use 2.0.2.

* Fri Jun 06 2014 Jan Pazdziora <jpx-opentx@adelton.com> - 2.0.1-0.1
- Use 2.0.1.

* Sun Jun 01 2014 Jan Pazdziora <jpx-opentx@adelton.com> - 1.99.7-0.1
- Initial attempt to build on Fedora 20.

