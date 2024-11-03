#
# $Revision$
#

Summary:     Local cache actions for libdnf5
Name:        dnf-local-cache-actions
Version:     0.1
Release:     1%{?dist}
License:     GPLv2
Group:       System Environment/Base
BuildArch:   noarch
Source0:     dnf-local-cache-actions
Source1:     local.actions
Source2:     README.md
Source3:     LICENSE.txt
URL:         http://worldwidesullivan.com
Vendor:      John Sullivan
Packager:    jsullivan3@gmail.com
BuildRequires: /usr/bin/install
BuildRequires: /usr/bin/shellcheck
Requires:    dnf5

%description
Automatically copy all downloaded packages to a repository on the
local filesystem and generating repo metadata.

%prep
cp -v %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build

%install
install -d ${RPM_BUILD_ROOT}/%{_sysconfdir}/dnf/libdnf5-plugins/actions.d
install -m 0644 local.actions ${RPM_BUILD_ROOT}/%{_sysconfdir}/dnf/libdnf5-plugins/actions.d
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
%{_sysconfdir}/dnf/libdnf5-plugins/actions.d/local.actions
%{_sbindir}/dnf-local-cache-actions

%changelog
* Sun Nov 3 2024 John Sullivan <jsullivan3@gmail.com> [0.1-1]
- Initial version