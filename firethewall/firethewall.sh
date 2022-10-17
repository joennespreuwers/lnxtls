#!/bin/bash

# Fire The Wall
# -------------
# This small script BURNS down firewalld cuz its useless <3

sudo systemctl stop firewalld

sudo systemctl disable firewalld

sudo systemctl mask --now firewalld

clear

echo "Burned down Firewalld!"
