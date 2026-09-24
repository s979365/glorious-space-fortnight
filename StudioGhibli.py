import requests
def search_ghibli_film():
    url = "https://ghibliapi.vercel.app/films"
    print("Fetching Studio Ghibli film catalog...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        films = response.json()
        user_choice = input("\nWhat Studio Ghibli movie would you like to watch?").lower()
        found = False
        for film in films:
          if user_choice in film['title'].lower() or user_choice in film['original_title'].lower():
            print(f"Title: {film['title']} ({film['original_title']})")
            found = True
        if not found:
          print(f"\nSorry, no Studio Ghibli movie found matching {user_choice}")
    except Exception as e:
        print(f"An error occured while connecting to the API: {e}")
search_ghibli_film()

