#!/usr/bin/env bash

### Genrate CSV and JSON
echo -e "\n\n\nGenrating CSV and JSON for all programs present ..."
./gen.py

### Cleanup
echo -e "\n\n\nCleaning up old files ..."
rm -rf ./assets/ ./icon.svg ./node_modules/

### Append HTML
echo -e "\n\n\nAppending HTML ..."
echo '<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <!-- Site Icon -->
        <link rel="icon" type="image/svg+xml" href="/icon.svg" />

        <!-- Bootstrap CSS -->
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
            crossorigin="anonymous"
        />

        <!-- Title -->
        <title>SDE Sheet</title>
    </head>

    <body>
        <div id="root"></div>
        <script type="module" src="/src/main.tsx"></script>

        <!-- Bootstrap JS -->
        <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
            crossorigin="anonymous"
        ></script>
    </body>
</html>' >index.html

### Install node dependencies
echo -e "\n\n\nInstalling node dependencies ..."
npm install

### Build production ready app
echo -e "\n\n\nBuilding the app ..."
npm run build

### Copying Files
cp -r ./dist/* .
rm -rf dist
sed -i 's/\/assets/\.\/assets/g' index.html
sed -i 's/\/icon/\.\/icon/g' index.html
