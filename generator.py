from faker import Faker

faker = Faker()

def generator_user_body():
    generator_user_body ={
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.name()
    }
    return generator_user_body
