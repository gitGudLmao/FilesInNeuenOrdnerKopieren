import shutil
import os
from re import sub
# standard extensions:
videoExtensions = ('.mp4', '.mkv', '.avi')


# Berücksichtigt alle Subfolder
print('In welchem Pfad möchten Sie Ordner Anlegen?: ')
quelle = input()
files = os.listdir(quelle)
print("Folgende Ordner wurden in " + quelle + " gefunden: ")
print(files)

print("Wie soll der Ordner heißen der in allen unterverzeichnissen angelegt wird?: ")
ordnerName = input()

# ordner erstellen:
for f in files:
    if not os.path.exists(quelle + '/' + f + '/' + ordnerName):
        os.makedirs(quelle + '/' + f + '/' + ordnerName)
        print('Folder ' + ordnerName + ' in ' + quelle + f + ' created')


# files verschieben:
# user kann fileextensions hinzufügen:
def tupeladd(anzahl):
    t = ()
    while anzahl > 0:
        print("Geben Sie den Dateityp ein der gemoved werden soll(.dateityp): ")
        eingabe = input()
        t += (eingabe,)
        anzahl -= 1
    return t


print("Möchten Sie ein weiteren Dateityp moven?: ")
janein = input().lower()
if janein == 'ja':
    print("Wie viele Dateitypen möchten Sie hinzufügen? ")
    anzahl = input()
    anzahl = int(anzahl)
    userExtensions = (tupeladd(anzahl))
    extension = videoExtensions + userExtensions
    for e in extension:

        print("Es werden alle Dateien mit der endung:  " + e + " verschoben.")
else:
    print("Keine Dateitypen hinzugefügt")
    print("Es wird nur: " + videoExtensions + " von: "+ quelle + "nach" + ordnerName + " gemoved")
    extensions = videoExtensions






daten = os.listdir(quelle)
for x in daten:
    toBeMoved = os.listdir(quelle + '/' + x)
    for element in toBeMoved:
        if element.endswith(tuple(extension)) or element == 'gesehen':
            shutil.move(quelle + '/' + x + '/' + element, quelle + '/' + x + '/' + ordnerName)
