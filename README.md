# Nextbac

A program to backup your pictures from your nextcloud
synced folder to a local folder of your choice.

## Installation
Clone the repository with:

git clone https://github.com/jutep/nextbac.git

Install by running below command in the cloned repository

[sudo] pip install .

## Usage
It is usable by just running next-bac from your command line or
dmenu etc.

## Future Plans
In the future it will also have the abbility to pipe in 
Image names and remove pictures. It should be good with sxiv, in 
which you can select pictures and print them to standard output, which
can be piped to nextbac --remove in the future.
Depending on the flag, pictures will be removed,
only from local, from the nextcloud synced folder or both.
Also little statistic stuff will be possible like showing how
many pictures are stored or also the ratio between stored and
deleted pictures.
