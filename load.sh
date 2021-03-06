# The name of the dump file is received as a parameter
legacy_db_dump_filename=$1

# Calls to dbshell command are too verbose, lets rename them before start
legacy_db='python manage.py dbshell --database=legacy'
db='python manage.py dbshell'

# All legacy database (tpoodump) tables gets truncated
echo -n "Cleaning legacy database... "
echo 'show tables' | $legacy_db | tail --lines +2 | while read table;
do echo "truncate table $table" | $legacy_db;  done
echo -e "\e[32mOK\e[39m"

# Legacy database (tpoodump) gets filled with data from the dump file
echo -n "Filling legacy database with data... "
$legacy_db < $legacy_db_dump_filename
echo -e "\e[32mOK\e[39m"


# Get a list of all tables used in our migration script
echo -n "Cleaning most tables from the default database... "
tpoo_tables=$( \
    cat scripts_migracion.sql | grep "insert into" \
                              | grep -v "/\*" \
                              | cut -d " " -f 3 \
                              | cut -d "(" -f 1 \
)
# Each of those tables gets truncated (foreign key checks gets disabled temporally)
for table in $tpoo_tables; do
    echo "SET FOREIGN_KEY_CHECKS = 0; truncate table $table;" | $db;
done;
echo -e "\e[32mOK\e[39m"

# Our migration script is run, filling the default database (tpoo)
# with data from the legacy databse (tpoodump).
# Since no database is specified, dbshell command uses the default,
# just like out script which assumes that tpoo is the current db.
echo -n "Migration data from legacy database to the default one... "
$db < scripts_migracion.sql
echo -e "\e[32mOK\e[39m"
