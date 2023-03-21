"""Sendinblue tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers


from tap_sendinblue.streams import (
    SendinblueStream,
    ListsStream,
    CampaignsStream,
    CampaignsReportStream,
    ListMembersStream,
)


STREAM_TYPES = [ListsStream, CampaignsStream, CampaignsReportStream, ListMembersStream]


class TapSendinblue(Tap):
    """Sendinblue tap class."""

    name = "tap-sendinblue"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
