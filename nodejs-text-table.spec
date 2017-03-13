%{?scl:%scl_package nodejs-text-table}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-text-table_0.2.0

%global npmname text-table
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-text-table
Version:        0.2.0
Release:        3%{?dist}
Summary:        Borderless text tables with alignment
Url:            https://github.com/substack/text-table
Source0:        http://registry.npmjs.org/text-table/-/text-table-%{version}.tgz
License:        MIT

BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

# cyclic? BuildRequires: %{?scl_prefix}npm(cli-color@0.2.3)
# cyclic? BuildRequires: %{?scl_prefix}npm(tap@0.4.0)
# cyclic? BuildRequires: %{?scl_prefix}npm(tape@1.0.2)

%description
Borderless text tables with alignment

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/text-table
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/text-table
%nodejs_symlink_deps

%files
%{nodejs_sitelib}/text-table
%doc LICENSE readme.markdown

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.2.0-3
- Rebuilt with new metapackage
- add missing BuildArch and ExclusiveArch

* Wed Feb 12 2014 Tomas Hrcka <thrcka@redhat.com>
- Initial package build

