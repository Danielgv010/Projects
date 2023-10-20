def home_page_start():
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
                        <div class="table-div">
                            <table border="1">
                                <tr>
                                    <th>ID</th>
                                    <th>Account Code</th>
                                    <th>Balance</th>
                                    <th>Actions</th>
                                </tr>
        """)

def home_page_middle():
    print("""
                            </table>
                        </div>
                        <div class="account_control">
                            <form action="create_account.py" method="get">
                                <button type="submit">Create Account</button>
                            </form>
                        </div>
                    </div>
                    <div class="operations">
                        <form action="operate.py" method="get">
                            <div class="cols">
                                <div class="col2">
                                    <select class="inputs" name="account">
        """)

def home_page_end():
    print("""
                                    </select>
                                    <input class="inputs" type="text" name="quantity" value="0.0" placeholder="Write a number in euro">
                                </div>
                                <div class="col2">
                                    <p class="radios"><input type="radio" name="operation" value="deposit" checked>Deposit</p>
                                    <p class="radios"><input type="radio" name="operation" value="withdraw">Withdraw</p>
                                </div>
                            </div>
                            <div class="cols">
                                <button type="submit" class="button1">Operate</button>
                            </div>
                        </form>
                    </div>
                </body>
            </html>
""")

def operation_done():
    print("""
<!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="refresh" content="2;atm.py">
                    <title>ATM</title>
                    <link rel="stylesheet" href="../css/style.css">
                    </link>
                </head>
                <body>
                    <div class="accounts">
                        <h1>Operation done succesfully!</h1>
                    </div>
                </body>
            </html>
""")
    
def operation_not_done():
    print("""
<!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="refresh" content="2;atm.py">
                    <title>ATM</title>
                    <link rel="stylesheet" href="../css/style.css">
                    </link>
                </head>
                <body>
                    <div class="accounts">
                        <h1>Operation not completed</h1>
                        <h2>Check your balance and the one you want to withdraw and try again</h2>
                    </div>
                </body>
            </html>
""")

def check_account_page():
    pass