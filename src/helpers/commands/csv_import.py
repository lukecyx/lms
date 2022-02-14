import inspect


def transform(csv_row: dict, typed_dict) -> dict:
    """Transform CSV field values into types specified on a TypedDict subclass.

    Skips fields that are not defined on the subclass.

    :param csv_row: Row from csv.DictReader
    :param typed_dict: A TypedDict subclass.
    :type  typed_dict: Subclass of typing.TypedDict.
    :return: Csv row with converted values.
    """

    if not inspect.isclass(typed_dict):
        raise ValueError("TypedDict subclass required")

    fields_types = typed_dict.__annotations__
    type_transformed = {}

    for field, value in csv_row.items():
        try:
            type_transformed[field] = fields_types[field](value)
        except KeyError:
            print(f"{field} not defined in {typed_dict.__name__}")
            continue

    return type_transformed
