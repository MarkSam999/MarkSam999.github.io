from cities.models import AquaPark
from cities.models import City

city_1 = City(name="Москва", description="a")
city_1.save()
city_2 = City(name="Санкт-Петербург", description="a")
city_2.save()
city_3 = City(name="Казань", description="a")
city_3.save()
city_4 = City(name="Сочи", description="a")
city_4.save()
city_5 = City(name="Екатеринбург", description="a")
city_5.save()
city_6 = City(name="Новосибирск", description="a")
city_6.save()
city_7 = City(name="Воронеж", description="a")
city_7.save()
city_8 = City(name="Краснодар", description="a")
city_8.save()
city_9 = City(name="Ростов-на-Дону", description="a")
city_9.save()
city_10 = City(name="Нижний Новгород", description="a")
city_10.save()

aquapark_1 = AquaPark(name="Ква-ква парк", address="address", description="a")
aquapark_1.save()
aquapark_2 = AquaPark(name="карибия", address="address", description="a")
aquapark_2.save()
aquapark_3 = AquaPark(name="южный", address="address", description="a")
aquapark_3.save()
aquapark_4 = AquaPark(name="ривьера", address="address", description="a")
aquapark_4.save()
aquapark_5 = AquaPark(name="ривьера_2", address="address", description="a")
aquapark_5.save()
aquapark_6 = AquaPark(name="казанская лагуна", address="address", description="a")
aquapark_6.save()
aquapark_7 = AquaPark(name="амфибиус", address="address", description="a")
aquapark_7.save()
aquapark_8 = AquaPark(name="поляна", address="address", description="a")
aquapark_8.save()
aquapark_9 = AquaPark(name="лето", address="address", description="a")
aquapark_9.save()
aquapark_10 = AquaPark(name="весёлая лагуна", address="address", description="a")
aquapark_10.save()
aquapark_11 = AquaPark(name="аквамир", address="address", description="a")
aquapark_11.save()
aquapark_12 = AquaPark(name="тропикана", address="address", description="a")
aquapark_12.save()
aquapark_13 = AquaPark(name="океан", address="address", description="a")
aquapark_13.save()
aquapark_14 = AquaPark(name="гроза", address="address", description="a")
aquapark_14.save()
aquapark_15 = AquaPark(name="солнечный", address="address", description="a")
aquapark_15.save()
aquapark_16 = AquaPark(name="плай", address="address", description="a")
aquapark_16.save()
aquapark_17 = AquaPark(name="пляж", address="address", description="a")
aquapark_17.save()
aquapark_18 = AquaPark(name="гроза_2", address="address", description="a")
aquapark_18.save()
aquapark_19 = AquaPark(name="лето_2", address="address", description="a")
aquapark_19.save()
aquapark_20 = AquaPark(name="пляж_2", address="address", description="a")
aquapark_20.save()

city_1 = City.objects.all()[0]
city_2 = City.objects.all()[1]
city_3 = City.objects.all()[2]
city_4 = City.objects.all()[3]
city_5 = City.objects.all()[4]
city_6 = City.objects.all()[5]
city_7 = City.objects.all()[6]
city_8 = City.objects.all()[7]
city_9 = City.objects.all()[8]
city_10 = City.objects.all()[9]

aquapark_1 = AquaPark.objects.all()[0]
aquapark_2 = AquaPark.objects.all()[1]
aquapark_3 = AquaPark.objects.all()[2]
aquapark_4 = AquaPark.objects.all()[3]
aquapark_5 = AquaPark.objects.all()[4]
aquapark_6 = AquaPark.objects.all()[5]
aquapark_7 = AquaPark.objects.all()[6]
aquapark_8 = AquaPark.objects.all()[7]
aquapark_9 = AquaPark.objects.all()[8]
aquapark_10 = AquaPark.objects.all()[9]
aquapark_11 = AquaPark.objects.all()[10]
aquapark_12 = AquaPark.objects.all()[11]
aquapark_13 = AquaPark.objects.all()[12]
aquapark_14 = AquaPark.objects.all()[13]
aquapark_15 = AquaPark.objects.all()[14]
aquapark_16 = AquaPark.objects.all()[15]
aquapark_17 = AquaPark.objects.all()[16]
aquapark_18 = AquaPark.objects.all()[17]
aquapark_19 = AquaPark.objects.all()[18]
aquapark_20 = AquaPark.objects.all()[19]

aquapark_1.city.add(city_1)
aquapark_2.city.add(city_1)
aquapark_3.city.add(city_2)
aquapark_4.city.add(city_2)
aquapark_5.city.add(city_)
aquapark_6.city.add(city_)
aquapark_7.city.add(city_)
aquapark_8.city.add(city_)
aquapark_9.city.add(city_)
aquapark_10.city.add(city_)
aquapark_11.city.add(city_)
aquapark_12.city.add(city_)
aquapark_13.city.add(city_)
aquapark_14.city.add(city_)
aquapark_15.city.add(city_)
aquapark_16.city.add(city_)
aquapark_17.city.add(city_9)
aquapark_18.city.add(city_9)
aquapark_19.city.add(city_10)
aquapark_20.city.add(city_10)