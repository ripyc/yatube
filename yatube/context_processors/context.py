import datetime as dt


def current_year(request):
    """ Добавляет переменную с текущим годом.
    """
    current_year = dt.datetime.today().year
    return {"current_year": current_year}
