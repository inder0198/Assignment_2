from django.shortcuts import render
from string import ascii_letters

def index(request):
    return render(request,"input.html")

def vowel(request):
    str1 = request.POST['str1']
    sr = 1
    first = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for j in range(sr):
        for i in str1:
            if i in vowels:
                first = first + i.upper()
            else:
                first = first + i
    else:
        return render(request, "home.html", {"result": first})

def reverse(request):
    str2 = request.POST['str2']
    # print(str2)
    words = str2.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return render(request, "home.html", {"result": newSentence})

def alpha_numeric_order(request):
    str3 = request.POST['str3']
    se = 1
    third=""
    words = str3.split()
    for j in range(se):
        for i in words:
            a = i
            res = ''.join(sorted(a))
            third = third + str(res) + " "
    else:
        return render(request, "home.html", {"result": third})

def traverse(request):
    str4 = request.POST['str4']
    a = "".join(dict.fromkeys(str4))
    return render(request, "home.html", {"result": a})

def ascii(request):
    str5 = request.POST['str5']
    sw = 1
    fifth = ""
    for j in range(sw):
        for c in str5:
            if c in ascii_letters:
                fifth = fifth + ascii_letters[(ascii_letters.index(c) + 2) % len(ascii_letters)]
            elif c == " ":
                fifth = fifth + " "

    else:
        return render(request, "home.html", {"result": fifth})