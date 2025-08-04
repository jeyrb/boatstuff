
from pathlib import Path

from numbers_parser import Document
from loguru import logger
from zipfile import ZipFile
import sqlite3
import os
import sys
from io import BytesIO

def sanitize_name(name):
    return "".join(c if c.isalnum() or c == "_" else "_" for c in name)

def convert(numbers_location):

    zip_buffer = BytesIO()
    with ZipFile(zip_buffer, 'w') as zip_file:

        try:
            doc = Document(numbers_location)
        except Exception as e:
            real_path=Path(numbers_location).resolve(strict=True)
            logger.error(f"Failed to open {real_path}: {e}")
            raise

        if not doc.sheets:
            logger.warning(f"No sheets found in {numbers_location}. Skipping.")
        else:
            for sheet in doc.sheets:
                sheet_name = sanitize_name(sheet.name)
                db_name = f"{sheet_name}.db"
  
                conn = sqlite3.connect(":memory:")
                cur = conn.cursor()
                for table in sheet.tables:
                
                    data = list(table.rows(values_only=True))
                    if not data:
                        continue
                    if len(sheet.tables)>1 or table.name != 'Table 1':
                        table_name = sanitize_name(table.name)
                    else:
                        table_name = sheet_name
                    headers = [sanitize_name(str(h)) for h in data[0]]
                    cur.execute(f"DROP TABLE IF EXISTS {table_name}")
                    columns = ", ".join(f'"{h}" TEXT' for h in headers)
                    cur.execute(f'CREATE TABLE "{table_name}" ({columns})')
                    for row in data[1:]:
                        placeholders = ", ".join("?" for _ in headers)
                        cur.execute(
                            f'INSERT INTO "{table_name}" VALUES ({placeholders})', row)
                    logger.info(f"Processed table: {table_name} in sheet: {sheet.name}")
                conn.commit()
                with zip_file.open(db_name,'w') as db_zip:
                    db_zip.write(conn.serialize())
                conn.close()
                logger.info(f"Converted {sheet.name} to {db_name} in zip")
    logger.info(f"Finished zip for : {numbers_location}")
    os.write(sys.stdout.fileno(),zip_buffer.getvalue())
   