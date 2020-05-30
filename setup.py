from setuptools import setup, find_packages

setup(name='nextbac',
      version='0.1',
      description='Programm to back pictures from Nextcloud',
      packages=find_packages(),
      entry_points={
          'console_scripts': ['next-bac=nextbac.command_line:main']
      }
      )
