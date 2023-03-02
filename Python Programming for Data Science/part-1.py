print("hello world")

print("hello AI Era")
################################
    #NUMBERS AND STRINGS
################################

print(9+10)
type(9.2)
type(3)
type("hello")

################################
     #Assigments & Variables
################################

a=9
a
b="hello ai era"

c=13

a*c

d=a-c
d

###########################################################
     #Virtual Environment and Package  Managment
###########################################################

#for the listing of virtual environments
#conda env list

#if we want to create a virtual environment with a name of our own
#conda create -n myenv (bu isimlendirme degişebilir)


#to activate the virtual environment
#conda activate myenv

#listing of installed packages
#conda list

#package loading
#conda install numpy

#loading multiple packages at the same time
#conda install numpy scipy pandas

#packet deletion process
#conda remove package_name

#loading a package according to a specific data
#conda install numpy=1.20.1

#pip==
#conda=

#uprading package
#conda upgrade numpy

#upgrading all packages
#conda upgrade -all

#pip:pypi(python package index)paket yönetim aracı

#package install
#pip insatall package_name

#according to the installation version of all packages
#pip install pandas==(version name)

#if we want to send what the packages are
#conda env export > environment.yaml

# if we want to close our own environment
#conda deactivate

#if we want to delete our own environment
#conda env remove -n myenv

#if we want to install the package that comes to us from scrath
#conda env create -f environment.yaml

#if we want to create the file that comes to us
#conda env create -f environment.yaml

