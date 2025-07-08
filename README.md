# Installation
## Step 1
Make sure you have python 3.12 or newer installed.
Create a virtual environment using

```bash
python -m venv venv
```

Then activate it:
- On Windows (git bash):
  ```bash
  source venv/Scripts/activate
  ```

  - On Linux:
  ```bash
  source venv/bin/activate
  ```

Once activated, install required packages:

```bash
pip install -r requirements.txt
```

## Step 2
Please use bash to run the following script

```bash
./setup.sh
```

This will migrate and populate database on step 1 API, run it on port 8000 and run step 2 API on port 8001 on local.
If not working , please inspect setup.sh in each project and run commands for each API on different terminals.

## Step 3

Once setup, you can consume the API using that Postman workspace:
https://app.getpostman.com/join-team?invite_code=bd1d0a40dbd53b274981b0599deb840991ab3b7b27ffbf81b50d9c302265e63b&target_code=73979b4767834a9aad34aef1dc906d24

# Developement notes
## Step 1
- Types are stocked in database to avoid redundant calls while setting groups.

## Step 2
- To connect to the step 2 API, simply use the access token in header the same way as in step 1 API, I've set the lifetime
to 10 years to avoid trouble while testing, as subject didn't require refresh token management.
  
- At first, I thought I should handle the multi-types restrictively
For example: For a fire - flying pokemon, if user is not in flying group, it should not have access to this pokemon.
But as types are not returned in list call on pokeapi.co, I figured I should only remove the duplicates when user
belongs to multiple groups , else I'd be forced eticher to spam the api with request to make sure each pokemon have the appropriate multi-types or to stock every pokemon in database, which seemed not very logical for this exercice.
So if an user belongs to group fire, he will see each multi type pokemons containing fire type, which is the permissive way
to handle this.
