# Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def only_dir(path):
    listik = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]
    print(listik)


def only_files(path):
    listik = [dir for dir in os.listdir(path) if os.path.isfile(os.path.join(path, dir))]
    print(listik)


def doublegis(path):
    listik = [dir for dir in os.listdir(path)]
    print(listik)


path = "/pp2-labki" # nado dopolnit'
doublegis(path)
only_dir(path)
only_files(path)