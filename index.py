<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Page with PyScript</title>
    <script src="https://cdn.jsdelivr.net/npm/pyscript"></script>
</head>
<body>
    <h1>Hello World - SITE GNOV - </h1>
    <div id="output"></div>

    <script pyscript>
        def say_hello():
            print("Hello, world!")
            document.getElementById("output").innerHTML = "Python said: Hello, world!"

        say_hello()
    </script>

    <h2>Test site :  <script pyscript> print("Hey i'm code python") </script> </h2>
</body>
</html>

