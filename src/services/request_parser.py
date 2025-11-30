def parse_filters(request_args: dict) -> tuple:
    # get filters
    filters = []
    i = 0
    while True:
        try:
            field = request_args[f'filters[{i}][field]']
            op = request_args[f'filters[{i}][op]']
            value = request_args[f'filters[{i}][value]']
            if field and op:
                filters.append({
                    "field": field,
                    "op": op,
                    "value": value,
                })
            else:
                break
            i += 1
        except: 
            break
    
    return filters
    