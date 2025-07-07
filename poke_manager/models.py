from django.db.models import (
    Model,
    CharField,
    URLField
)

# Create your models here.
class PokemonType(Model):
    name = CharField(max_length=16, unique=True)
    url = URLField()

    def __str__(self):
        return self.name