import webbrowser

while True:
    user_input = input('Please enter a topic for the Wikipedia search: ')
    if user_input:
        try:
            url = 'https://www.wikipedia.org/wiki/' + user_input
            webbrowser.open(url)
        except Exception as e:
            print("An error occurred:", e)
    else:
        break
