####################################################################################################
# 
# PyElectronic - Python Electronic Tools.
# Copyright (C) 2012 Salvaire Fabrice
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
# 
####################################################################################################

####################################################################################################

import os

####################################################################################################


# Utility function to read the README file.
# Used for the long_description.
def read(file_name):

    path = os.path.dirname(os.path.realpath(__file__))
    if os.path.basename(path) == 'tools':
        path = os.path.dirname(path)
    elif 'build/bdist' in path:
        path = path[:path.find('build/bdist')]
    absolut_file_name = os.path.join(path, file_name)

    return open(absolut_file_name).read()

####################################################################################################

setup_dict = dict(
    name='pyelectronic',
    version='0.1.0',
    author='Fabrice Salvaire',
    author_email='fabrice.salvaire@orange.fr',
    description='Python Tools for Electronic',
    license = "GPLv3",
    keywords = "electronic tools",
    url='http://fabrice-salvaire.pagesperso-orange.fr/software/index.html',
    scripts=['bin/resistor-decoder'],
    packages=['PyElectronic'],
    data_files = [('share/PyElectronic/icons',['share/icons/resistor.svg']),
                  ('share/applications', ['spec/resistor-decoder.desktop']),
                  ],
    long_description=read('README.pypi'),
    # cf. http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Education",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        ],
    install_requires=[
        'pyqt>=4.9',
        ],
    )

####################################################################################################
#
# End
#
####################################################################################################
