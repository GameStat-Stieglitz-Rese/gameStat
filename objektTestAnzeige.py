#import anmeldung

def useranzeigen(user): # Zeigt zu Testzwecken den Inhalt des Objekts an.
    print(user.vorname)
    print(user.nutzername)
    print(user.passwort)
    print(user.email)
    print(user.land)
    print(user.sprache)
    print(user.geburtsdatum)
    print(user.geschlecht)
    print("+++++++++++++BenutzerID+++++++++++++++++")
    print(user.id)
    print(type(user.id))
    
    #anmeldung.home()