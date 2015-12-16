%{?scl:%scl_package nodejs-text-table}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-text-table_0.2.0

%global npmname text-table
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-text-table
Version:        0.2.0
Release:        1.sc1%{?dist}
Summary:        borderless text tables with alignment
Url:            https://github.com/substack/text-table
Source0:        http://registry.npmjs.org/text-table/-/text-table-0.2.0.tgz
License:        MIT

BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

# cyclic? BuildRequires: %{?scl_prefix}npm(cli-color@0.2.3)
# cyclic? BuildRequires: %{?scl_prefix}npm(tap@0.4.0)
# cyclic? BuildRequires: %{?scl_prefix}npm(tape@1.0.2)

%description
borderless text tables with alignment

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/text-table
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/text-table
%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/text-table

%doc LICENSE readme.markdown

%changelog
* Wed Feb 12 2014 Tomas Hrcka <thrcka@redhat.com>
- Initial package build

