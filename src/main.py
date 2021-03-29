class source():
    def __init__(self, item):
        self.item = item

    def add(self, item):
        self.item = item
        return str(item)

class sourceList():
    def __init__(self, source):
        self.source = source

'''
- Rechnung einragen
- Rechnung kann alleine stehen (Name<o2>, Preis<40>, Datum<1.April.21>)
## Date Time Module oder os Module?
- Rechnung kann mehrteilig sein (Name<Einkauf>, Inhalte<Tomaten, Gurken, Beeren>, Preis<3>, Datum<1.April.21>)
- Alle Rechnungen innerhalb von Monat aufaddieren und Gesamtrechnung ausgeben
- Kategorien erstellen (Standard<Einkauf, Strom, Miete>, custom auch einstellbar)
- Möglichkeit Kategorien hinzuzufügen
- Rechnungen + Anteile im Kuchendiagramm anzeigen
## Matplotlib Module
- Möglichkeit zu schauen, wie oft was gekauft wird <zB Tomaten>
- Möglichkeit, Einnahmen hinzuzufügen
- Excel-Tabelle nur visueller Darstellen
- Möglichkeit, bestimmte Kategorien ein- und auszublenden
'''

'''
git remote add origin https://github.com/fruitiestPunch/eZfin.git
git branch -M main
git push -u origin main
'''