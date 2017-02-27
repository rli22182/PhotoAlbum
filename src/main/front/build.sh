#!/usr/bin/env bash
ng build -prod
rm -r ../resources/static
mkdir ../resources/static/
cp dist/* ../resources/static/
git add ../resources/static/