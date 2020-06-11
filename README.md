# Nextbac

A program to backup your pictures from your nextcloud
synced folder to a local folder of your choice. Best to use
with sxiv.

## Installation
Clone the repository with:

git clone https://github.com/jutep/nextbac.git

Install by running below command in the cloned repository

[sudo] pip install .

## Usage
It is usable by just running next-bac from your command line or
dmenu etc.

If it's first time usage, run next-bac and it will ask you to
to enter the paths for your server- and backupfolder, and
creates  an config file. The config file will be stored in
.config/nextbac/

To remove Pictures you can pipe the picture names to
next-bac.

Example:

In the backup folder

sxiv -ftor 2020 | next-bac

So the pictures you mark in sxiv, or any other method you
would like to pipe, gets transformed inside nextbac and
removed. 

The only difference between backing up and deleting is, if 
sth is piped into nextbac or not.

## Features
Nextbac will store the pictures for you in an folder
hierarchy of year/month in your backup folder. It does not
determine when the picture was taken but the month you are
backing it up in. 


If you have nextbac running on multiple devices, everytime
you run it, it will first sync your Nextcloud server folder
with your backup folder. So when you delete Pictures on one
device, the next time you run nextbac, they will automatically
be removed from your local backup. 

## Problems

1. Only Pictures that are jpg can get stored right now :)
   quick fix next time
