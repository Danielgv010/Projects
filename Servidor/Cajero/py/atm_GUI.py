def pagina_principal():
    print("""
        <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>ATM</title>
                    <link rel="stylesheet" href="../css/style.css">
                    </link>
                </head>
                <body>
                    <div class="accounts">
                        <table>

                        </table>
                        <div class="account_control">
                            <form action="create_account.py" method="get">
                                <button type="button">Create Account</button>
                            </form>
                        </div>
                    </div>
                    <div class="operations">
                        <form action="atm.py" method="get"></form>
                            <div class="cols">
                                <div class="col2">
                                    <select class="inputs">

                                    </select>
                                    <input class="inputs" type="text" placeholder="Introduce cantidad en €">
                                </div>
                                <div class="col2">
                                    <p class="radios"><input type="radio" value="Deposit">Deposit</p>
                                    <p class="radios"><input type="radio" value="Withdraw">Withdraw</p>
                                </div>
                            </div>
                            <div class="cols">
                                <button type="button" class="button1">Operate</button>
                            </div>
                        </form>
                    </div>
                </body>
            </html>
        """)