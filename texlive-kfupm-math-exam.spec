Name:		texlive-kfupm-math-exam
Version:	63977
Release:	2
Summary:	A LaTeX document style to produce homework, quiz and exam papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kfupm-math-exam
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kfupm-math-exam.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kfupm-math-exam.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kfupm-math-exam.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands and environments that simplify
and streamline the process of preparing homework, quiz and exam
papers according to apreffered style. The default style is
based on the guidelines set by the department of mathematics at
King Fahd University of Petroleum and Minerals (KFUPM). It can
be easily customized to fit any style for any institution.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/kfupm-math-exam
%{_texmfdistdir}/tex/latex/kfupm-math-exam
%doc %{_texmfdistdir}/doc/latex/kfupm-math-exam

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
