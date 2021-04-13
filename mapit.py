import webbrowser, sys, pyperclip, os

sys.argv #['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed

if len(sys.argv) > 1:
    #['mapit.py', '870', 'Valencia', 'St.']
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
pyperclip.copy('5019 Royal Cypress Dr.')
webbrowser.open('https://www.google.com/maps/place/' + address)




