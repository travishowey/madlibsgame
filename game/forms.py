from django import forms
from .models import Item, GameOne, GameTwo, GameThree, GameFour, GameFive, GameSix, GameSeven, GameEight, GameNine, \
    GameTen, GameEleven, GameTwelve, GameThirteen, GameFourteen, GameFifteen


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['noun', 'plural_noun', 'verb', 'number', 'celebrity_name']


class GameOneForm(forms.ModelForm):
    class Meta:
        model = GameOne
        fields = ['adjective', 'month', 'adjectiveTwo', 'bird', 'room', 'pastTenseVerb', 'verb', 'relative', 'noun',
                  'liquid', 'verbWithIng', 'bodyPart', 'pluralNoun', 'verbWithIngTwo', 'nounTwo']


class GameTwoForm(forms.ModelForm):
    class Meta:
        model = GameTwo
        fields = ['personOne', 'personTwo', 'verb', 'noun', 'nounTwo', 'nounThree', 'nounFour']


class GameThreeForm(forms.ModelForm):
    class Meta:
        model = GameThree
        fields = ['personOne', 'personTwo', 'bread', 'noun', 'nounTwo', 'nounThree', 'adjective']


class GameFourForm(forms.ModelForm):
    class Meta:
        model = GameFour
        fields = ['familyMember', 'adjective', 'adjectiveTwo', 'activity', 'activityTwo', 'pluralNoun',
                  'adjectiveThree', 'noun', 'nickName']


class GameFiveForm(forms.ModelForm):
    class Meta:
        model = GameFive
        fields = ['adjective', 'place', 'color', 'waterForm', 'foodOne', 'foodTwo', 'name']


class GameSixForm(forms.ModelForm):
    class Meta:
        model = GameSix
        fields = ['noun', 'place', 'number', 'nounTwo', 'verbWithIng', 'clothing', 'clothingTwo', 'beverage', 'food']


class GameSevenForm(forms.ModelForm):
    class Meta:
        model = GameSeven
        fields = ['person', 'adjective', 'adjectiveTwo', 'noun', 'adjectiveThree', 'nounTwo', 'adjectiveFour', 'color',
                  'verb', 'verbTwo', 'personTwo', 'verbThree', 'adjectiveFive', 'verbFour']


class GameEightForm(forms.ModelForm):
    class Meta:
        model = GameEight
        fields = ['holiday', 'noun', 'place', 'costume', 'adjective', 'bodyPartPlural', 'verb', 'adjectiveTwo',
                  'nounTwo', 'food', 'pluralNoun']


class GameNineForm(forms.ModelForm):
    class Meta:
        model = GameNine
        fields = ['name', 'setting', 'place', 'problem', 'adjective', 'adjectiveTwo', 'problemResolution', 'result']


class GameTenForm(forms.ModelForm):
    class Meta:
        model = GameTen
        fields = ['properNoun', 'verbWithIng', 'noun', 'pronoun', 'nounTwo', 'verb']


class GameElevenForm(forms.ModelForm):
    class Meta:
        model = GameEleven
        fields = ['verbWithIng', 'person', 'verbWithIngTwo', 'adjective', 'adjectiveTwo', 'personTwo', 'verb',
                  'adjectiveThree', 'food', 'clothing', 'adjectiveFour', 'adjectiveFive']


class GameTwelveForm(forms.ModelForm):
    class Meta:
        model = GameTwelve
        fields = ['verb', 'adjectiveWithLy', 'verbTwo', 'bodyPart', 'plants', 'food', 'noun', 'streetName',
                  'verbWithIng', 'verbWithIngTwo', 'foodTwo']


class GameThirteenForm(forms.ModelForm):
    class Meta:
        model = GameThirteen
        fields = ['container', 'adjective', 'adjectiveTwo', 'noun', 'animal', 'vegetable', 'vegetableTwo', 'color',
                  'adjectiveThree']


class GameFourteenForm(forms.ModelForm):
    class Meta:
        model = GameFourteen
        fields = ['name', 'dinosaurType', 'noise', 'animal', 'bodyPart', 'color', 'smell', 'number', 'game', 'emotion']


class GameFifteenForm(forms.ModelForm):
    class Meta:
        model = GameFifteen
        fields = ['food', 'ingredient', 'adjective', 'person', 'adjectiveTwo', 'place', 'noun', 'nounTwo']
