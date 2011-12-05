%define debug_package %{nil}

Name:           sblim-cmpi-devel
Version:        2.0.1
Release:        5%{?dist}
Summary:        SBLIM CMPI Provider Development Support

Group:          Development/Libraries
License:        EPL
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         sblim-cmpi-devel-2.0.0-cmpidata_constructor_4_cmpistring.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This packages provides the C and C++ CMPI header files needed by
provider developers and can be used standalone. If used for
C++ provider development it is also necessary to have
tog-pegasus-devel installed.

%package -n libcmpiCppImpl0
License:        EPL
Summary:        CMPI C++ wrapper library
Group:          Development/Libraries
Conflicts:      tog-pegasus

%description -n libcmpiCppImpl0
This packages provides the C++ wrapper library for CMPI development

%prep
%setup -q
%patch0 -p1 -b cmpidata_constructor_4_cmpistring

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# remove *.a and *.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/libcmpiCppImpl.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/libcmpiCppImpl.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libcmpiCppImpl0 -p /sbin/ldconfig

%postun -n libcmpiCppImpl0 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}
%{_includedir}/cmpi

%files -n libcmpiCppImpl0
%defattr(-,root,root,-)
%{_libdir}/libcmpiCppImpl.so*

%changelog
* Thu Jul 22 2010 Ondrej Vasik <ovasik@redhat.com> - 2.0.1-5
- based on further discussion the old approach with
  conflicts will be used, reverting previous two changes(#604578)

* Wed Jul 21 2010 Ondrej Vasik <ovasik@redhat.com> - 2.0.1-4
- ship ld.so.conf.d file(#604578)

* Tue Jul 20 2010 Ondrej Vasik <ovasik@redhat.com> - 2.0.1-3
- ship libcmpiCppImpl .so files in sblim subdir to prevent
  file conflict(#604578, #608846)

* Tue May 18 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.1-2
- Ship libcmpiCppImpl library in libcmpiCppImpl0 package

* Mon Mar 15 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.1-1
- Update to sblim-cmpi-devel-2.0.1

* Wed Nov  4 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.0-2
- Fix conversion between CMPIData and String

* Thu Aug 27 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov  4 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.5-2
- Fix License
- Spec file cleanup, rpmlint check

* Fri Oct 24 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.5-1
- Update to 1.0.5
  Resolves: #468326

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.4-6
- Autorebuild for GCC 4.3

* Mon Dec 18 2006 Mark Hamzy <hamzy@us.ibm.com> - 1.0.4-5
- Removed -debuginfo package.
- Removed ldconfig from post/postun

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> - 1.0.4-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Feb 09 2006 Viktor Mihajlovski <mihajlov@de.ibm.com> - 1.0.4-1
- Initial RH/Fedora version
