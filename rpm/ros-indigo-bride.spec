%undefine _missing_build_ids_terminate_build
%undefine _python_bytecompile_errors_terminate_build

Name:           ros-indigo-bride
Version:        0.3.3
Release:        1%{?dist}
Summary:        ROS bride package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/bride
Source0:        %{name}-%{version}.tar.gz

Requires:       java-1.8.0-openjdk
Requires:       ros-indigo-bride-compilers
Requires:       ros-indigo-bride-templates
Requires:       ros-indigo-bride-tutorials
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  glibc-devel(x86-32)
BuildRequires:  glibc-static
BuildRequires:  glibc-static(x86-32)
BuildRequires:  java-1.8.0-openjdk
BuildRequires:  libcurl-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libstdc++-devel(x86-32)
BuildRequires:  libstdc++-static
BuildRequires:  libstdc++-static(x86-32)
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rospack

%description
installer.py installs a full eclipse installation in this package. Additionally
CDT and the BRIDE plugins will be installed. After rosmake you have the full
model driven engineering tool chain accessible inside this package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Alexander Bubeck <aub@ipa.fraunhofer.de> - 0.3.3-1
- Autogenerated by Bloom

