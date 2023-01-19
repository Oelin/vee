#!/usr/bin/env python3

"""
Vee

Usage: vee [owner]/[package]
"""


import os
import sys


def vee(owner, package):

        if package in os.listdir():
                return print(f'{package} is already installed.')

        print(f'[Vee]    installing {owner}/{package}...')

        if os.system(f'git clone https://github.com/{owner}/{package} --quiet'):
                return print(f'\n[Vee]    downloading {owner}/{package} cancelled ❌.')

        if 'vee.py' in os.listdir(package):
                return print(f'[Vee]    running vee.py...')

                try:
                        __import__('vee.py')

                except:
                        return print(f'\n[Vee]    an exception occured while running vee.py ❌.')

        print(f'[Vee]    successfully installed {package} 🥳.')


if __name__ == '__main__':
	
        try:
                owner, package = sys.argv[1].split('/')

        except:
                print(__doc__)
                exit(1)

        vee(owner, package)
