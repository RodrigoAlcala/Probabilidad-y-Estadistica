import statistics
import matplotlib
from matplotlib import pyplot
import numpy



data = [3,7,4,4,5,5,5,4,6,7,4,5,4,4,6,4,7,8,5,3,4,3,10,4,6,3,4,3,3,4]


def basicStatistics(dataList):

	deviation = statistics.stdev(dataList)
	varianza = deviation ** 2
	mean = statistics.mean(dataList)
	variation = (deviation/mean)
	median = statistics.median(dataList)
	multimodes = statistics.multimode(dataList)
	print("En base a {}\nEl coeficiente de variacicion es: {} \nLa desviacón estándar es: {} \nLa media es: {}\nLa mediana es {}\nLas modas son: {}\nLa varianza es {}".format(dataList, variation ,deviation, mean, median, multimodes,varianza))

def numpyStats(dataList):
	mediana = numpy.median(dataList)
	promedio = numpy.average(dataList)
	media = numpy.mean(dataList)
	desviación = numpy.std(dataList)
	varianza = numpy.var(dataList)
	cuartil1 = numpy.quantile(dataList,0)
	cuartil2 = numpy.quantile(dataList,0.25)
	cuartil3 = numpy.quantile(dataList,0.50)
	cuartil4 = numpy.quantile(dataList,0.75)
	cuartil5 = numpy.quantile(dataList,1)
	print("Mediana: {}\nPromedio: {}\nMedia: {}\nDesviación: {}\nVarianza: {}\nPrimer Cuartil: {}\nSegundo Cuartil: {}\nTercer Cuartil: {}\nCuarto Cuartil: {}\nQuinto Cuartil: {}".format(mediana,promedio,media,desviación,varianza,cuartil1,cuartil2,cuartil3,cuartil4,cuartil5))

numpyStats(data)

def generateGraphs(dataList):
	generatePlot(dataList) 
	generateHistogram(dataList)
	generatePolygon(dataList)



def generateHistogram(dataList):
	pyplot.hist(dataList, color = "g", bins = "auto")
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
generateGraphs(data)


