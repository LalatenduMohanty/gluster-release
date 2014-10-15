Name:		glusterfs-release
Version:	3.5
Release:	2.1%{?dist}
BuildArch:	noarch
Summary:	Repository file for the download.gluster.org yum repo

Group:		System Environment/Base
License:	GPLv2
URL:		http://download.gluster.org/pub/gluster/glusterfs/
Requires:	yum-plugin-priorities

%description
Repository files for the download.gluster.org releases.


%prep


%build
cat << EOF > glusterfs-%{version}.repo
[glusterfs-%{version}]
name=GlusterFS is a clustered file-system capable of scaling to several petabytes.
baseurl=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/epel-$releasever/$basearch/
enabled=1
skip_if_unavailable=1
gpgcheck=1
gpgkey=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/pub.key
priority=1

[glusterfs-noarch-%{version}]
name=GlusterFS is a clustered file-system capable of scaling to several petabytes.
baseurl=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/epel-$releasever/noarch
enabled=1
skip_if_unavailable=1
gpgcheck=1
gpgkey=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/pub.key
priority=1

[glusterfs-source-%{version}]
name=GlusterFS is a clustered file-system capable of scaling to several petabytes. - Source
baseurl=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/epel-$releasever/SRPMS
enabled=0
skip_if_unavailable=1
gpgcheck=1
gpgkey=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/pub.key
priority=1
EOF

%install
mkdir -p %{buildroot}/etc/yum.repos.d
install -p -m 0644 glusterfs-%{version}.repo %{buildroot}%{_sysconfdir}/yum.repos.d/


%files
%{_sysconfdir}/yum.repos.d/*

%changelog

* Wed Oct 15 2014 Kaleb S. KEITHLEY <kkeithle [at] redhat.com> 3.5-2.1
- Initial packaging.

