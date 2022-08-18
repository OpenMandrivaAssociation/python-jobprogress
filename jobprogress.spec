# Created by pyp2rpm-3.3.5
%global pypi_name jobprogress

Name:           python-%{pypi_name}
Version:        1.0.4
Release:        2
Summary:        Cross-toolkit UI progress tracking
Group:          Development/Python
License:        BSD License
URL:            http://hg.hardcoded.net/jobprogress/
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 jobprogress -- Cross-toolkit UI progress tracking When doing complex
processing that has to report progress indication to the user, things can get
complex quick. Often, we don't know beforehand how many work unit our
processing will have, because knowing it depends on another work unit for which
the progress should also be reported to the user. One example of such situation
is processing...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

