```bash
brew install postgresql
```

add this line to .zshrc file
```bash
export PGDATA=$HOME/.brew/var/postgres
```

```bash
source ~/.zshrc
```

create directory for database system
```bash
mkdir $PGDATA
```

initialize database cluster
```bash
initdb ~/.brew/var
```

Start the server
```bash
pg_ctl start
```

Use `pg_ctl stop` to stop the server anytime

