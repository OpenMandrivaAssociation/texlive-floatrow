Name:		texlive-floatrow
Version:	15878
Release:	1
Summary:	Modifying the layout of floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/floatrow
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/floatrow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/floatrow.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/floatrow.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The floatrow package provides many ways to customize layouts of
floating environments and has code to cooperate with the
caption 3.x package. The package offers mechanisms to put
floats side by side, and to put the caption beside its float.
The floatrow settings could be expanded to the floats created
by packages rotating, wrapfig, subfig (in the case of rows of
subfloats), and longtable.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/floatrow/floatpagestyle.sty
%{_texmfdistdir}/tex/latex/floatrow/floatrow.sty
%{_texmfdistdir}/tex/latex/floatrow/fr-fancy.sty
%{_texmfdistdir}/tex/latex/floatrow/fr-longtable.sty
%{_texmfdistdir}/tex/latex/floatrow/fr-subfig.sty
%{_texmfdistdir}/tex/latex/floatrow/listpen.sty
%doc %{_texmfdistdir}/doc/latex/floatrow/README
%doc %{_texmfdistdir}/doc/latex/floatrow/floatrow-rus.pdf
%doc %{_texmfdistdir}/doc/latex/floatrow/floatrow-rus.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/floatrow.pdf
%doc %{_texmfdistdir}/doc/latex/floatrow/fr-sample.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/frsample01.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/frsample02.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/frsample03.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/frsample04.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/frsample05.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/frsample06.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/frsample07.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/frsample10.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/frsample11.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/frsample12.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/pictures.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/sample-longtable-rus.tex
%doc %{_texmfdistdir}/doc/latex/floatrow/sample-longtable.tex
#- source
%doc %{_texmfdistdir}/source/latex/floatrow/floatrow.dtx
%doc %{_texmfdistdir}/source/latex/floatrow/floatrow.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
