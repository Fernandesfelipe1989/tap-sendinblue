"""Stream type classes for tap-sendinblue."""

from pathlib import Path
from typing import Optional

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_sendinblue.client import SendinblueStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ListsStream(SendinblueStream):
    """Define custom stream."""
    name = "lists"
    path = "/contacts/lists"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.lists[*]"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("totalBlacklisted", th.IntegerType),
        th.Property("totalSubscribers", th.IntegerType),
        th.Property("uniqueSubscribers", th.IntegerType),
        th.Property("folderId", th.IntegerType),
    ).to_dict()

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
    records_jsonpath = "$.campaigns[*]"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        # th.Property("scheduledAt", th.DateTimeType),
        # th.Property("createdAt", th.DateTimeType),
        # th.Property("modifiedAt", th.DateTimeType),
        # th.Property("sentDate", th.DateTimeType),
        # th.Property("shareLink", th.StringType),
        # th.Property("subject", th.StringType),
        # th.Property("statistics",
        #             th.ObjectType(
        #                 th.Property("mirrorClick", th.IntegerType),
        #                 th.Property("remaining", th.IntegerType),
        #                 th.Property("campaignStats",
        #                             th.ArrayType(
        #                                 th.ObjectType(
        #                                     th.Property("listId", th.IntegerType),
        #                                     th.Property("uniqueClicks", th.IntegerType),
        #                                     th.Property("clickers", th.IntegerType),
        #                                     th.Property("complaints", th.IntegerType),
        #                                     th.Property("delivered", th.IntegerType),
        #                                     th.Property("sent", th.IntegerType),
        #                                     th.Property("softBounces", th.IntegerType),
        #                                     th.Property("hardBounces", th.IntegerType),
        #                                     th.Property("uniqueViews", th.IntegerType),
        #                                     th.Property("trackableViews", th.IntegerType),
        #                                     th.Property(
        #                                         "unsubscriptions", th.IntegerType
        #                                     ),
        #                                     th.Property("viewed", th.IntegerType),
        #                                     th.Property("deferred", th.IntegerType),
        #                                 ),
        #                             )
        #                             ),
        #             ),
        #             ),

    ).to_dict()


class ListMembersStream(SendinblueStream):
    """Define custom stream."""
    name = "listmembers"
    path = "/contacts/lists/{list_id}/contacts"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.contacts[*]"
    parent_stream_type = ListsStream

    schema = th.PropertiesList(
        th.Property("email", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("emailBlacklisted", th.BooleanType),
        th.Property("smsBlacklisted", th.BooleanType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("modifiedAt", th.DateTimeType),
        th.Property("attributes", th.ObjectType(
            th.Property("value", th.StringType), th.Property("label", th.StringType)
        ),
                    ),
    ).to_dict()
