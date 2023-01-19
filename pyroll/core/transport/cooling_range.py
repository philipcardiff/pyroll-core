import logging
from typing import List, cast

from .transport import Transport


class CoolingRange(Transport):
    """Represents a cooling range."""

    def __init__(
            self,
            label: str = "",
            **kwargs
    ):
        """
        :param label: label for human identification
        :param kwargs: additional hook values as keyword arguments to set explicitly
        """

        super().__init__(label)
        self.__dict__.update(kwargs)
        self._log = logging.getLogger(__name__)

    @property
    def disk_elements(self) -> List['CoolingRange.DiskElement']:
        """A list of disk elements used to subdivide this unit."""
        return list(self._subunits)

    class Profile(Transport.Profile):
        """Represents a profile in context of a transport unit."""

        @property
        def cooling_range(self) -> 'CoolingRange':
            return cast(CoolingRange, self.unit)

    class InProfile(Profile, Transport.InProfile):
        """Represents an incoming profile of a transport unit."""

    class OutProfile(Profile, Transport.OutProfile):
        """Represents an outgoing profile of a transport unit."""

    class DiskElement(Transport.DiskElement):
        """Represents a disk element in a roll pass."""

        @property
        def cooling_range(self) -> 'CoolingRange':
            return cast(CoolingRange, self.parent)

        class Profile(Transport.DiskElement.Profile):
            """Represents a profile in context of a disk element unit."""

        class InProfile(Profile, Transport.DiskElement.InProfile):
            """Represents an incoming profile of a disk element unit."""

        class OutProfile(Profile, Transport.DiskElement.OutProfile):
            """Represents an outgoing profile of a disk element unit."""
