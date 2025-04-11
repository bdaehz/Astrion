# Astrion
un proyecto de una red social hecho en django

# Librerias
pip install django-otp django-two-factor-auth qrcode phonenumbers

si sigue dando error, hay que acceder a:
disco_local(c)/"aca el usuario que tengas sin comillas"/AppData/Local/Programs/Python/"aca va la version mas reciente de python, sin comillas esto tambien"/Lib/django/site-package/two_factor/urls.py

ej:

C:\Users\Alumnos\AppData\Local\Programs\Python\Python313\Lib\site-packages\two_factor

y abrimos para editar el archivo: "urls.py"

vamos a lo ultimo del archivo y escribimos esto:

#urlpatterns = (core + profile + plugin_urlpatterns, 'two_factor')

app_name = "two_factor"
urlpatterns = core + profile + plugin_urlpatterns