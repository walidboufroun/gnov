#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Active l'utilisation de la sortie CGI
print("Content-type: text/html\n\n")

# Votre code Python ici
result = "Hello, world from Python!"

# Utilisez les balises de format pour inclure le résultat dans le HTML
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML + Python</title>
</head>
<body>
    <h1>Bienvenue sur ma page HTML + Python</h1>
    
    <p>Le résultat du script Python :</p>
    
    <script>
        // Affiche la sortie du script Python
        document.write('<p>' + 'Output: ' + '<strong>' + '{result}' + '</strong>' + '</p>');
    </script>
</body>
</html>
""")
