from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("totalBlacklisted", th.IntegerType),
    th.Property("totalSubscribers", th.IntegerType),
    th.Property("uniqueSubscribers", th.IntegerType),
    th.Property("folderId", th.IntegerType),
).to_dict()
