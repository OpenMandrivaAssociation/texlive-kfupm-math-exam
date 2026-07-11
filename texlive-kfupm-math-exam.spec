%global tl_name kfupm-math-exam
%global tl_revision 63977

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.0
Release:	%{tl_revision}.1
Summary:	A LaTeX document style to produce homework, quiz and exam papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kfupm-math-exam
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kfupm-math-exam.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kfupm-math-exam.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kfupm-math-exam.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands and environments that simplify and
streamline the process of preparing homework, quiz and exam papers
according to apreffered style. The default style is based on the
guidelines set by the department of mathematics at King Fahd University
of Petroleum and Minerals (KFUPM). It can be easily customized to fit
any style for any institution.

