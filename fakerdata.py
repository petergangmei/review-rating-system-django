from faker import Faker
from comments.models import Review
f = Faker()

for _ in range(10):
    Review.objects.create(name=f.name(),stars=5, comment=f.text())
    print(f.name())
    print(f.email())
    print(f.address())
    print(f.text())
    print("----")