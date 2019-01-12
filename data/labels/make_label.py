import os

l = ["stopsign", "yeildsign"]

for word in l:
    os.system("convert -fill black -background white -bordercolor white -border 4 -font arial -pointsize 18 label:\"%s\" \"%s.png\""%(word, word))