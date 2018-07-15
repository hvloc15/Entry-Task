def filter_list_by_type(list_event, type):
    if type == "none":
        return list_event
    else:
        return list_event.filter(type = type)


def filter_list_by_date_ranges(list_event, start_date, end_date):
    if start_date == 0 and end_date == 0:
        return list_event
    elif end_date == 0:
        return list_event.filter(date__gte = start_date)
    else:
        return list_event.filter(date__gte = start_date, date__lte = end_date )


def paginate_list(list_event, page, page_size):
    start_index = (page - 1) * page_size
    events = list_event[start_index: start_index + page_size]
    return events

