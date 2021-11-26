Name:       pth
Summary:    The GNU Portable Threads library
Version:    2.0.7
Release:    2
License:    LGPLv2+
URL:        http://www.gnu.org/software/pth/
Source0:    ftp://ftp.gnu.org/gnu/pth/pth-%{version}.tar.gz
Source1:    ftp://ftp.gnu.org/gnu/pth/pth-%{version}.tar.gz.sig
Patch0:     pth-2.0.7-dont-remove-gcc-g.patch
Patch1:     pth-2.0.7-fixbuildlinux.patch
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.



%package devel
Summary:    Development headers and libraries for GNU Pth
Requires:   %{name} = %{version}-%{release}

%description devel
Development headers and libraries for GNU Pth.


%prep
%autosetup -p1 -n %{name}-%{version}

%build
%configure --disable-static ac_cv_func_sigstack='no'

# this is necessary; without it make -j fails
make pth_p.h
make %{?_smp_mflags}



%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%doc HACKING
%doc ANNOUNCE AUTHORS ChangeLog HISTORY NEWS PORTING README
%doc SUPPORT TESTS THANKS USERS
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/*/*
%{_datadir}/aclocal/*

