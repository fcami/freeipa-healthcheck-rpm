# remaining issues
# * man page for ipa-healthcheck

%global project freeipa
%global shortname healthcheck
%global longname ipa%{shortname}
%global debug_package %{nil}
%global python3dir %{_builddir}/python3-%{name}-%{version}-%{release}
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}


# git ls-remote https://github.com/freeipa/freeipa-healthcheck.git
%global commit f0c33bd26e3aaaadd60bc130ab89f5fb09a9464a
%global gittag 0.1
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Name:           %{project}-%{shortname}
Version:        %{gittag}
Release:        1%{?dist}
Summary:        Health check tool for FreeIPA
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/%{project}/%{project}-%{shortname}
Source0:        https://github.com/%{project}/%{project}-%{shortname}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        %{longname}.conf
Patch0:         0001-add-ipahealthcheck.ipa-package.patch


BuildRequires:  python3-devel


%{?python_enable_dependency_generator}


%description
The FreeIPA health check tool provides a set of checks to proactively detect
defects in a FreeIPA cluster.


%prep
%autosetup -p1 -n %{project}-healthcheck-%{commit}


%build
%py3_build


%install
%py3_install
mkdir -p %{buildroot}%{_sysconfdir}/%{longname}
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{longname}


%check
%{__python3} setup.py test


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md
%{_bindir}/ipa-%{shortname}
%dir %{_sysconfdir}/%{longname}
%config(noreplace) %{_sysconfdir}/%{longname}/%{longname}.conf
%{python3_sitelib}/%{longname}/
%{python3_sitelib}/%{longname}-%{version}-*.egg-info/
%{python3_sitelib}/%{longname}-%{version}-*-nspkg.pth


%changelog
* Tue Apr 2 2019 François Cami <fcami@redhat.com> - 0.1-1
- Initial package import
