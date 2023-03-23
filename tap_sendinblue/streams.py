"""Stream type classes for tap-sendinblue."""

from pathlib import Path
from typing import Optional


from tap_sendinblue.client import SendinblueStream
from tap_sendinblue import schemas

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ListsStream(SendinblueStream):
    """Define custom stream."""
    name = "lists"
    path = "/contacts/lists"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.lists[*]"
    schema = schemas.lists

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "list_id": record["id"],
        }


class CampaignsStream(SendinblueStream):
    """Define custom stream."""
    name = "campaigns"
    path = "/emailCampaigns"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "campaigns.[*]"
    schema = schemas.campaigns


class ListMembersStream(SendinblueStream):
    """Define custom stream."""
    name = "listmembers"
    path = "/contacts/lists/{list_id}/contacts"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.contacts[*]"
    parent_stream_type = ListsStream

    schema = schemas.list_members


class SmtpAggregatedReportStream(SendinblueStream):
    name = "smtp_report"
    path = "/smtp/statistics/aggregatedReport"
    primary_keys = ["id"]
    replication_key = None
    schema = schemas.smtp_report


class SmtpEventsStream(SendinblueStream):
    name = "smtp_events"
    path = "/smtp/statistics/events"
    replication_key = None
    primary_keys = ["messageId"]
    records_jsonpath = "events.[*]"
    schema = schemas.smtp_events
