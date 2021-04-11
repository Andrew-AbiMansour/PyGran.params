"""
  Created on Oct 08, 2019
  Author: Andrew Abi-Mansour

  This is the::

  ██████╗ ██╗   ██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗
  ██╔══██╗╚██╗ ██╔╝██╔════╝ ██╔══██╗██╔══██╗████╗  ██║
  ██████╔╝ ╚████╔╝ ██║  ███╗██████╔╝███████║██╔██╗ ██║
  ██╔═══╝   ╚██╔╝  ██║   ██║██╔══██╗██╔══██║██║╚██╗██║
  ██║        ██║   ╚██████╔╝██║  ██║██║  ██║██║ ╚████║
  ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

  DEM simulation and analysis toolkit
  http://www.pygran.org, support@pygran.org
  Core developer and main author:
  Andrew Abi-Mansour, andrew.abi.mansour@pygran.org
  PyGran is open-source, distributed under the terms of the GNU Public
  License, version 2 or later. It is distributed in the hope that it will
  be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. You should have
  received a copy of the GNU General Public License along with PyGran.
  If not, see http://www.gnu.org/licenses . See also top-level README
  and LICENSE files.
"""

from setuptools import setup, find_packages
import versioneer
import os

setup(
    name="pygran_params",
    version=versioneer.get_version(),
    author="Andrew Abi-Mansour",
    author_email="support@pygran.org",
    description=("A PyGran package for powder/granular materials definition."),
    license="GNU v2",
    keywords="Discrete Element Method, Granular Materials",
    url="https://github.com/Andrew-AbiMansour/PyGranParams",
    packages=find_packages(),
    include_package_data=True,
    long_description="A PyGran package that serves as an extensible materials database. See http://www.pygran.org for more info on PyGran.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX :: Linux",
    ],
    zip_safe=True,
    cmdclass=versioneer.get_cmdclass(),
)
