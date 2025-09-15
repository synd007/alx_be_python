user_question = input("What's the weather like today? (sunny/rainy/cold): ")
if user_question.lower() == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_question.lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_question.lower() == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")