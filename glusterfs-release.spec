Name:		gluster-release
Version:	3.5
Release:	1%{?dist}
BuildArch:	noarch
Summary:	Repository file for the download.gluster.org yum repo

Group:		System Environment/Base
License:	GPLv2
URL:		http://download.gluster.org/pub/gluster/glusterfs/

%description
Repository files for the download.gluster.org releases.


%prep


%build
cat << EOF > glusterfs.repo
[glusterfs-3.5]
name=GlusterFS is a clustered file-system capable of scaling to several petabytes.
baseurl=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/epel-$releasever/$basearch/
enabled=1
skip_if_unavailable=1
gpgcheck=1
gpgkey=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/pub.key
priority=50

[glusterfs-noarch-3.5]
name=GlusterFS is a clustered file-system capable of scaling to several petabytes.
baseurl=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/epel-$releasever/noarch
enabled=1
skip_if_unavailable=1
gpgcheck=1
gpgkey=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/pub.key
priority=50

[glusterfs-source-3.5]
name=GlusterFS is a clustered file-system capable of scaling to several petabytes. - Source
baseurl=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/epel-$releasever/SRPMS
enabled=0
skip_if_unavailable=1
gpgcheck=1
gpgkey=http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/pub.key
priority=50
EOF

%install
mkdir -p %{buildroot}/etc/yum.repos.d
install -p -m 0644 glusterfs.repo %{buildroot}%{_sysconfdir}/yum.repos.d/


%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%postin
echo "Please review your system and install the yum-plugin-priorities RPM"
echo "as necessary."
echo "For more information please see http://www.gluster.org/pathto.html"

%changelog

* Wed Oct 15 2014 Kaleb S. KEITHLEY <kkeithle [at] redhat.com> 1.0-1
- Initial packaging.

