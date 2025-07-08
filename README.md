# Installation

## Step 1

Make sure you have **Python 3.12 or newer** installed.
Create a virtual environment using:

```bash
python -m venv venv
```

Then activate it:

* **On Windows (Git Bash):**

  ```bash
  source venv/Scripts/activate
  ```

* **On Linux:**

  ```bash
  source venv/bin/activate
  ```

Once activated, install required packages:

```bash
pip install -r requirements.txt
```

---

## Step 2

Please use **bash** to run the following script:

```bash
./setup.sh
```

This will:

* Migrate and populate the database on the Step 1 API,
* Create a test user,
* Run Step 1 API on port **8000** locally,
* Run Step 2 API on port **8001** locally.

If this doesn’t work, please inspect the `setup.sh` script in each project folder and run the commands for each API in separate terminals.

---

## Step 3

Once setup, you can consume the API using this Postman workspace:
[Join Postman Team](https://app.getpostman.com/join-team?invite_code=bd1d0a40dbd53b274981b0599deb840991ab3b7b27ffbf81b50d9c302265e63b&target_code=73979b4767834a9aad34aef1dc906d24)

If you ran `setup.sh` correctly, you should have a test user with the following credentials:

* **username:** `testuser`
* **password:** `foobar123;`

---

# Development Notes

Names for apps and project could be inconsistant due to a missunderstanding of specifications until step 2.

## Step 1

* Pokemon types are stored in the database to avoid redundant API calls while managing groups.

## Step 2

* To connect to the Step 2 API, simply use the access token in the header, same as Step 1 API.
* The token lifetime is set to **10 years** to simplify testing, as refresh token management was not required by the subject.
* Initially, I considered a **restrictive multi-type access** policy (e.g., a Fire-Flying Pokemon would require user to be in both Fire and Flying groups).
* However, since the PokeAPI’s Pokemon list endpoint does not return types directly, handling this restrictively would require:

  * Excessive API calls per Pokemon to verify types, or
  * Storing every Pokemon locally in a database, which seemed overkill for this exercise.
* Therefore, I chose a **permissive approach**:

  * If a user belongs to the Fire group, they will see all Pokemon having Fire as **at least one** of their types.
  * Avoid duplicate Pokemon in results when a user belongs to multiple groups.
  * This approach simplifies the implementation and still respects the exercise requirements.
