import webbrowser as wb

def webauto():
    chrome_path="/usr/bin/google-chrome"
    URLS = (
        "github.com/Gribesh",
        "gmail.com"
    )
    for url in URLS:
        print("opening urls " + url)
        wb.get(chrome_path).open(URLS)
webauto()