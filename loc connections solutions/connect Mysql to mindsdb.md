# Connect MySQL to MindsDB Locally

```bash
$ sudo systemctl status mysql
```

## Create a MySQL User for MindsDB

```bash
$ mysql -u root -p
```

```sql
mysql > CREATE USER 'mindsdb'@'%' IDENTIFIED BY 'mindsdb';
mysql > GRANT ALL PRIVILEGES ON *.* TO 'mindsdb'@'%';
mysql > FLUSH PRIVILEGES;
```

## Test Connection to MySQL from Another Tool

```bash
$ mysql -u mindsdb -p -h 127.0.0.1 -P 3306
Enter Password: mindsdb
```

# Resolving MySQL Connection Error

The issue may occur because MySQL is only listening on `127.0.0.1:3306` (localhost), which makes it inaccessible from external IP addresses like `192.168.1.17`.

## Steps to Resolve the Issue

### 1. Update MySQL's Bind Address

MySQL might be configured to only listen on `127.0.0.1`. Update it to listen on all network interfaces or specifically on `192.168.1.17`.

Open the MySQL configuration file (`/etc/mysql/my.cnf` or `/etc/mysql/mysql.conf.d/mysqld.cnf`) using a text editor:

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

Look for the `bind-address` directive:

```ini
bind-address = 127.0.0.1
```

Change it to:

```ini
bind-address = 0.0.0.0
```

This allows MySQL to listen on all available network interfaces.

### 2. Restart MySQL

After making the change, restart the MySQL service to apply the new configuration:

```bash
sudo systemctl restart mysql
```

### 3. Verify MySQL is Listening on All Interfaces

After the restart, check if MySQL is listening on all interfaces, especially `192.168.1.17`:

```bash
netstat -tuln | grep 3306
```

You should see something like:

```
tcp        0      0 0.0.0.0:3306           0.0.0.0:*               LISTEN
```

### 4. Check Firewall Rules

If you're still facing issues, verify that your firewall isn't blocking external connections on port `3306`. If you're using `ufw`, run:

```bash
sudo ufw allow 3306
```

### 5. Retry the MySQL Connection

Now, try connecting to MySQL again from the remote machine or container:

```bash
mysql -u mindsdb -p -h 192.168.1.17 -P 3306
```

## Final Notes

- If you're using Docker or any other container-based setup, ensure that you're connecting to the correct network interface and port.
- If MySQL is running in Docker, the host IP (`192.168.1.17`) must be accessible from the Docker container.

