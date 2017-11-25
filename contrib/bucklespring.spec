Name:           bucklespring
Version:        1.4.0
Release:        1%{?dist}
Summary:        Nostalgia bucklespring keyboard sound


Group:          Applications/Multimedia
License:        GPLv2
URL:            https://github.com/zevv/bucklespring
Source0:        https://github.com/zevv/bucklespring/archive/v1.4.0.zip
#Source0:       bucklespring-1.4.0.zip

# BuildRequires:        pkg-config pkgconf-pkg-config
BuildRequires:  gcc alure-devel libXtst-devel openal-soft-devel
Requires:       alure openal-soft libXtst

%description
This project emulates the sound of my old faithful IBM Model-M
space saver bucklespring keyboard while typing on my notebook,
mainly for the purpose of annoying the hell out of my coworkers.

%prep
%setup -q

%build

cat >>Makefile <<EOF

install:
	mkdir -p "${RPM_BUILD_ROOT}/usr/local/bin"
	install buckle "${RPM_BUILD_ROOT}/usr/local/bin/buckle"
	install --directory wav "${RPM_BUILD_ROOT}/usr/local/lib/bucklespring/wav"
	cp -a wav/* "${RPM_BUILD_ROOT}/usr/local/lib/bucklespring/wav/"

EOF

tail Makefile

make


%install
make install


%files
%doc
/usr/local/bin/buckle
/usr/local/lib/bucklespring/wav/



%changelog
