import random
from enum import Enum
from colors import Colors
from sizes import Sizes
from races import Races


class AnimalData(Enum):
    FOCA = ('carnivorous', 'Foca', Sizes.M.value, Colors.RED.value)
    HIENA = ('carnivorous', 'Hiena', Sizes.S.value, Colors.RED.value)
    LINCE = ('carnivorous', 'Lince', Sizes.S.value, Colors.RED.value)
    GATO = ('carnivorous', 'Gato', Sizes.XS.value, Colors.RED.value)
    JAGUAR = ('carnivorous', 'Jaguar', Sizes.M.value, Colors.RED.value)
    LOBO = ('carnivorous', 'Lobo', Sizes.S.value, Colors.RED.value)
    GATO_MONTÉS = ('carnivorous', 'Gato montés',
                   Sizes.L.value, Colors.RED.value)
    LOBO_GRIS = ('carnivorous', 'Lobo gris', Sizes.S.value, Colors.RED.value)
    COMADREJA = ('carnivorous', 'Comadreja', Sizes.XS.value, Colors.RED.value)
    LEÓN = ('carnivorous', 'León', Sizes.M.value, Colors.RED.value)
    MARINO = ('carnivorous', 'marino', Sizes.S.value, Colors.RED.value)
    CIVETA = ('carnivorous', 'Civeta', Sizes.XS.value, Colors.RED.value)
    COYOTE = ('carnivorous', 'Coyote', Sizes.XS.value, Colors.RED.value)
    LEOPARDO = ('carnivorous', 'Leopardo', Sizes.S.value, Colors.RED.value)
    MANGOSTA = ('carnivorous', 'Mangosta', Sizes.XS.value, Colors.RED.value)
    MARTA = ('carnivorous', 'Marta', Sizes.XS.value, Colors.RED.value)
    TIGRE_SIBERIANO = ('carnivorous', 'Tigre siberiano',
                       Sizes.M.value, Colors.RED.value)
    TIGRE_DE_BENGALA = ('carnivorous', 'Tigre de bengala',
                        Sizes.M.value, Colors.RED.value)
    OSO_POLAR = ('carnivorous', 'Oso polar', Sizes.L.value, Colors.RED.value)
    NUTRIA = ('carnivorous', 'Nutria', Sizes.XS.value, Colors.RED.value)
    GUEPARDO = ('carnivorous', 'Guepardo', Sizes.M.value, Colors.RED.value)
    GINETA_MANCHADA = ('carnivorous', 'Gineta manchada',
                       Sizes.XS.value, Colors.RED.value)
    PUMA = ('carnivorous', 'Puma', Sizes.S.value, Colors.RED.value)
    PANDA_ROJO = ('carnivorous', 'Panda rojo',
                  Sizes.XS.value, Colors.RED.value)
    PANTERA = ('carnivorous', 'Pantera', Sizes.M.value, Colors.RED.value)
    NEGRA = ('carnivorous', 'negra', Sizes.S.value, Colors.RED.value)
    GINETA_COMÚN = ('carnivorous', 'Gineta común',
                    Sizes.XS.value, Colors.RED.value)
    LINSANGS = ('carnivorous', 'Linsangs', Sizes.XS.value, Colors.RED.value)
    FOSA = ('carnivorous', 'Fosa', Sizes.XS.value, Colors.RED.value)
    MURCIÉLAGO_ESPECTRAL = ('carnivorous', 'Murciélago espectral',
                            Sizes.SMALLEST.value, Colors.RED.value)
    MAPACHE = ('carnivorous', 'Mapache', Sizes.XS.value, Colors.RED.value)
    VISÓN_EUROPEO = ('carnivorous', 'Visón europeo',
                     Sizes.XS.value, Colors.RED.value)
    MURCIÉLAGO_PESCADOR = ('carnivorous', 'Murciélago pescador',
                           Sizes.SMALLEST.value, Colors.RED.value)
    DEMONIO_DE_TASMANIA = ('carnivorous', 'Demonio de Tasmania',
                           Sizes.XS.value, Colors.RED.value)
    MORSA = ('carnivorous', 'Morsa', Sizes.XL.value, Colors.RED.value)
    CHACAL = ('carnivorous', 'Chacal', Sizes.XS.value, Colors.RED.value)
    PANGOLÍN = ('carnivorous', 'Pangolín', Sizes.XS.value, Colors.RED.value)
    HURÓN = ('carnivorous', 'Hurón', Sizes.XS.value, Colors.RED.value)
    GLOTÓN = ('carnivorous', 'Glotón', Sizes.XS.value, Colors.RED.value)
    TEJÓN = ('carnivorous', 'Tejón', Sizes.XS.value, Colors.RED.value)

    CABALLO = ('herbivorous', 'caballo', Sizes.L.value, Colors.GREEN.value)
    CABRA = ('herbivorous', 'cabra', Sizes.S.value, Colors.GREEN.value)
    CANGURO = ('herbivorous', 'canguro', Sizes.M.value, Colors.GREEN.value)
    CEBRA = ('herbivorous', 'cebra', Sizes.L.value, Colors.GREEN.value)
    CIERVO = ('herbivorous', 'ciervo', Sizes.M.value, Colors.GREEN.value)
    CONEJO = ('herbivorous', 'conejo',
              Sizes.SMALLEST.value, Colors.GREEN.value)
    CHINCHILLA = ('herbivorous', 'chinchilla',
                  Sizes.SMALLEST.value, Colors.GREEN.value)
    ELEFANTE = ('herbivorous', 'elefante',
                Sizes.BIGGEST.value, Colors.GREEN.value)
    GACELA = ('herbivorous', 'gacela', Sizes.M.value, Colors.GREEN.value)
    JIRAFA = ('herbivorous', 'jirafa', Sizes.BIGGEST.value, Colors.GREEN.value)
    KOALA = ('herbivorous', 'koala', Sizes.XS.value, Colors.GREEN.value)
    ORUGA = ('herbivorous', 'oruga', Sizes.SMALLEST.value, Colors.GREEN.value)
    OSO_PANDA = ('herbivorous', 'oso panda',
                 Sizes.XL.value, Colors.GREEN.value)
    OVEJA = ('herbivorous', 'oveja', Sizes.S.value, Colors.GREEN.value)
    RINOCERONTE = ('herbivorous', 'rinoceronte',
                   Sizes.BIGGEST.value, Colors.GREEN.value)
    TORTUGA_DE_TIERRA = ('herbivorous', 'tortuga de tierra',
                         Sizes.XS.value, Colors.GREEN.value)
    VACA = ('herbivorous', 'vaca', Sizes.XL.value, Colors.GREEN.value)

    PERRO = ('omnivorous', 'Perro', Sizes.S.value, Colors.RED.value)
    OSO_PARDO = ('omnivorous', 'Oso pardo', Sizes.L.value, Colors.RED.value)
    AVESTRUZ = ('omnivorous', 'avestruz', Sizes.M.value, Colors.BLUE.value)
    CERDO = ('omnivorous', 'cerdo', Sizes.M.value, Colors.BLUE.value)
    CHIMPANCÉ = ('omnivorous', 'chimpancé', Sizes.S.value, Colors.BLUE.value)
    COATÍ = ('omnivorous', 'coatí', Sizes.XS.value, Colors.BLUE.value)
    CUERVO = ('omnivorous', 'cuervo', Sizes.SMALLEST.value, Colors.BLUE.value)
    ERIZO = ('omnivorous', 'erizo', Sizes.SMALLEST.value, Colors.BLUE.value)
    GALLINA = ('omnivorous', 'gallina', Sizes.XS.value, Colors.BLUE.value)
    ÑANDÚ = ('omnivorous', 'ñandú', Sizes.S.value, Colors.BLUE.value)
    OSO = ('omnivorous', 'oso', Sizes.L.value, Colors.BLUE.value)
    RATON = ('omnivorous', 'raton', Sizes.SMALLEST.value, Colors.BLUE.value)
    TORTUGA_MARINA = ('omnivorous', 'tortuga marina',
                      Sizes.M.value, Colors.BLUE.value)
    URRACA = ('omnivorous', 'urraca', Sizes.SMALLEST.value, Colors.BLUE.value)

    def random_existing(self):
        animal_base = random.choice(list(AnimalData)).value
        animal = (animal_base[0], animal_base[1], Sizes.random_between(
            Sizes, int(animal_base[2]*0.85), int(animal_base[2]*1.15)), animal_base[3])
        return animal

    def get_by_name(self, name: str):
        for animal in list(AnimalData):
            if animal.value[1] == name:
                return animal.value
        raise ValueError('{} is not a valid animal name'.format(name))

        return
