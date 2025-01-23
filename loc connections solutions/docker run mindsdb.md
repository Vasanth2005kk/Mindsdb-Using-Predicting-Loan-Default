# MindsDB Documentation

## MindsDB Docs
[Official MindsDB Documentation](https://docs.mindsdb.com/setup/self-hosted/docker)

## Install MindsDB

### If you want to persist your models and configurations in the host machine, run these commands:

```bash
$ mkdir mdb_data
$ docker run --name mindsdb_container -p 47334:47334 -v $(pwd)/mdb_data:/root/mdb_storage mindsdb/mindsdb:lightwood
```

## Verify Docker Container

```bash
$ docker ps
```

## Access the MindsDB Editor

You can now access the MindsDB editor by going to:

- [http://127.0.0.1:47334](http://127.0.0.1:47334)
- [http://<docker-ip>:47334](http://<docker-ip>:47334) (replace `<docker-ip>` with your Docker container's IP address)

## Use Host IP or host.docker.internal

When connecting from a Docker container, replace `localhost` with either:

1. Your host machine's IP address, or
2. `host.docker.internal`, which resolves to the host's IP in Docker.

## Example SQL Command

```sql
CREATE DATABASE mysql_integration
WITH ENGINE = "mysql",
    PARAMETERS = {
        "host": "<Your host machine's IP address>",
        "port": 3306,
        "user": "mindsdb",
        "password": "mindsdb",
        "database": "loan"
    };
```

## Option

### MindsDB HTTP API Stopped Time

If the error persists:

Run the container with an interactive shell to troubleshoot:
(No Issues Detected)

```bash
pip check
```

**Output:**

    No broken requirements found.
