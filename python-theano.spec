%define tarname Theano
%define name	python-theano
%define version	0.4.1
%define release %mkrel 1

Summary:	Optimizing compiler for mathematical expressions in Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://deeplearning.net/software/theano/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-numpy >= 1.3.0, python-scipy >= 0.7.0
Requires:	blas-devel, python-devel, gcc-c++
Suggests:	python-nose, nvidia-cuda-toolkit
BuildRequires:	python-devel

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

%prep
%setup -q -n %{tarname}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
find %{buildroot} -type f -exec chmod 644 {} \;
find doc/ -type f -exec chmod 644 {} \;
find doc/ -type d -exec chmod 755 {} \;
chmod 644 *.txt

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README.txt HISTORY.txt doc/* 
