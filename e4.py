import webbrowser

user_term = input("Enter a search : ")
url = f"https://www.google.com/search?q={user_term}"
webbrowser.open(url)

