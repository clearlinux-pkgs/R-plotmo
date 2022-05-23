#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-plotmo
Version  : 3.6.2
Release  : 55
URL      : https://cran.r-project.org/src/contrib/plotmo_3.6.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plotmo_3.6.2.tar.gz
Summary  : Plot a Model's Residuals, Response, and Partial Dependence Plots
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Formula
Requires: R-TeachingDemos
Requires: R-plotrix
BuildRequires : R-Formula
BuildRequires : R-TeachingDemos
BuildRequires : R-plotrix
BuildRequires : buildreq-R

%description
using partial dependence plots and other techniques.
        Also plot model residuals and other information on the model.

%prep
%setup -q -c -n plotmo
cd %{_builddir}/plotmo

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653343065

%install
export SOURCE_DATE_EPOCH=1653343065
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plotmo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plotmo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plotmo
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc plotmo || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/plotmo/DESCRIPTION
/usr/lib64/R/library/plotmo/INDEX
/usr/lib64/R/library/plotmo/Meta/Rd.rds
/usr/lib64/R/library/plotmo/Meta/features.rds
/usr/lib64/R/library/plotmo/Meta/hsearch.rds
/usr/lib64/R/library/plotmo/Meta/links.rds
/usr/lib64/R/library/plotmo/Meta/nsInfo.rds
/usr/lib64/R/library/plotmo/Meta/package.rds
/usr/lib64/R/library/plotmo/NAMESPACE
/usr/lib64/R/library/plotmo/NEWS
/usr/lib64/R/library/plotmo/R/plotmo
/usr/lib64/R/library/plotmo/R/plotmo.rdb
/usr/lib64/R/library/plotmo/R/plotmo.rdx
/usr/lib64/R/library/plotmo/README-figures/plotmo-randomForest.png
/usr/lib64/R/library/plotmo/README-figures/plotres-glmnet-gbm.png
/usr/lib64/R/library/plotmo/README-figures/plotres-randomForest.png
/usr/lib64/R/library/plotmo/doc/index.html
/usr/lib64/R/library/plotmo/doc/modguide.pdf
/usr/lib64/R/library/plotmo/doc/plotmo-notes.pdf
/usr/lib64/R/library/plotmo/doc/plotres-notes.pdf
/usr/lib64/R/library/plotmo/help/AnIndex
/usr/lib64/R/library/plotmo/help/aliases.rds
/usr/lib64/R/library/plotmo/help/paths.rds
/usr/lib64/R/library/plotmo/help/plotmo.rdb
/usr/lib64/R/library/plotmo/help/plotmo.rdx
/usr/lib64/R/library/plotmo/html/00Index.html
/usr/lib64/R/library/plotmo/html/R.css
/usr/lib64/R/library/plotmo/tests/test.plotmo.R
/usr/lib64/R/library/plotmo/tests/test.plotmo.Rout.save
