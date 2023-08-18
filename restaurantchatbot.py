import re

class RestaurantChatbot:
    def __init__(self):
        self.add_initial_message()
    
    def add_initial_message(self):
        print("Chatbot: Hi there! I'm the restaurant recommendation chatbot. What type of cuisine do you like?")
    
    def start(self):
        while True:
            user_input = input("You: ")
            response = self.restaurant_recommendation(user_input)
            print("Chatbot:", response)
            
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye! Enjoy your meal!")
                break
    
    def restaurant_recommendation(self, user_input):
        user_input = user_input.lower()
        
        patterns = {
            r".*hii.*|.*hello.*": "Hi there! I'm the restaurant recommendation chatbot. What type of cuisine do you like?",
            r".*i am in mood for chinese cusine.*": "How about trying a Chinese restaurant? They offer a variety of dishes with diverse flavors.",
            r".*italian cusine.*": "Italian restaurants are a great choice if you're craving pasta and pizza. Give it a try!",
            r".*what about mexican cusine.*": "Craving some Mexican food? Tacos, burritos, and guacamole await you!",
            r".*japanese cusine.*": "How about trying a Japanese restaurant? They offer sushi, sashimi, and more.",
            r".*indian cusine.*": "Indian cuisine is known for its rich spices and flavors. It's a delicious option to explore.",
            r".*thanks.*": "You're welcome! Enjoy your meal. If you have more questions, feel free to ask.",
            r".*goodbye.*": "Goodbye! If you ever need more restaurant recommendations, don't hesitate to return.",
        }
        
        for pattern, response in patterns.items():
            if re.search(pattern, user_input):
                return response
        
        return "I'm sorry, I don't have recommendations for that cuisine."

if __name__ == "__main__":
    chatbot = RestaurantChatbot()
    chatbot.start()