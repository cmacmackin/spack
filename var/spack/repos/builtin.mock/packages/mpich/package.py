##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Mpich(Package):
    homepage   = "http://www.mpich.org"
    url        = "http://www.mpich.org/static/downloads/3.0.4/mpich-3.0.4.tar.gz"
    list_url   = "http://www.mpich.org/static/downloads/"
    list_depth = 2

    variant('debug', default=False,
            description="Compile MPICH with debug flags.")

    version('3.0.4', '9c5d5d4fe1e17dd12153f40bc5b6dbc0')
    version('3.0.3', 'foobarbaz')
    version('3.0.2', 'foobarbaz')
    version('3.0.1', 'foobarbaz')
    version('3.0', 'foobarbaz')
    version('1.0', 'foobarbas')

    provides('mpi@:3', when='@3:')
    provides('mpi@:1', when='@:1')

    def install(self, spec, prefix):
        pass
