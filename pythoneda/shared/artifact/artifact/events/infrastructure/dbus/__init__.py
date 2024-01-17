# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/artifact/events/infrastructure/dbus/__init__.py

This file ensures pythoneda.shared.artifact.artifact.events.infrastructure.dbus is a package.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/artifact-events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

DBUS_PATH = "/pythoneda/shared/artifact/artifact"

from .dbus_artifact_changes_committed import DbusArtifactChangesCommitted
from .dbus_artifact_commit_pushed import DbusArtifactCommitPushed
from .dbus_artifact_commit_tagged import DbusArtifactCommitTagged
from .dbus_artifact_tag_pushed import DbusArtifactTagPushed
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
