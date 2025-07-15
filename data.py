class BodyAnswer:
    USER_ALREADY_EXIST = {
    "success": False,
    "message": "User already exists"
    }

    ALL_FIELDS_ARE_REQUIRED = {
    "success": False,
    "message": "Email, password and name are required fields"
    }

    WRONG_EMAIL_OR_PASSWORD = {
    "success": False,
    "message": "email or password are incorrect"
    }

    ID_INGREDIENTS_REQUIRED = {
    "success": False,
    "message": "Ingredient ids must be provided"
    }


class BodyOrder:
    ZERO_INGREDIENTS = {
        "ingredients": []
    }

    THREE_INGREDIENTS = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa76", "61c0c5a71d1f82001bdaaa75"]
    }

    WRONG_INGREDIENTS = {
        "ingredients": ["123123123", "qweasdzxc"]
    }
