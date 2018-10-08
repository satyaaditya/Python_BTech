import webbrowser,sys,pyperclip
def open_maps():
    if sys.argv > 1 :
        location = ' '.join(sys.argv[1:])   #get address from cmd
    else :
        location = pyperclip.paste()        #get address from clipboard

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    url = 'http://www.google.com/maps/place/' + location
    webbrowser.get(chrome_path).open(url)

if __name__ == "__main__" :
    open_maps()


