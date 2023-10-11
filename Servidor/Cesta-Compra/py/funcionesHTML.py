def pagPrincipal():
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

def pagCesta():
    print("""

""")
