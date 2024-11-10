#
# $Revision$
#

Summary:     Local cache actions for libdnf5
Name:        dnf-local-cache-actions
Version:     0.2
Release:     2%{?dist}
License:     GPLv2
Group:       System Environment/Base
BuildArch:   noarch
Source0:     dnf-local-cache-actions
Source1:     local.actions
Source2:     local.conf
Source3:     local.repo
Source4:     README.md
Source5:     LICENSE.txt
URL:         https://github.com/jsullivan3/dnf-local-cache-actions
Vendor:      John Sullivan
Packager:    jsullivan3@gmail.com
BuildRequires: /usr/bin/install
BuildRequires: /usr/bin/shellcheck
Requires:    dnf5
Requires:    createrepo_c
Requires:    libdnf5-plugin-actions
# util-linux-core provides logger
Requires:    util-linux-core
Obsoletes:   python3-dnf-plugin-local = 4.9.0-1

%description
Automatically copy all downloaded packages to a repository on the
local filesystem and generating repo metadata.

%prep
cp -v %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .

%build

%install
install -d ${RPM_BUILD_ROOT}/%{_sysconfdir}/dnf/libdnf5-plugins/actions.d
install -m 0644 local.actions ${RPM_BUILD_ROOT}/%{_sysconfdir}/dnf/libdnf5-plugins/actions.d
install -d ${RPM_BUILD_ROOT}/%{_sysconfdir}/dnf/plugins
install -m 0644 local.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/dnf/plugins
install -d ${RPM_BUILD_ROOT}/%{_sysconfdir}/yum.repos.d
install -m 0644 local.repo ${RPM_BUILD_ROOT}/%{_sysconfdir}/yum.repos.d
install -d ${RPM_BUILD_ROOT}/%{_sbindir}/
install -m 0755 dnf-local-cache-actions ${RPM_BUILD_ROOT}/%{_sbindir}/

%check
shellcheck ${RPM_BUILD_ROOT}/%{_sbindir}/dnf-local-cache-actions

%post
# Insert configuration migration from python3-dnf-plugin-local here.

%preun

%postun

%files
%doc README.md
%license LICENSE.txt
%config(noreplace) %{_sysconfdir}/dnf/plugins/local.conf
%{_sysconfdir}/dnf/libdnf5-plugins/actions.d/local.actions
%attr(0644, -, -) %{_sysconfdir}/yum.repos.d/local.repo
%{_sbindir}/dnf-local-cache-actions

%changelog
* Sat Nov 9 2024 John Sullivan <jsullivan3@gmail.com> [0.2-2]
- Obsolete the python3-dnf-plugin-local package to avoid conflicts with the config file
- Use logger to log to system log and/or journal instead of directly to log file
- Correctly handle repository metadata update without architecture-specific directories
- Correctly handle i686 repository in x86_64 environments
- Update project URL to point to GitHub repository
- Fix repository configuration not readable by non-root user

* Sun Nov 3 2024 John Sullivan <jsullivan3@gmail.com> [0.1-1]
- Initial version
