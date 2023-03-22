from singer_sdk import typing as th

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
