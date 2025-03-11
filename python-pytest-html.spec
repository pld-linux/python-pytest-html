#
# Conditional build:
%bcond_with	tests	# unit tests (failing)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pytest plugin for generating HTML reports
Summary(pl.UTF-8):	Wtyczka pytesta do generowania raportów HTML
Name:		python-pytest-html
# keep 1.x here for python2 support
Version:	1.22.1
Release:	3
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-html/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-html/pytest-html-%{version}.tar.gz
# Source0-md5:	16dbaffa45c78a3d28cfa424b9ab069a
URL:		https://pypi.org/project/pytest-html/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-pytest >= 3.0
BuildRequires:	python-pytest-metadata
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-pytest >= 3.0
BuildRequires:	python3-pytest-metadata
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest-html is a plugin for pytest that generates a HTML report for
the test results.

%description -l pl.UTF-8
pytest-html to wtyczka pytesta generująca raport HTML do wyników
testów.

%package -n python3-pytest-html
Summary:	pytest plugin for generating HTML reports
Summary(pl.UTF-8):	Wtyczka pytesta do generowania raportów HTML
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-pytest-html
pytest-html is a plugin for pytest that generates a HTML report for
the test results.

%description -n python3-pytest-html -l pl.UTF-8
pytest-html to wtyczka pytesta generująca raport HTML do wyników
testów.

%prep
%setup -q -n pytest-html-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_html.plugin,pytest_metadata.plugin,pytest_mock.plugin,pytest_rerunfailures \
PYTHONPATH=$(pwd) \
%{__python} -m pytest -v -r a testing
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_html.plugin,pytest_metadata.plugin,pytest_mock.plugin,pytest_rerunfailures \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest -v -r a testing
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/pytest_html
%{py_sitescriptdir}/pytest_html-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-html
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_html
%{py3_sitescriptdir}/pytest_html-%{version}-py*.egg-info
%endif
