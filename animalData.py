import random
from enum import Enum
from colors import Colors
from sizes import Sizes
from feedings import Feedings


class AnimalData(Enum):
    SEAL = (Feedings.CARNIVOROUS.value, 'seal',
            Sizes.M.value, Colors.RED.value)
    HYENA = (Feedings.CARNIVOROUS.value, 'hyena',
             Sizes.S.value, Colors.RED.value)
    LYNX = (Feedings.CARNIVOROUS.value, 'lynx',
            Sizes.S.value, Colors.RED.value)
    CAT = (Feedings.CARNIVOROUS.value, 'cat',
           Sizes.XS.value, Colors.RED.value)
    JAGUAR = (Feedings.CARNIVOROUS.value, 'jaguar',
              Sizes.M.value, Colors.RED.value)
    WOLF = (Feedings.CARNIVOROUS.value, 'wolf',
            Sizes.S.value, Colors.RED.value)
    WILDCAT = (Feedings.CARNIVOROUS.value, 'wildcat',
               Sizes.L.value, Colors.RED.value)
    GREY_WOLF = (Feedings.CARNIVOROUS.value, 'grey_wolf',
                 Sizes.S.value, Colors.RED.value)
    WEASEL = (Feedings.CARNIVOROUS.value, 'weasel',
              Sizes.XS.value, Colors.RED.value)
    SEALION = (Feedings.CARNIVOROUS.value, 'sealion',
               Sizes.M.value, Colors.RED.value)
    CIVET = (Feedings.CARNIVOROUS.value, 'civet',
             Sizes.XS.value, Colors.RED.value)
    COYOTE = (Feedings.CARNIVOROUS.value, 'coyote',
              Sizes.XS.value, Colors.RED.value)
    LEOPARD = (Feedings.CARNIVOROUS.value, 'leopard',
               Sizes.S.value, Colors.RED.value)
    MONGOOSE = (Feedings.CARNIVOROUS.value, 'mongoose',
                Sizes.XS.value, Colors.RED.value)
    MARTHA = (Feedings.CARNIVOROUS.value, 'martha',
              Sizes.XS.value, Colors.RED.value)
    SIBERIAN_TIGER = (Feedings.CARNIVOROUS.value, 'siberian_tiger',
                      Sizes.M.value, Colors.RED.value)
    BENGAL_TIGER = (Feedings.CARNIVOROUS.value, 'bengal_tiger',
                    Sizes.M.value, Colors.RED.value)
    POLAR_BEAR = (Feedings.CARNIVOROUS.value, 'polar_bear',
                  Sizes.L.value, Colors.RED.value)
    OTTER = (Feedings.CARNIVOROUS.value, 'otter',
             Sizes.XS.value, Colors.RED.value)
    CHEETAH = (Feedings.CARNIVOROUS.value, 'cheetah',
               Sizes.M.value, Colors.RED.value)
    SPOTTED_GIN = (Feedings.CARNIVOROUS.value, 'spotted_gin',
                   Sizes.XS.value, Colors.RED.value)
    RED_PANDA = (Feedings.CARNIVOROUS.value, 'red_panda',
                 Sizes.XS.value, Colors.RED.value)
    COUGAR = (Feedings.CARNIVOROUS.value, 'cougar',
              Sizes.M.value, Colors.RED.value)
    COMMON_GIN = (Feedings.CARNIVOROUS.value, 'common_gin',
                  Sizes.XS.value, Colors.RED.value)
    LINSANGS = (Feedings.CARNIVOROUS.value, 'linsangs',
                Sizes.XS.value, Colors.RED.value)
    PIT = (Feedings.CARNIVOROUS.value, 'pit',
           Sizes.XS.value, Colors.RED.value)
    BAT = (Feedings.CARNIVOROUS.value, 'bat',
           Sizes.SMALLEST.value, Colors.RED.value)
    RACCOON = (Feedings.CARNIVOROUS.value, 'raccoon',
               Sizes.XS.value, Colors.RED.value)
    EUROPEAN_MINK = (Feedings.CARNIVOROUS.value, 'european_mink',
                     Sizes.XS.value, Colors.RED.value)
    FISHER_BAT = (Feedings.CARNIVOROUS.value, 'fisher_bat',
                  Sizes.SMALLEST.value, Colors.RED.value)
    TASMANIAN_DEVIL = (Feedings.CARNIVOROUS.value, 'tasmanian_devil',
                       Sizes.XS.value, Colors.RED.value)
    WALRUS = (Feedings.CARNIVOROUS.value, 'walrus',
              Sizes.XL.value, Colors.RED.value)
    JACKAL = (Feedings.CARNIVOROUS.value, 'jackal',
              Sizes.XS.value, Colors.RED.value)
    PANGOLIN = (Feedings.CARNIVOROUS.value, 'pangolin',
                Sizes.XS.value, Colors.RED.value)
    FERRET = (Feedings.CARNIVOROUS.value, 'ferret',
              Sizes.XS.value, Colors.RED.value)
    GLUTTON = (Feedings.CARNIVOROUS.value, 'glutton',
               Sizes.XS.value, Colors.RED.value)
    BADGER = (Feedings.CARNIVOROUS.value, 'badger',
              Sizes.XS.value, Colors.RED.value)

    HORSE = (Feedings.HERBIVOROUS.value, 'horse',
             Sizes.L.value, Colors.GREEN.value)
    GOAT = (Feedings.HERBIVOROUS.value, 'goat',
            Sizes.S.value, Colors.GREEN.value)
    KANGAROO = (Feedings.HERBIVOROUS.value, 'kangaroo',
                Sizes.M.value, Colors.GREEN.value)
    ZEBRA = (Feedings.HERBIVOROUS.value, 'zebra',
             Sizes.L.value, Colors.GREEN.value)
    DEER = (Feedings.HERBIVOROUS.value, 'deer',
            Sizes.M.value, Colors.GREEN.value)
    RABBIT = (Feedings.HERBIVOROUS.value, 'rabbit',
              Sizes.SMALLEST.value, Colors.GREEN.value)
    CHINCHILLA = (Feedings.HERBIVOROUS.value, 'chinchilla',
                  Sizes.SMALLEST.value, Colors.GREEN.value)
    ELEPHANT = (Feedings.HERBIVOROUS.value, 'elephant',
                Sizes.BIGGEST.value, Colors.GREEN.value)
    GAZELLE = (Feedings.HERBIVOROUS.value, 'gazelle',
               Sizes.M.value, Colors.GREEN.value)
    GIRAFFE = (Feedings.HERBIVOROUS.value, 'giraffe',
               Sizes.BIGGEST.value, Colors.GREEN.value)
    KOALA = (Feedings.HERBIVOROUS.value, 'koala',
             Sizes.XS.value, Colors.GREEN.value)
    CATERPILLAR = (Feedings.HERBIVOROUS.value, 'caterpillar',
                   Sizes.SMALLEST.value, Colors.GREEN.value)
    PANDA_BEAR = (Feedings.HERBIVOROUS.value, 'panda_bear',
                  Sizes.L.value, Colors.GREEN.value)
    SHEEP = (Feedings.HERBIVOROUS.value, 'sheep',
             Sizes.S.value, Colors.GREEN.value)
    RHINO = (Feedings.HERBIVOROUS.value, 'rhino',
             Sizes.BIGGEST.value, Colors.GREEN.value)
    LAND_TURTLE = (Feedings.HERBIVOROUS.value, 'land_turtle',
                   Sizes.XS.value, Colors.GREEN.value)
    COW = (Feedings.HERBIVOROUS.value, 'cow',
           Sizes.L.value, Colors.GREEN.value)

    DOG = (Feedings.OMNIVOROUS.value, 'dog',
           Sizes.S.value, Colors.RED.value)
    GRIZZLY = (Feedings.OMNIVOROUS.value, 'grizzly',
               Sizes.L.value, Colors.RED.value)
    OSTRICH = (Feedings.OMNIVOROUS.value, 'ostrich',
               Sizes.M.value, Colors.BLUE.value)
    PIG = (Feedings.OMNIVOROUS.value, 'pig',
           Sizes.M.value, Colors.BLUE.value)
    CHIMPANZEE = (Feedings.OMNIVOROUS.value, 'chimpanzee',
                  Sizes.S.value, Colors.BLUE.value)
    COATI = (Feedings.OMNIVOROUS.value, 'coati',
             Sizes.XS.value, Colors.BLUE.value)
    CROW = (Feedings.OMNIVOROUS.value, 'crow',
            Sizes.SMALLEST.value, Colors.BLUE.value)
    HEDGEHOG = (Feedings.OMNIVOROUS.value, 'hedgehog',
                Sizes.SMALLEST.value, Colors.BLUE.value)
    HEN = (Feedings.OMNIVOROUS.value, 'hen',
           Sizes.XS.value, Colors.BLUE.value)
    RHEA = (Feedings.OMNIVOROUS.value, 'rhea',
            Sizes.S.value, Colors.BLUE.value)
    BEAR = (Feedings.OMNIVOROUS.value, 'bear',
            Sizes.L.value, Colors.BLUE.value)
    MOUSE = (Feedings.OMNIVOROUS.value, 'mouse',
             Sizes.SMALLEST.value, Colors.BLUE.value)
    SEA_TURTLE = (Feedings.OMNIVOROUS.value, 'sea_turtle',
                  Sizes.M.value, Colors.BLUE.value)
    MAGPIE = (Feedings.OMNIVOROUS.value, 'magpie',
              Sizes.SMALLEST.value, Colors.BLUE.value)

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
