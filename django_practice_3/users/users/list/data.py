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

user.username = 
user.username = 
user.username = 
user.username = 
user.username = 