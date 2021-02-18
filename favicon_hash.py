import mmh3, sys, requests, codecs

class Favicon:
    def __init__(self, args):
        self.args = args
    
    def GetFavicon(self):
        try:
            r = requests.get(self.args['url']+"/favicon.ico")
            favicon = codecs.encode(r.content,"base64")
            return str(mmh3.hash(favicon))

        except:
            return "Not Found"

if __name__ == "__main__":
    args = {
        "url": sys.argv[1]
    }

    Favicon = Favicon(args).GetFavicon()
    print(Favicon)