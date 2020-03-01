import pafy
def foobart(URL,type):
    vid=pafy.new(URL)
    if(type=="Video"):
        k=vid.getbestvideo()
    else :
        k=vid.getbestaudio()
    k.download('test.'+k.extension)