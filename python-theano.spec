%define module Theano
%define lmodule %(echo %{module} | tr [:upper:] [:lower:])

Summary:	Optimizing compiler for mathematical expressions in Python
Name:		python-%{lmodule}
Version:	1.0.5
Release:	1
Source0:	https://github.com/Theano/Theano/releases/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://deeplearning.net/software/theano/
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(scipy)
BuildRequires:	python3dist(setuptools)

#Requires:	blas-devel

BuildArch:	noarch

%description
Theano is a Python library that allows you to define, optimize, and
efficiently evaluate mathematical expressions involving
multi-dimensional arrays. Using Theano, for problems involving large
amounts of data, it is possible to attain speeds that are only a few
percentage points slower than hand-crafted C implementations.

Theano melds some aspects of a computer algebra system (CAS) with
aspects of an optimizing compiler. It can even transform some or all
of the mathematical expression into C code and compile it into native
machine instructions. This combination of CAS with optimizing
compilation is particularly useful for tasks in which complicated
mathematical expressions are evaluated repeatedly and evaluation speed
is critical.

Theano supports a range of numerical types in multiple dimensions and
a number of well-tested operations. It also allows you to compute the
gradient of an expression with respect to another. Symbolic
expressions may be compiled into functions, which work on the same
data structures as numpy, allowing for easy interoperability.

%files
%doc README.rst LICENSE.txt
%{_bindir}/%{lmodule}-cache
%{_bindir}/%{lmodule}-nose
%{python3_sitelib}/bin
%{python3_sitelib}/%{lmodule}
%{python3_sitelib}/%{module}-%{version}-py?.?.egg-info

#-----------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py3_build

%install
%py3_install

# Restore executable permission on the scripts
chmod a+x $(find %{buildroot} -name \*.py -o -name \*.sh | xargs grep -l '^#!')

# Do not ship the tests
rm -rf %{buildroot}%{python3_sitelib}/tests
