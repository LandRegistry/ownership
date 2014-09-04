#!/bin/bash

echo "Creating database for casework-frontend"

createuser -s ownership
createdb -U ownership -O ownership ownership -T template0
