Summary:	Manage files with git, without checking in their contents
Name:		git-annex
Version:	4.20130501.1
Release:	0.1
License:	GPL v3
Group:		Applications/Archiving
URL:		http://git-annex.branchable.com/
Source0:	http://hackage.haskell.org/packages/archive/git-annex/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	59026597f8ef9575998cbab0fafe8416
BuildRequires:	ghc >= 7.4
BuildRequires:	ghc-IfElse
BuildRequires:	ghc-extensible-exceptions
BuildRequires:	ghc-MissingH
BuildRequires:	ghc-QuickCheck
BuildRequires:	ghc-dataenc
BuildRequires:	ghc-monad-control
#BuildRequires:	ghc-pcre-light
BuildRequires:	ghc-utf8-string
BuildRequires:	libuuid
Requires:	findutils
Requires:	findutils
Requires:	git-core
Requires:	git-core
Requires:	libuuid
Requires:	rsync
Requires:	rsync
Suggests:	curl
Suggests:	gnu-gpg
Suggests:	lsof
Suggests:	nss-mdns
Suggests:	sha1sum
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
#%setup -qc
#mv %{name}-*/* .

%build
%{__make}
#%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-shell
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-shell.1*
