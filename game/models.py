from django.db import models

# Create your models here.


class Item(models.Model):

    noun = models.CharField(max_length=200)
    plural_noun = models.CharField(max_length=200)
    verb = models.CharField(max_length=200)
    number = models.IntegerField()
    celebrity_name = models.CharField(max_length=200)


class GameOne(models.Model):

    adjective = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    adjectiveTwo = models.CharField(max_length=200)
    bird = models.CharField(max_length=200)
    room = models.CharField(max_length=200)
    pastTenseVerb = models.CharField(max_length=200)
    verb = models.CharField(max_length=200)
    relative = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    liquid = models.CharField(max_length=200)
    verbWithIng = models.CharField(max_length=200)
    bodyPart = models.CharField(max_length=200)
    pluralNoun = models.CharField(max_length=200)
    verbWithIngTwo = models.CharField(max_length=200)
    nounTwo = models.CharField(max_length=200)


class GameTwo(models.Model):

    personOne = models.CharField(max_length=200)
    personTwo = models.CharField(max_length=200)
    verb = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    nounTwo = models.CharField(max_length=200)
    nounThree = models.CharField(max_length=200)
    nounFour = models.CharField(max_length=200)


class GameThree(models.Model):

    personOne = models.CharField(max_length=200)
    personTwo = models.CharField(max_length=200)
    bread = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    nounTwo = models.CharField(max_length=200)
    nounThree = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)


class GameFour(models.Model):

    familyMember = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)
    adjectiveTwo = models.CharField(max_length=200)
    activity = models.CharField(max_length=200)
    activityTwo = models.CharField(max_length=200)
    pluralNoun = models.CharField(max_length=200)
    adjectiveThree = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    nickName = models.CharField(max_length=200)


class GameFive(models.Model):

    adjective = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    waterForm = models.CharField(max_length=200)
    foodOne = models.CharField(max_length=200)
    foodTwo = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


class GameSix(models.Model):

    noun = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    number = models.IntegerField()
    nounTwo = models.CharField(max_length=200)
    verbWithIng = models.CharField(max_length=200)
    clothing = models.CharField(max_length=200)
    clothingTwo = models.CharField(max_length=200)
    beverage = models.CharField(max_length=200)
    food = models.CharField(max_length=200)


class GameSeven(models.Model):

    person = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)
    adjectiveTwo = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    adjectiveThree = models.CharField(max_length=200)
    nounTwo = models.CharField(max_length=200)
    adjectiveFour = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    verb = models.CharField(max_length=200)
    verbTwo = models.CharField(max_length=200)
    personTwo = models.CharField(max_length=200)
    verbThree = models.CharField(max_length=200)
    adjectiveFive = models.CharField(max_length=200)
    verbFour = models.CharField(max_length=200)


class GameEight(models.Model):

    holiday = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    costume = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)
    bodyPartPlural = models.CharField(max_length=200)
    verb = models.CharField(max_length=200)
    adjectiveTwo = models.CharField(max_length=200)
    nounTwo = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    pluralNoun = models.CharField(max_length=200)


class GameNine(models.Model):

    name = models.CharField(max_length=200)
    setting = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    problem = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)
    adjectiveTwo = models.CharField(max_length=200)
    problemResolution = models.CharField(max_length=200)
    result = models.CharField(max_length=200)


class GameTen(models.Model):
    properNoun = models.CharField(max_length=200)
    verbWithIng = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    pronoun = models.CharField(max_length=200)
    nounTwo = models.CharField(max_length=200)
    verb = models.CharField(max_length=200)


class GameEleven(models.Model):
    verbWithIng = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    verbWithIngTwo = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)
    adjectiveTwo = models.CharField(max_length=200)
    personTwo = models.CharField(max_length=200)
    verb = models.CharField(max_length=200)
    adjectiveThree = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    clothing = models.CharField(max_length=200)
    adjectiveFour = models.CharField(max_length=200)
    adjectiveFive = models.CharField(max_length=200)


class GameTwelve(models.Model):
    verb = models.CharField(max_length=200)
    adjectiveWithLy = models.CharField(max_length=200)
    verbTwo = models.CharField(max_length=200)
    bodyPart = models.CharField(max_length=200)
    plants = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    streetName = models.CharField(max_length=200)
    verbWithIng = models.CharField(max_length=200)
    verbWithIngTwo = models.CharField(max_length=200)
    foodTwo = models.CharField(max_length=200)


class GameThirteen(models.Model):
    container = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)
    adjectiveTwo = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    animal = models.CharField(max_length=200)
    vegetable = models.CharField(max_length=200)
    vegetableTwo = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    adjectiveThree = models.CharField(max_length=200)


class GameFourteen(models.Model):
    name = models.CharField(max_length=200)
    dinosaurType = models.CharField(max_length=200)
    noise = models.CharField(max_length=200)
    animal = models.CharField(max_length=200)
    bodyPart = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    smell = models.CharField(max_length=200)
    number = models.IntegerField()
    game = models.CharField(max_length=200)
    emotion = models.CharField(max_length=200)


class GameFifteen(models.Model):
    food = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    adjectiveTwo = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    nounTwo = models.CharField(max_length=200)


