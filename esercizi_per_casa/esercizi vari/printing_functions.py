

def make_car(manufacturer: str, model: str, color=None, tow_package=False) -> dict:
    car_info = {
        'manufacturer': manufacturer,
        'model': model,
        'color': color,
        'tow_package': tow_package
    }
    return car_info

