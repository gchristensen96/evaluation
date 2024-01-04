#merge temp_table into existing table
def merge_dummy(table_name):
    return f"""
     INSERT OR REPLACE INTO {table_name}
     SELECT * FROM {table_name}_temp;

    """

#drop table, typically temp_table
def drop_temp(table_name):
    return f"""
    DROP TABLE IF EXISTS {table_name};
    """

#create cities table, everything not null, added id column as primary key
def create_cities_table():
    return """
    CREATE TABLE IF NOT EXISTS cities (
        id INT NOT NULL,
        LatD INT NOT NULL,
        LatM INT NOT NULL,
        LatS INT NOT NULL,
        NS TEXT NOT NULL,
        LonD INT NOT NULL,
        LonM INT NOT NULL,
        LonS INT NOT NULL,
        EW TEXT NOT NULL,
        City TEXT NOT NULL,
        State TEXT NOT NULL,
        CONSTRAINT cities_pk PRIMARY KEY (id)

    );
    """

#create .csv report of product id, title, price, and image count.
def create_csv_export():
    return """
    SELECT
    prod.id,
    prod.title,
    prod.price,
    COUNT(product_id) AS image_count


    FROM
    product prod
    JOIN
    product_image image ON prod.id = image.product_id
    GROUP BY 
    prod.id, prod.title, prod.price;
    """
