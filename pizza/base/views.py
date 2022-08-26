from django.shortcuts import render
from base.models import MailAdresi, Sayfa, GaleriFoto, Menu
import sys
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
import datetime
# Create your views here.

def home(request):
    context = {}
    menu = Menu.objects.get(isim = "Menü (Lütfen Menüyü Buraya Yükleyiniz)")
    anasayfa = Sayfa.objects.get(isim = "Anasayfa" )
    hikayemiz = Sayfa.objects.get(isim = "Hikayemiz")
    rezervasyon = Sayfa.objects.get(isim = "Rezervasyon")
    iletisim = Sayfa.objects.get(isim = "İletişim")

    sliders = [x.fotograf_tag() for x in GaleriFoto.objects.all()]

    context["menu"] = menu.menu_tag()
    
    context["anasayfa_logo"] = anasayfa.logo_tag()
    context["anasayfa_arkaplan"] = anasayfa.arkaplan_tag()

    context["hikayemiz_baslik"] = hikayemiz.baslik
    context["hikayemiz_yazi"] = hikayemiz.yazi
    context["hikayemiz_fotograf"] = hikayemiz.fotograf_tag()


    context["rezervasyon_baslik"] = rezervasyon.baslik
    context["rezervasyon_yazi"] = rezervasyon.yazi
    context["rezervasyon_arkaplan"] = rezervasyon.arkaplan_tag()

    context["iletisim_baslik"] = iletisim.baslik
    context["iletisim_yazi"] = iletisim.yazi 
    context["iletisim_arkaplan"] = iletisim.arkaplan_tag()

    context["sliders"] = sliders


    if request.method == "POST":
        print(request.POST, file = sys.stderr)
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = datetime.datetime.strptime(request.POST.get("date").replace("T"," "), "%Y-%m-%d %H:%M")
        date = date.strftime("%d-%m-%Y %H:%M")
        people = request.POST.get("people")
        print(date, file = sys.stderr)
    
    
        adresses_to_send = [x.adres for x in MailAdresi.objects.all()]

        site = get_current_site(request)
        message = render_to_string('templates/mail.html', {
                        'protocol': 'http',
                        'domain': site.domain,
                        'name': name,
                        'email': email,
                        'phone' : phone,
                        'date': date,
                        'people': people
                    })
        mail_subject = 'Rezervasyon Bildirimi'
        email = EmailMessage(
            mail_subject, message, to=adresses_to_send
        )
        email.send()

        



    return render(request, "templates/index.html",context)