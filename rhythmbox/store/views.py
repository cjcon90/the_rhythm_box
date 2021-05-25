# from products.models import Product
from django.shortcuts import render

def index(request):
    """
    Landing/Welcome page for website.
    """
    return render(request, 'store/index.html')


def shop(request):
    # products = Product.objects.all()
    context = {
        'products': [
    {
        "pk": 1,
        "title": "Pearl DC1450S Dennis Chambers Snare",
        "slug": "pearl-dc1450s-dennis-chambers-snare",
        "description": "Considered by many to be one of the greatest drummers of all time, Pearl's Signature Snare drum collaboration with the great Dennis Chambers is a celebration of three decades of partnership, and a unique tribute to his diverse playing talents.",
        "price": "877.00",
        "rating": (4.47 / 5) * 100,
        "num_ratings": 15,
        "image": "https://thumbs.static-thomann.de/thumb/orig/pics/bdb/382510/11288892_800.webp",
        "brand_image": "https://images.static-thomann.de/pics/herstlogos/pearl.gif",
    },
    {
        "pk": 2,
        "title": "Pearl DC1450S Dennis Chambers Snare",
        "slug": "pearl-dc1450s-dennis-chambers-snare",
        "description": "Considered by many to be one of the greatest drummers of all time, Pearl's Signature Snare drum collaboration with the great Dennis Chambers is a celebration of three decades of partnership, and a unique tribute to his diverse playing talents.",
        "price": "877.00",
        "rating": (4.47 / 5) * 100,
        "num_ratings": 15,
        "image": "https://thumbs.static-thomann.de/thumb/orig/pics/bdb/382510/11288892_800.webp",
        "brand_image": "https://images.static-thomann.de/pics/herstlogos/pearl.gif",
    },
    {
        "pk": 3,
        "title": "Pearl DC1450S Dennis Chambers Snare",
        "slug": "pearl-dc1450s-dennis-chambers-snare",
        "description": "Considered by many to be one of the greatest drummers of all time, Pearl's Signature Snare drum collaboration with the great Dennis Chambers is a celebration of three decades of partnership, and a unique tribute to his diverse playing talents.",
        "price": "877.00",
        "rating": (4.47 / 5) * 100,
        "num_ratings": 15,
        "image": "https://thumbs.static-thomann.de/thumb/orig/pics/bdb/382510/11288892_800.webp",
        "brand_image": "https://images.static-thomann.de/pics/herstlogos/pearl.gif",
    },
    {
        "pk": 4,
        "title": "Pearl DC1450S Dennis Chambers Snare",
        "slug": "pearl-dc1450s-dennis-chambers-snare",
        "description": "Considered by many to be one of the greatest drummers of all time, Pearl's Signature Snare drum collaboration with the great Dennis Chambers is a celebration of three decades of partnership, and a unique tribute to his diverse playing talents.",
        "price": "877.00",
        "rating": (4.47 / 5) * 100,
        "num_ratings": 15,
        "image": "https://thumbs.static-thomann.de/thumb/orig/pics/bdb/382510/11288892_800.webp",
        "brand_image": "https://images.static-thomann.de/pics/herstlogos/pearl.gif",
    },
    {
        "pk": 5,
        "title": "Pearl DC1450S Dennis Chambers Snare",
        "slug": "pearl-dc1450s-dennis-chambers-snare",
        "description": "Considered by many to be one of the greatest drummers of all time, Pearl's Signature Snare drum collaboration with the great Dennis Chambers is a celebration of three decades of partnership, and a unique tribute to his diverse playing talents.",
        "price": "877.00",
        "rating": (4.47 / 5) * 100,
        "num_ratings": 15,
        "image": "https://thumbs.static-thomann.de/thumb/orig/pics/bdb/382510/11288892_800.webp",
        "brand_image": "https://images.static-thomann.de/pics/herstlogos/pearl.gif",
    },
]
    }
    return render(request, 'store/shop.html' , context)