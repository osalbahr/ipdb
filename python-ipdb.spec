Name:           python-ipdb
Version:        0.13.13
Release:        %autorelease
Summary:        IPython-enabled pdb

License:         BSD-3-Clause
URL:            https://github.com/gotcha/ipdb
Source:         %{pypi_source ipdb}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ipdb' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ipdb
Summary:        %{summary}

%description -n python3-ipdb %_description


%prep
%autosetup -p1 -n ipdb-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l ...


%check
%pyproject_check_import


%files -n python3-ipdb -f %{pyproject_files}


%changelog
%autochangelog