%global goipath github.com/cpu/goacmedns
Version:        0.0.1
%global tag     %{version}
%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        A Go library to handle acme-dns client communication
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}


%description
%{summary}.


%package devel
Summary:        %{summary}
BuildArch:      noarch


%description devel
%{summary}.

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup


%build
%gobuildroot
%gobuild -o _bin/goacmedns-register %{goipath}/cmd/goacmedns-register


%install
%goinstall -t cmd
install -D -p -m 0755 _bin/goacmedns-register %{buildroot}%{_bindir}/goacmedns-register


%check
%gochecks


%files
%license LICENSE
%{_bindir}/goacmedns-register


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Nov 16 2018 Carl George <carl@george.computer> - 0.0.1-1
- Initial package
