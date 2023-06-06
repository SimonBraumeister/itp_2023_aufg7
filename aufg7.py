import csv
import subplot

# Dateinamen erfragen und die in der Datei enthaltenen Daten einlesen
# in while-Schleife mit Fehlerabfangen
while True: 
    dateiname = input("CSV Dateiname: ")
                      
    if dateiname == "graph.csv":
        break
    else:
        print("Datei wurde nicht gefunden. Bitter erneut einen Dateinamen eingeben.\n")

# Variablen anlegen
value_x = []
value_y = []

# Datei öffnen und Werte auslesen und in Listen schreiben
with open("graph.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        value_x.append(float(row[0]))
        value_y.append(float(row[1]))

# Nach Skalierungsfaktor fragen 
# Fehler abfangen, wenn string o.ä. eingegeben wird
# dann erneut fragen
while True:
    skal_fakt = input("Skalierungsfaktor: ")
    
    try:
        float(skal_fakt)
        break
    except ValueError:        
        print("Der Skalierungsfaktor muss vom Typ Float sein.\n")
        
#
# damit y-Wert skalieren
value_y = [wert * float(skal_fakt) for wert in value_y]

# nach Start Prozent und End Prozent fragen
# Exceptions abfangen
while True:
    start_prozent = input("Start Prozent: ")    
   
    try:
        float(start_prozent)
        break
    except ValueError:
        print("Es werden Floats als Eingabe erwartet.\n")
        
    if start_prozent < 100.0 and start_prozent > 0.0:
        break
    else:
        print("Gebe einen Wert zwischen 0 und 100 ein.")
        
while True:
    end_prozent = input("End Prozent: ")

    try:
        float(end_prozent)
        break
    except ValueError:
        print("Es werden Floats als Eingabe erwartet.\n")
        
    if end_prozent < 100.0 and start_prozent > 0.0:
        break
    else:
        print("Gebe einen Wert zwischen 0 und 100 ein.")

start = float(start_prozent) / 100 * max(value_x)
end = float(end_prozent) / 100 * max(value_x)

# Teil des Graphen, welcher innerhalb der soeben definierten Grenzen liegt, geplottet 
# und als PDF ausgegeben werden. 
# 
subplot.create_subplot(value_x, value_y, start, end)
