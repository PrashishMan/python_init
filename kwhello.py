def get_people(**kwargs):
	if "Prashish" in kwargs and kwargs.get("Prashish") == "Special":
		print("Special Greetings Prashish Man Singh")
	elif "Prashish" in kwargs:
		print( f" {kwargs.get('Prashish')} Prashish Man Singh")
	else:
		print("Who again?")

get_people(Prashish = "Hello")
get_people(Bob = "Hello")
get_people(Prashish = "Special")
get_people(Prashish = "Special", Bob = "Special")