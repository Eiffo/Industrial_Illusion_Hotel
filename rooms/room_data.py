from django.utils.translation import gettext_lazy as _

ROOM_INFO = {
    "standard": {
        "title": _("Pokój Standardowy"),
        "description": 
        _("Ten przytulny pokój idealnie sprawdzi się dla jednej lub dwóch osób, oferując komfortowy wypoczynek w przystępnej cenie. Wyposażony w wygodne łóżko typu queen-size, nowoczesną łazienkę z prysznicem, telewizor LCD oraz bezpłatne Wi-Fi, zapewnia wszystko, czego potrzeba do relaksu po dniu zwiedzania lub pracy. Jasne wnętrze oraz stonowana kolorystyka tworzą ciepłą i przyjazną atmosferę, sprzyjającą wypoczynkowi."),
        "image": "img/standard_room.jpg",
    },
    "deluxe": {
        "title": _("Pokój Deluxe"),
        "description":
        _("Pokój Deluxe to doskonały wybór dla tych, którzy cenią sobie nieco więcej przestrzeni i elegancji. Pokój oferuje większy metraż, wygodne łóżko typu king-size, część wypoczynkową z fotelem, a także elegancką łazienkę z wanną i zestawem kosmetyków oraz alkocholi. Duże okna zapewniają mnóstwo naturalnego światła, a nowoczesne wnętrze zostało zaprojektowane z dbałością o każdy szczegół. Idealny zarówno dla par, jak i osób podróżujących służbowo."),
        "image": "img/deluxe_room.jpg",
    },
    "suite": {
        "title": _("Apartament"),
        "description":
        _("Nasze apartamenty to idealna przestrzeń dla rodzin lub gości szukających dłuższego pobytu z dodatkowym komfortem. Składają się z oddzielnej sypialni i salonu, aneksu kuchennego oraz przestronnej łazienki. Dzięki dużej przestrzeni i funkcjonalności zapewniają poczucie prywatności i domowej atmosfery. Każdy apartament urządzony jest w nowoczesnym stylu z elementami przytulnego designu, tworząc idealne miejsce do odpoczynku po intensywnym dniu."),
        "image": "img/suite_room.jpg",
    },
    "penthouse": {
        "title": "Penthouse",
        "description":
        _("Penthouse to nasza najbardziej ekskluzywna opcja zakwaterowania – luksusowy apartament na najwyższym piętrze z panoramicznym widokiem na góry. Oferuje przestronny salon, elegancką sypialnię, prywatny taras oraz designerską łazienkę z wanną wolnostojącą i prysznicem typu walk-in. Wysokiej klasy wykończenie, indywidualny system nagłośnienia i możliwość zamówienia obsługi pokojowej 24/7 sprawiają, że jest to idealna opcja dla najbardziej wymagających gości lub wyjątkowych okazji, takich jak rocznice czy wieczory panieńskie."),
        "image": "img/penthouse_room1.jpg",
    },
}