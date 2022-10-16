from addressValidator import address_validator

def test_address_validator() -> str:

    address = "Calle 3BC #10-2 Barrio San Juan Apartamento 201"
    if address_validator(address):
       return "direccion valida"
    else:
       return "direccion invalida"

if __name__ == "__main__":
    print(test_address_validator())
