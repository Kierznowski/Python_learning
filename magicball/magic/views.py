from django.shortcuts import render

import random

def home(request):
    n = random.randint(1, 20)   
    
    if n == 1:
        answer = "It is certain."
    elif n == 2:
        answer = "It is decidedly so."
    elif n == 3:
        answer = "Without a doubt."
    elif n == 4:
        answer = "Yes definitely."
    elif n == 5:
        answer = "You may rely on it."
    elif n == 6:
        answer = " As I see it, yes."
    elif n == 7:
        answer = "Most likely."
    elif n == 8:
        answer = "Outlook good."
    elif n == 9:
        answer = "Yes."
    elif n == 10:
        answer = "Signs point to yes."
    elif n == 11:
        answer = "Reply hazy, try again."
    elif n == 12:
        answer = "Ask again later."
    elif n == 13:
        answer = "Better not tell you now."
    elif n == 14:
        answer = "Cannot predict now."
    elif n == 15:
        answer = "Concentrate and ask again."
    elif n == 16:
        answer = "Don't count on it."
    elif n == 17:
        answer = "My reply is no."
    elif n == 18:
        answer = "My sources say no."
    elif n == 19:
        answer = "Outlook not so good."
    else:
        answer = "Very doubtful."

    result = {"answer": answer}
    return render(request, "magic/home.html", result)
