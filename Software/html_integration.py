import webbrowser

with open("test.html", "w") as fileout: 
    htmlCode = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Python Webpage</title>
        </head>
        <body>
            
            <h1>Square Numbers</h1>
            <table>
                <tr border=1>
                    <th>Number</th>
                    <th>Square</th>
            </table>
    """

    fileout.write(htmlCode)

for index in range(1,26):
    with open("test.html", "a") as fileout:
        htmlCode = """
            <tr><td> %s </td> <td> %s </td></tr>
        """ % (str(index), str(index**2))

        fileout.write(htmlCode)

with open("test.html", "a") as fileout: 
    htmlCode = """
        </table>
        </body>
        </html>
    """

    fileout.write(htmlCode)

webbrowser.open("test.html")