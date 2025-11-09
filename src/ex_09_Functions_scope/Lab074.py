public_toilet = "PB"   #global variable

def home():
    private_toilet = "PT"  #local varibale
    public_toilet = "PBl"
    print(public_toilet)
    print(private_toilet)

def strangers():
    print(public_toilet)
    #print(private_toilet)
home()
strangers()