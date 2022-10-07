import faker
f = faker.Faker('cz-CZ')
title = f.paragraph(2)
print(title)

content = '\n\n'.join([f.paragraph(6) for _ in range(5)])
print(content)

# content = '\n\n'.join([f.paragraph(6) for _ in range(5)])
# print(content)
# f = faker.Faker()
# print(f.name())
# f = faker.Faker('pl-PL')
# print(f.name())
# content = '\n\n'.join(f.paragraphs(2))
# print(content)



