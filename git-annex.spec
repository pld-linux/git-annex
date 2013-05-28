%define     _enable_debug_packages  0
Summary:	Manage files with git, without checking in their contents
Name:		git-annex-standalone
Version:	4.20130521.1
Release:	0.2
License:	GPL v3
Group:		Applications/Archiving
URL:		http://git-annex.branchable.com/
Source0:	http://downloads.kitenet.net/git-annex/linux/current/%{name}-amd64.tar.gz
# Source0-md5:	dfceaa0d56d13815ba15bb50a711d1bb
Source1:	http://downloads.kitenet.net/git-annex/linux/current/%{name}-i386.tar.gz
Source2:	git-annex-shell
# Source1-md5:	12bbe08f32b7d499849b600575959954
Conflicts:	git-annex
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git-annex allows managing files with git, without checking the file
contents into git. While that may seem paradoxical, it is useful when
dealing with files larger than git can currently easily handle,
whether due to limitations in memory, checksumming time, or disk
space.

Even without file content tracking, being able to manage files with
git, move files around and delete files with versioned directory
trees, and use branches and distributed clones, are all very handy
reasons to use git. And annexed files can co-exist in the same git
repository with regularly versioned files, which is convenient for
maintaining documents, Makefiles, etc that are associated with annexed
files but that benefit from full revision control.

When a file is annexed, its content is moved into a key-value store,
and a symlink is made that points to the content. These symlinks are
checked into git and versioned like regular files. You can move them
around, delete them, and so on. Pushing to another git repository will
make git-annex there aware of the annexed file, and it can be used to
retrieve its content from the key-value store.

%prep
%ifarch %{x8664}
%setup -qc
%endif
%ifarch %{ix86}
%setup -qc -T -a1
%endif

%build
mkdir -p opt/git-annex
mkdir -p usr/bin
mv git-annex.linux/* opt/git-annex

%{__sed} -i 's:^base=.*:base=/opt/git-annex:' opt/git-annex/git-annex
%{__sed} -i 's:^base=.*:base=/opt/git-annex:' opt/git-annex/git-annex-webapp
%{__sed} -i 's:^base=.*:base=/opt/git-annex:' opt/git-annex/runshell

cp opt/git-annex/git-annex usr/bin/
cp opt/git-annex/git-annex-webapp usr/bin/

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/opt/git-annex
install -d $RPM_BUILD_ROOT/usr/bin
cp -a opt/git-annex/* $RPM_BUILD_ROOT/opt/git-annex
cp -a usr/bin/* $RPM_BUILD_ROOT/usr/bin
install %{SOURCE2} $RPM_BUILD_ROOT/usr/bin/git-annex-shell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir /opt/git-annex
%dir /opt/git-annex/bin
%dir /opt/git-annex/git-core
%dir /opt/git-annex/git-core/mergetools
%dir /opt/git-annex/lib
%dir /opt/git-annex/glibc-libs
%dir /opt/git-annex/libdirs
%dir /opt/git-annex/usr
%dir /opt/git-annex/templates
%dir /opt/git-annex/usr/lib
%ifarch %{x8664}
%dir /opt/git-annex/usr/lib/x86_64-linux-gnu
%dir /opt/git-annex/lib/x86_64-linux-gnu
%attr(755,root,root) /opt/git-annex/usr/lib/x86_64-linux-gnu/*
%attr(755,root,root) /opt/git-annex/lib/x86_64-linux-gnu/*
%endif
%ifarch %{ix86}
%dir /opt/git-annex/usr/lib/i386-linux-gnu
%dir /opt/git-annex/lib/i386-linux-gnu
%attr(755,root,root) /opt/git-annex/usr/lib/i386-linux-gnu/*
%attr(755,root,root) /opt/git-annex/lib/i386-linux-gnu/*
%endif
%attr(755,root,root) /opt/git-annex/git-annex
%attr(755,root,root) /opt/git-annex/git-annex-webapp
%attr(755,root,root) /opt/git-annex/runshell
%attr(755,root,root) /opt/git-annex/bin/*
%attr(755,root,root) /opt/git-annex/git-core/git*
%attr(755,root,root) /opt/git-annex/git-core/mergetools/*
%attr(755,root,root) /opt/git-annex/usr/lib/*so*
%attr(755,root,root) /usr/bin/git-annex
%attr(755,root,root) /usr/bin/git-annex-webapp
%attr(755,root,root) /usr/bin/git-annex-shell
#%{_mandir}/man1/%{name}.1*
#%{_mandir}/man1/%{name}-shell.1*
