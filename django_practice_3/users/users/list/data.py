from list.models import User

user_1 = User(username="", email="")
user_1.save()
user_2 = User(username="", email="")
user_2.save()
user_3 = User(username="", email="")
user_3.save()
user_4 = User(username="", email="")
user_4.save()
user_5 = User(username="", email="")
user_5.save()

user_1 = User.objects.all()[0]
user_2 = User.objects.all()[1]
user_3 = User.objects.all()[2]
user_4 = User.objects.all()[3]
user_5 = User.objects.all()[4]

user_1.username = "Ivan"
user_1.email = "ivan@email.com"
user_1.save()
user_2.username = "George"
user_2.email = "george@email.com"
user_2.save()
user_3.username = "John"
user_3.email = "john@email.com"
user_3.save()
user_4.username = "Kanul"
user_4.email = "kanul@email.com"
user_4.save()
user_5.username = "Richard"
user_5.email = "richard@email.com"
user_5.save()