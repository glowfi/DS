#!/usr/bin/env bash

### Genrate CSV and JSON
echo -e "\n\n\nGenrating CSV and JSON for all programs present ..."
./gen.py

### Install node dependencies
echo -e "\n\n\nInstalling node dependencies ..."
npm install

### Build production ready app
echo -e "\n\n\nBuilding the app ..."
npm run build
