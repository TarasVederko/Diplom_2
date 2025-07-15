BASE_URL = 'https://stellarburgers.nomoreparties.site'

class EndPoints:
    CREATE_USER = f'{BASE_URL}/api/auth/register'
    LOGIN_USER = f'{BASE_URL}/api/auth/login'
    LOGOUT_USER = f'{BASE_URL}/api/auth/logout'
    UPDATE_TOKEN = f'{BASE_URL}/api/auth/token'
    CREATE_ORDER = f'{BASE_URL}/api/orders'
