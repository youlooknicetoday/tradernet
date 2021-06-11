def recursive_sort(dict_: dict):
    return {
        key: recursive_sort(value) if isinstance(value, dict)
        else str(value) for key, value in sorted(dict_.items())
    }


def http_build_query(query_data: dict, /, sep='&', temp_key=None):
    result = []
    for key, value in query_data.items():
        key = '%s[%s]' % (temp_key, key) if temp_key else key
        if isinstance(value, dict):
            sub_query = http_build_query(value, sep, key)
        elif isinstance(value, (list, tuple)):
            value = dict(enumerate(value))
            sub_query = http_build_query(value, sep, key)
        else:
            sub_query = '%s=%s' % (key, value)
        result.append(sub_query)
    return sep.join(sub for sub in result)
