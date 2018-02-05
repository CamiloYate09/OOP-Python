from Auto.clases import Auto


carrito = Auto("Rojo","Ferrari","1992", 4, 320)
#ENCAPSULAMIENTO DE ATRIBUTOS
carrito.setConductor("camilo Yalt")
carrito.caracteristicas()
carrito.aceleracion(180)
carrito.frenado(180,20)
carrito.detenido()

#ENCAPSULAMIENTO DE OTRA FORMA
print("Conductor", carrito.getConductor())
