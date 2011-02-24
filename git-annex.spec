Summary:	Manage files with git, without checking in their contents
Name:		git-annex
Version:	0.11
Release:	0.1
License:	GPL v3
Group:		Applications/Archiving
# Made from git
#   git clone git://git.kitenet.net/git-annex
#   cd git-annex
#   git archive --format=tar --prefix=git-annex-0.11/ 0.11 | bzip2 --best > ../git-annex-0.11.tar.bz2
URL:		http://git-annex.branchable.com/
Source0:	%{name}-%{version}.tar.bz2
Patch1:		prefix-support.patch
Patch0:		install-docs.patch
BuildRequires:	ikiwiki
# Build-time check for uuid
BuildRequires:	ghc-MissingH-devel
BuildRequires:	ghc-MissingH-prof
BuildRequires:	ghc-pcre-light-devel
BuildRequires:	ghc-pcre-light-prof
BuildRequires:	ghc-utf8-string-devel
BuildRequires:	ghc-utf8-string-prof
BuildRequires:	uuid
Requires:	findutils
Requires:	git-core
Requires:	rsync
Requires:	uuid
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
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install install-docs \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_docdir}/%{name}/
%{_mandir}/man1/%{name}.1*
