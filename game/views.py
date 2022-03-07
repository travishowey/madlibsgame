from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, GameOne, GameTwo, GameThree, GameFour, GameFive, GameSix, GameSeven, GameEight, GameNine, \
    GameTen, GameEleven, GameTwelve, GameThirteen, GameFourteen, GameFifteen
from .forms import GameOneForm, GameTwoForm, GameThreeForm, GameFourForm, GameFiveForm, GameSixForm, GameSevenForm,\
    GameEightForm, GameNineForm, GameTenForm, GameElevenForm, GameTwelveForm, GameThirteenForm, GameFourteenForm, \
    GameFifteenForm
from django.template import loader

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'game/index.html', context)


def create_item(request):
    form = GameOneForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gameone')

    return render(request, 'game/game-one-form.html', {'form': form})


def game_one_page(request):
    item = GameOne.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game1.html', context)


def create_item_two(request):
    form = GameTwoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gametwo')

    return render(request, 'game/game_two_form.html', {'form': form})


def game_two_page(request):
    item = GameTwo.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game2.html', context)


def create_item_three(request):
    form = GameThreeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gamethree')

    return render(request, 'game/game-three-form.html', {'form': form})


def game_three_page(request):
    item = GameThree.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game3.html', context)


def create_item_four(request):
    form = GameFourForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gamefour')

    return render(request, 'game/game-four-form.html', {'form': form})


def game_four_page(request):
    item = GameFour.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game4.html', context)


def create_item_five(request):
    form = GameFiveForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gamefive')

    return render(request, 'game/game-five-form.html', {'form': form})


def game_five_page(request):
    item = GameFive.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game5.html', context)


def create_item_six(request):
    form = GameSixForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gamesix')

    return render(request, 'game/game-six-form.html', {'form': form})


def game_six_page(request):
    item = GameSix.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game6.html', context)


def create_item_seven(request):
    form = GameSevenForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gameseven')

    return render(request, 'game/game-seven-form.html', {'form': form})


def game_seven_page(request):
    item = GameSeven.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game7.html', context)


def create_item_eight(request):
    form = GameEightForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gameeight')

    return render(request, 'game/game-eight-form.html', {'form': form})


def game_eight_page(request):
    item = GameEight.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game8.html', context)


def create_item_nine(request):
    form = GameNineForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gamenine')

    return render(request, 'game/game-nine-form.html', {'form': form})


def game_nine_page(request):
    item = GameNine.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game9.html', context)


def create_item_ten(request):
    form = GameTenForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gameten')

    return render(request, 'game/game-ten-form.html', {'form': form})


def game_ten_page(request):
    item = GameTen.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game10.html', context)


def create_item_eleven(request):
    form = GameElevenForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gameeleven')

    return render(request, 'game/game-eleven-form.html', {'form': form})


def game_eleven_page(request):
    item = GameEleven.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game11.html', context)


def create_item_twelve(request):
    form = GameTwelveForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gametwelve')

    return render(request, 'game/game-twelve-form.html', {'form': form})


def game_twelve_page(request):
    item = GameTwelve.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game12.html', context)


def create_item_thirteen(request):
    form = GameThirteenForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gamethirteen')

    return render(request, 'game/game-thirteen-form.html', {'form': form})


def game_thirteen_page(request):
    item = GameThirteen.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game13.html', context)


def create_item_fourteen(request):
    form = GameFourteenForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gamefourteen')

    return render(request, 'game/game-fourteen-form.html', {'form': form})


def game_fourteen_page(request):
    item = GameFourteen.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game14.html', context)


def create_item_fifteen(request):
    form = GameFifteenForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:gamefifteen')

    return render(request, 'game/game-fifteen-form.html', {'form': form})


def game_fifteen_page(request):
    item = GameFifteen.objects.all()
    context = {
        'items': item,
    }
    print (item)
    return render(request, 'game/game15.html', context)

