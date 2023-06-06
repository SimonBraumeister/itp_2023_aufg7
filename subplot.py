import matplotlib.pyplot as plt
# Modul Subplot
#
# Das Modul soll die Funktion create_subplot() anbieten, 
# welche als ersten Parameter die x-Werte, 
# als zweiten Parameter die y-Werte, 
# als dritten Parameter Start Prozent 
# und als vierten Parameter End Prozent akzeptiert.
 


def create_subplot(x, y, start, end):
    plt.plot(x, y, label="Graph 1")
 
# Es sollen ein passender Titel sowie passende Achsenbeschriftungen gew¨ahlt werden. 
# Die Verwendung einer Legende ist freiwillig. 
    plt.xlabel("Beschriftung der x-Achse")
    plt.ylabel("Beschriftung der y-Achse")
    plt.title("Titel des Graphen")
    plt.legend()
    plt.xlim(start, end)
    
# Der generierte Plot soll als plot.pdf gespeichert werden und zus¨atzlich im Plots-Reiter in Spyder angezeigt werden.    
    plt.savefig("plot.pdf", format="pdf")
    plt.show()