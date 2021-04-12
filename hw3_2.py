def person_inf(name, surname, year_birth, city, email, phone):
    print(f'name: {name}, surname: {surname}; year_birth: {year_birth};\
 city: {city}; email: {email}; phone: {phone}')

person_inf(
    input('name: '),
    input('surname: '),
    input('year_birth: '),
    input('city: '),
    input('email: '),
    input('phone: ')
)