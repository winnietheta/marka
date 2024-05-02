import requests

BASE_API_URL = 'http://markamark.local/api'


def get_marks(telegram_id):
    return requests.get(BASE_API_URL + '/get_marks.php?telegram_id=' + str(telegram_id)).json()


def add_mark(telegram_id, subject, mark, date):
    return requests.get(
        BASE_API_URL + '/add_mark.php?telegram_id=' + str(telegram_id) + '&subject=' + str(subject) + '&mark=' + str(
            mark) + '&date=' + date).json()


def reset_marks(telegram_id):
    return requests.get(BASE_API_URL + '/reset_marks.php?telegram_id=' + str(telegram_id)).json()


def get_mark(uuid):
    return requests.get(BASE_API_URL + '/get_mark.php?uuid=' + str(uuid)).json()


def delete_mark(uuid):
    return requests.get(BASE_API_URL + '/delete_mark.php?uuid=' + str(uuid)).json()


def import_marks(telegram_id, session_id):
    return requests.get(
        BASE_API_URL + '/import_marks.php?telegram_id=' + str(telegram_id) + '&session_id=' + str(session_id)).json()
