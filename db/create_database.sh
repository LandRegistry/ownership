#!/bin/bash

createuser -s ownership
createdb -U ownership -O ownership ownership -T template0
