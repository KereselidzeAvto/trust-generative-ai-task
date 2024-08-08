from faker import Faker


class FakeData:
    fake = Faker()

    def generate_email(self):
        return self.fake.email()

    def generate_first_name(self):
        return self.fake.first_name()

    def generate_last_name(self):
        return self.fake.last_name()

    def generate_password(self):
        return self.fake.password(
            length=10,
            digits=True,
            upper_case=True,
            lower_case=True,
            special_chars=False
        )

    def generate_address(self):
        return self.fake.street_address()

    def generate_city(self):
        return self.fake.city()

    def generate_zip_code(self):
        return self.fake.zipcode()

    def generate_phone_number(self):
        return self.fake.phone_number()
