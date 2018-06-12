import os
#Installing the VirtualBox
os.system("brew cask install virtualbox")

#Installing the Vagrant Dependencies
os.system ("brew cask install vagrant")


os.system("sudo install vagrant")

#creating a CentOS Virtual Machine using Vagrant Boxes
os.system("vagrant init centos/7")

#Turning up the vagrant
os.system("vagrant up")

#Accessing the Virtual Machine
os.system("vagrant ssh")