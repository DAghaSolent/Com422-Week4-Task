from Dog import Dog
from Enclosure import Enclosure
from Kennel_Company import Kennel_Company
import pytest


def load_enclosures_stub(self):
    return [
        Enclosure(1, 10.50, 5),
        Enclosure(2, 15.00, 3),
        Enclosure(3, 5.99, 10),
    ]


def add_occupant_stub(self, dog):
    self.occupants.append(dog)


@pytest.fixture
def kennel_company_with_dogs(monkeypatch):
    monkeypatch.setattr(Kennel_Company, "load_enclosures", load_enclosures_stub)
    company = Kennel_Company()
    return company


def test_book_dog(monkeypatch, kennel_company_with_dogs):

    dog1 = Dog("Brian", "Peter", 12, "Jack Russell", "Annoying")
    dog2 = Dog("Anubis", "Ra", 100, "Jackal", "Death bringer")
    monkeypatch.setattr(Enclosure, "add_occupant", add_occupant_stub)
    monkeypatch.setattr(Enclosure, "check_suitability", lambda self, dog: True)
    kennel_company_with_dogs.book_dog(dog1)
    kennel_company_with_dogs.book_dog(dog2)

    assert kennel_company_with_dogs.spaces_left() == 16


def test_remove_dog(monkeypatch, kennel_company_with_dogs):

    kennel_company_with_dogs.remove_dog("Brian")
    monkeypatch.setattr(Kennel_Company, "is_authorised", lambda self, dog:True)
    assert kennel_company_with_dogs.spaces_left() == 18
