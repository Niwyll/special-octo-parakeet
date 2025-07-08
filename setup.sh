#!/bin/bash
echo "Starting Auth Api (step 1) on port 8000"
(cd auth_api && ./setup.sh &)

echo "Starting Secure Pokedex (step 2) on port 8001"
(cd secure_pokedex && ./setup.sh &)