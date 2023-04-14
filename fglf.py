class OrganizationAddress:
    def __init__(self, city, street, zip_code, house=None, apartment=None):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.house = house
        self.apartment = apartment

    @property
    def address(self):
        if self.house:
            return f"{self.city}, {self.street}, дом {self.house}, {self.zip_code}"
        elif self.apartment:
            return f"{self.city}, {self.street}, квартира {self.apartment}, {self.zip_code}"
        else:
            raise ValueError("Должен быть указан дом или квартира ")

    def set_city(self, new_city):
        self.city = new_city

    def set_street(self, new_street):
        self.street = new_street

    def set_zip_code(self, new_zip_code):
        self.zip_code = new_zip_code

    def set_house(self, new_house):
        self.house = new_house
        self.apartment = None

    def set_apartment(self, new_apartment):
        self.apartment = new_apartment
        self.house = None

address1 = OrganizationAddress(city='Москва', street='Ленинская', zip_code=40080, house=31)
print(address1.address)

address2 = OrganizationAddress(city='Санкт-Петербург', street='Невский', zip_code=190000, apartment=42)
print(address2.address)