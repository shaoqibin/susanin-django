from website.slogans import slogans
import random

def generic(request):
    slogan = random.choice(slogans)
    return {'slogan': slogan}
