import random
from enum import Enum
from feedings import Feedings


class Races(Enum):
    CARNIVOROUS = ('Foca',
                   'Hiena',
                   'Lince',
                   'Gato',
                   'Jaguar',
                   'Lobo',
                   'Gato montés',
                   'León',
                   'Lobo gris',
                   'Comadreja',
                   'León',
                   'marino',
                   'Civeta',
                   'Coyote',
                   'Leopardo',
                   'Mangosta',
                   'Marta',
                   'Cachalote',
                   'Tigre siberiano',
                   'Ballena',
                   'azul',
                   'Delfín',
                   'Tigre de bengala',
                   'Ballena',
                   'jorobada',
                   'Oso pardo',
                   'Orca',
                   'Beluga',
                   'Oso',
                   'polar',
                   'Nutria',
                   'Narval',
                   'Guepardo',
                   'Gineta',
                   'manchada',
                   'Perro',
                   'Puma',
                   'Panda rojo',
                   'Pantera',
                   'negra',
                   'Gineta común',
                   'Linsangs',
                   'Fosa',
                   'Murciélago espectral',
                   'Mapache',
                   'Visón europeo',
                   'Murciélago pescador',
                   'Demonio de Tasmania',
                   'Serval',
                   'Morsa',
                   'Chacal',
                   'Pangolín',
                   'Hurón',
                   'Glotón',
                   'Tejón',
                   )
    HERBIVOROUS = ('caballo',
                   'cabra',
                   'canguro',
                   'cebra',
                   'ciervo',
                   'conejo',
                   'chinchilla',
                   'elefante',
                   'gacela',
                   'jirafa',
                   'koala',
                   'oruga',
                   'oso panda',
                   'oveja',
                   'rinoceronte',
                   'tortuga de tierra',
                   'vaca',
                   )
    OMNIVOROUS = ('avestruz',
                  'cerdo',
                  'chimpancé',
                  'coatí',
                  'cuervo',
                  'erizo',
                  'gallina',
                  'ñandú',
                  'oso',
                  'piraña',
                  'roedor',
                  'tortuga marina',
                  'urraca',
                  )

    def random_by_feeds(self, feed: str):
        if feed == Feedings.CARNIVOROUS.value:
            return self.random_carnivorous(self)
        elif feed == Feedings.HERBIVOROUS.value:
            return self.random_herbivorous(self)
        elif feed == Feedings.OMNIVOROUS.value:
            return self.random_omnivorous(self)
        else:
            raise Exception('Feed "' + feed + '" is not valid value')

    def random_carnivorous(self):
        return random.choice(list(Races.CARNIVOROUS.value))

    def random_herbivorous(self):
        return random.choice(list(Races.HERBIVOROUS.value))

    def random_omnivorous(self):
        return random.choice(list(Races.OMNIVOROUS.value))

    def random(self):
        return random.choice(list(Races.CARNIVOROUS.value + Races.HERBIVOROUS.value + Races.OMNIVOROUS.value))
