"""Sendinblue tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th

from tap_sendinblue.streams import (
    SendinblueStream,
    ListsStream,
    CampaignsStream,
    ListMembersStream,
    SmtpAggregatedReportStream,
    SmtpEventsStream,
)

STREAM_TYPES = [ListsStream, CampaignsStream, ListMembersStream,
                SmtpAggregatedReportStream, SmtpEventsStream]


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
