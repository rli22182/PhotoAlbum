#!/usr/bin/env bash
ng build -prod
rm -r ../resources/static/*
cp dist/* ../resources/static/