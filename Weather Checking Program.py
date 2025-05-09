import requests
import json


API_KEY = "d88394e2908159e11d2f1809faf356aa" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                "City": data["name"],
                "Temperature": data["main"]["temp"],
                "Humidity": data["main"]["humidity"],
                "Weather Condition": data["weather"][0]["description"],
            }
            return weather_data
        else:
            print(f"Error: {data['message']}")
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_menu():
    print("\n" + "=" * 40)
    print("           Weather Report")
    print("=" * 40)
    print("1. Get weather for a city")
    print("2. Save favorite city")
    print("3. Get weather for favorite city")
    print("4. Get weather for multiple cities")
    print("5. Exit")
    print("=" * 40)

# Main program
def weather_report():
    favorite_city = None

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            city = input("Enter the city name: ")
            weather = get_weather(city)
            if weather:
                print("\nWeather Report:")
                for key, value in weather.items():
                    print(f"{key}: {value}")

        elif choice == "2":
            favorite_city = input("Enter your favorite city: ")
            print(f"{favorite_city} has been saved as your favorite city.")

        elif choice == "3":
            if favorite_city:
                weather = get_weather(favorite_city)
                if weather:
                    print("\nWeather Report for Favorite City:")
                    for key, value in weather.items():
                        print(f"{key}: {value}")
            else:
                print("No favorite city saved. Please save a city first.")

        elif choice == "4":
            cities = input("Enter multiple city names separated by commas: ").split(",")
            print("\nWeather Reports:")
            for city in cities:
                city = city.strip()
                weather = get_weather(city)
                if weather:
                    print(f"\nWeather Report for {city}:")
                    for key, value in weather.items():
                        print(f"{key}: {value}")

        elif choice == "5":
            print("Thank you for using the Weather Report program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    weather_report()
