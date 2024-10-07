# Riddles Database
import time, random

riddle_list = [
    ["Ich bin nicht am Leben, aber ich wachse. Ich habe keine Lungen, aber ich brauche Luft. Was bin ich?", "Feuer", "Du siehst auf einer Wand einen brennenden Wald auf einem Gemälde."],
    ["Zwei Väter und zwei Söhne gingen angeln. Jeder von ihnen fing einen Fisch, aber am Ende waren nur drei Fische im Korb. Wie ist das möglich?", "Ein Großvater, ein Sohn und ein Enkel", "Auf einem Gemälde an einer Wand erblickst du eine Familie, bestehend aus Männern. Einen Grauhaarigen Mann links, einen großen Braunhaarigen rechts und vor ihnen beiden steht ein Kind."],
    ["Du bist mein Sohn, aber ich bin nicht dein Vater. Wer hat das gesagt?", "Mutter", "Du erblickst eine Statue einer Frau wie sie ein Bündel eines Babys im Arm hält."],
    ["Atemlos lebt es, kalt wie der Tod schwebt es. Kenn keinen Durst, dennoch trinkt es. Trägt ein Kettenhemd, doch nie klingt es.", "Fisch", "Auf dem Boden siehst du einen eine riesige Zeichnung eines Meeres und allerhand Lebewesen schwimmen darin."],
    ["Schreit ohne Stimme, fliegt ohne Schwinge. Beißt ohne Zahn, murmelt und pfeift, kein Mund hats getan.", "Wind", "Du merkst, dass das Gemäuer um dich undicht ist. Es zieht ganz schön."],
    ["Man kann es nicht sehen, kanns nicht aufstöbern. Kann es nicht fressen und kanns auch nicht hören. Es liegt hinter den Sternen und unterm Gestein. Rieselt in alle Höhlen hinein. Kommt zuerst und folgt auch zuletzt. Löscht alles Leben, bis keiner mehr schwätzt.", "Dunkel", "Es ist finsterste Nacht und du empfindest es als ganz schön düster."],
    ["Etwas, das alles und jeden verschlingt: Baum, der rauscht, Vogel der singt, frisst Eisen, zermalmt den härtesten Stein. Zerbeißt jedes Schwert und zerbricht jeden Schrein. Schlägt Könige nieder, schleift ihren Palast. Trägt manchen Fels fort, als leichte Last.", "Zeit", "Du hast das Gefühl schon eine Ewigkeit hier zu sein."],
    ["Der Schrein ohne Deckel, Schlüssel, Scharnier. Birgt einen goldenen Schatz, glaub es mir.", "Ei", "Du hörst das Gackern einer Henne in der Ferne."],
    ["Was hat Wurzeln, die keiner sieht, ragt höher als Bäume und Wipfelsäume, wächst nie und treibt nicht und reicht doch ins Licht?", "Berge", "Du siehst aus einem Fenster und erblickst ein Gebirge."],
    ["32 Schimmel auf einem roten Hang. Erst Malmen sie, dann stampfen sie und warten wieder lang.", "Zähne", "Du siehst in einen Spiegel und beginnst zu Lächeln."],
    ["Einige Monate haben 30 Tage, andere auch 31. Wie viele Monate haben 28 Tage?", "Alle", "Schau mal auf einen Kalender."],
    ["Kannst du drei aufeinander folgende Tage nennen, ohne die Wörter Mittwoch, Freitag oder Sonntag zu benutzen?", "Gestern, Heute und Morgen", "Ich war gestern Zuhause."],
    ["Welcher Tag ist Morgen, wenn vorgestern der Tag nach dem Sonntag war?", "Donnerstag", "Der Tag Vorgestern nach Sonntag war Montag."],
    ["Du nimmst an einem Rennen Teil. Du überholst den 3. Platzierten. An welche Stelle bist du nun?", "Dritter", "Vor dir sind noch zwei weitere Rennteilnehmer."],
    ["Beim ersten Mal kosten wir dir kein Geld. Beim zweiten Mal sind wir immer noch kostenlos. Aber beim dritten Mal werden wir richtig teuer. Wer sind wir?", "Zähne", "Du benutzt sie täglich."],
    ["Ein Mann hat sechs Söhne und jeder Sohn hat eine Schwester. Wie viele Kinder hat der Mann?", "Sieben Kinder", "Guckst du dich um, wo du gerade bist, entdeckst du 6 Männer Statuen aber nur 1 Frauen Statue."]
]

# hint_list = [
#     "Du siehst auf einer Wand einen brennenden Wald auf einem Gemälde.",
#     "Auf einem Gemälde an einer Wand erblickst du eine Familie, bestehend aus Männern. Einen Grauhaarigen Mann links, einen großen Braunhaarigen rechts und ihnen beiden steht ein Kind.",
#     "Du erblickst eine Statue einer Frau wie sie ein Bündel eines Babys im Arm hält."
# ]