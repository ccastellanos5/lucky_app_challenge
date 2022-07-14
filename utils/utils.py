def get_quantity_number(txt):
    return [int(s) for s in txt.split() if s.isdigit()][0]