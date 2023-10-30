def info_page(type,message,redirect):
    print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="2;"""+redirect+""">
    <title>Document</title>
</head>
<body>
    <div class="wrapper">
        <h1 class="""+type+""">"""+type.upper()+"""</h1>
        <h2 class="""+type+""">"""+message+"""</h2>
    </div>
</body>
</html>
""")
