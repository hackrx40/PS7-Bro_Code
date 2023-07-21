from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
    'recipient': "HackRx 4.0",
    'offer': "Easy EMI",
    'call_to_action': "Click Now! Limited Time Offer",
    'benefit': "Get 10% off on your first purchase",
    'image_url': "https://scontent-maa2-2.xx.fbcdn.net/v/t1.6435-9/57104038_2300925359929883_1446565781524447232_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=730e14&_nc_ohc=dP2vICM1_78AX9AyfX2&_nc_ht=scontent-maa2-2.xx&oh=00_AfAhQbcJy1b9rtXqPeljSW6vgLN9iOph1Fy19TJqbW-4mA&oe=64E189AC",
    'offer_url': "https://www.facebook.com/hackrx4/"
    }

    return render(request, 'offer.html', context=context)

