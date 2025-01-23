# Install and Run MindsDB (Local)

```bash
$ pip install mindsdb
$ pip install --upgrade mindsdb

$ python3 -m mindsdb
```

### Address Already in Use (Optional Step)

If you encounter an "address already in use" chacking command:

```bash
$ sudo lsof -i :47334
```

## Connect MySQL from MindsDB (GUI)

Use the MindsDB SQL interface or API to establish a connection to your local MySQL instance.

### Using MindsDB SQL API

URL: [http://127.0.0.1:47334](http://127.0.0.1:47334)

Log in to the MindsDB interface (e.g., through a GUI or the command-line interface) and execute the following SQL command:

```sql
CREATE DATABASE mindsdb_mysql
WITH ENGINE = "mysql",
PARAMETERS = {
    "user": "mindsdb",
    "password": "mindsdb",
    "host": "localhost",
    "port": 3306,
    "database": "loan"
};
