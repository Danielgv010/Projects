def pagina_principal():
    print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cesta Compra</title>
    <link rel="stylesheet" href="../css/style.css">
</head>

<body>
    <nav>
        <h1>TIENDA</h1>
        <a class="icon" href="verCestaCompra.py"><img class="icon-img" src="../img/carrito.png" alt="Carrito"></a>
    </nav>
    <section>
        <article>
            <div class="product">
                <img class="product-img" src="../img/teclado.png" alt="Teclado">
                <div class="controls">
                    <div class="add-control">
                        <a href="meterCesta.py?prod=1">ADD PRODUCT</a></div>
                </div>
            </div>
            <div class="product">
                <img class="product-img" src="../img/raton.png" alt="Raton">
                <div class="controls">
                    <div class="add-control">
                        <a href="meterCesta.py?prod=2">ADD PRODUCT</a></div>
                </div>

            </div>
            <div class="product">
                <img class="product-img" src="../img/monitor.png" alt="Monitor">
                <div class="controls">
                    <div class="add-control">
                        <a href="meterCesta.py?prod=3">ADD PRODUCT</a></div>
                </div>
            </div>
        </article>
    </section>
</body>

</html>
""")

def inicio_cesta_compra():
    print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cesta Compra</title>
    <link rel="stylesheet" href="../css/style.css">
</head>

<body>
    <nav>
        <h1>TIENDA</h1>
        <a class="icon" href="verCestaCompra.py"><img class="icon-img" src="../img/carrito.png" alt="Carrito"></a>
    </nav>
    <section>
        <article>
            <div class="product" style="display:block !important">
""")
    
def fin_cesta_compra():
    print("""
            </div>
        </article>
    </section>
</body>
</html>
""")
    
def formulario():
    print("""
<form action="productoNuevo.py" method="get">
    <label for="nombre">nombre del producto</label>
    <input type="text" name="producto">
    <button>Enviar</button>
</form>
""")