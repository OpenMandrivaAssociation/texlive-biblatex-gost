%global tl_name biblatex-gost
%global tl_revision 66935

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.24
Release:	%{tl_revision}.1
Summary:	BibLaTeX support for GOST standard bibliographies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-gost
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-gost.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-gost.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides BibLaTeX support for Russian bibliography style
GOST 7.0.5-2008

