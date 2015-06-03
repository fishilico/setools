# Copyright 2015, Tresys Technology, LLC
#
# This file is part of SETools.
#
# SETools is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 2.1 of
# the License, or (at your option) any later version.
#
# SETools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with SETools.  If not, see
# <http://www.gnu.org/licenses/>.
#

from PyQt5.uic import loadUi


class SEToolsWidget(object):
    def load_ui(self, filename):
        # If we are in the git repo, look at the local
        # UI file, otherwise look at the installed file.
        for path in ["data/", "/usr/share/setools/"]:
            try:
                loadUi(path + filename, self)
                break
            except OSError:
                pass
        else:
            raise RuntimeError("Unable to load Qt UI file \"{0}\"".format(filename))
