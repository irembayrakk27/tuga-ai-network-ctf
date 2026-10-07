from app import application


@application.route("/")
def home():
    return "CTF çalışıyor"