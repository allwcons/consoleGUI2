def colorText(label,color):
    label.setStyleSheet(f"background-color:{color}")

def error(error):
    r = colorText(error,"red")

def warn(warning):
    r = colorText(error,"yellow")

def simple(text):
    r = colorText(error,"green")

def special(text):
    r = colorText(error,"pink")

def log(text,type="simple"):
    if(type == "simple"):
        simple(text)
    elif(type == "error"):
        error(text)
    elif(type == "warn"):
        warn(text)
    elif(type == "special"):
        special(text)
        

