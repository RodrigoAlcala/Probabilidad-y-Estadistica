import statistics
import matplotlib
from matplotlib import pyplot
import numpy



data = [4,8,4,6,8,6,7,7,7,8,10,9,7,6,10,8,5,9,6,3,7,6,4,7,6,9,7,4,7,6,8,8,9,11,8,7,10,8,5,7,7,6,5,10,8,9,7,5,6,5]


def basicStatistics(dataList):

	deviation = statistics.stdev(dataList)
	varianza = deviation ** 2
	mean = statistics.mean(dataList)
	variation = (deviation/mean)
	median = statistics.median(dataList)
	multimodes = statistics.multimode(dataList)

	

	print("En base a {}\nEl coeficiente de variacicion es: {} \nLa desviacón estándar es: {} \nLa media es: {}\nLa mediana es {}\nLas modas son: {}\nLa varianza es {}".format(dataList, variation ,deviation, mean, median, multimodes,varianza))

	#generatePlot(dataList) 
	generateHistogram(dataList)
	generatePolygon(dataList)



def generateHistogram(dataList):
	pyplot.hist(dataList, color = "g", bins = "sturges")
	pyplot.grid(color = "black", lw = "0.5", axis = "x")
	pyplot.title("Histograma")
	pyplot.xlabel("Pesos")
	pyplot.ylabel("Frecuencias")
	pyplot.show()


def generatePlot(dataList):
	pyplot.plot(dataList, color = "r")
	pyplot.title("")
	pyplot.xlabel("")
	pyplot.ylabel("")
	pyplot.show()


def generateBar(dataList):
	pyplot.bar(dataList, color = "g", height = 10)
	pyplot.title("")
	pyplot.xlabel("")
	pyplot.ylabel("")
	pyplot.show()

def generatePolygon(dataList):
	pyplot.hist(dataList, cumulative = True, bins = "sturges", density= 1, histtype="step")
	pyplot.title("Histograma")
	pyplot.xlabel("Pesos")
	pyplot.ylabel("Frecuencias")
	pyplot.show()


basicStatistics(data)
