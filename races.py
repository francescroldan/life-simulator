import random
from enum import Enum
from feedings import Feedings


class Races(Enum):
    CARNIVOROUS = ('seal',
                   'hyena',
                   'lynx',
                   'cat',
                   'jaguar',
                   'wolf',
                   'wildcat',
                   'grey_wolf',
                   'weasel',
                   'sealion',
                   'civet',
                   'coyote',
                   'leopard',
                   'mongoose',
                   'martha',
                   'siberian_tiger',
                   'bengal_tiger',
                   'polar_bear',
                   'otter',
                   'cheetah',
                   'spotted_gin',
                   'red_panda',
                   'cougar',
                   'common_gin',
                   'linsangs',
                   'pit',
                   'bat',
                   'raccoon',
                   'european_mink',
                   'fisher_bat',
                   'tasmanian_devil',
                   'walrus',
                   'jackal',
                   'pangolin',
                   'ferret',
                   'glutton',
                   'badger'
                   )
    HERBIVOROUS = ('horse',
                   'goat',
                   'kangaroo',
                   'zebra',
                   'deer',
                   'rabbit',
                   'chinchilla',
                   'elephant',
                   'gazelle',
                   'giraffe',
                   'koala',
                   'caterpillar',
                   'panda_bear',
                   'sheep',
                   'rhino',
                   'land_turtle',
                   'cow'
                   )
    OMNIVOROUS = ('dog',
                  'grizzly',
                  'ostrich',
                  'pig',
                  'chimpanzee',
                  'coati',
                  'crow',
                  'hedgehog',
                  'hen',
                  'rhea',
                  'bear',
                  'mouse',
                  'sea_turtle',
                  'magpie'
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

    def random_list(self, quantity: int = None):
        all_races = list(Races.CARNIVOROUS.value +
                         Races.HERBIVOROUS.value + Races.OMNIVOROUS.value)
        random.shuffle(all_races)
        if not quantity:
            quantity = len(all_races)
        return all_races[:quantity]
