import argparse
import re
from loguru import logger
import sqlite3
from pathlib import Path
from numbers_parser import Document  # type: ignore


def sanitize_name(name):
    return "".join(c if c.isalnum() or c == "_" else "_" for c in name)


def bulk_convert(src_path: Path, dest_path: Path, force=False) -> int:
    logger.info(
        "Starting conversion of Apple Numbers workbooks to SQLite databases.")

    logger.info(
        f"Converting .numbers files from {src_path} to SQLite databases in {dest_path}")
    dest_path.mkdir(parents=True, exist_ok=True)
    db_build_count = 0

    for workbook_path in src_path.rglob('**/*.numbers'):
        logger.info(f"Processing workbook: {workbook_path}")
        workbook_prefixes = workbook_path.parts[len(src_path.parts):-1]
        doc = Document(workbook_path)
        if not doc.sheets:
            logger.warning(f"No sheets found in {workbook_path}. Skipping.")
            continue

        for sheet in doc.sheets:
            dest_sub_path = Path(dest_path, *workbook_prefixes,
                                 workbook_path.parts[-1].replace(".numbers", ""))
            dest_db = Path(
                dest_sub_path, f"{sanitize_name(sheet.name)}.sqlite")
            if dest_db.exists() and not force:
                logger.info(f"Database {dest_db} already exists. Skipping.")
                continue
            dest_sub_path.mkdir(parents=True, exist_ok=True)

            conn = sqlite3.connect(dest_db)
            cur = conn.cursor()
            for table in sheet.tables:
                table_name = sanitize_name(f"{sheet.name}")
                data = list(table.rows(values_only=True))
                if not data:
                    continue
                headers = [sanitize_name(str(h)) for h in data[0]]
                cur.execute(f"DROP TABLE IF EXISTS {table_name}")
                columns = ", ".join(f'"{h}" TEXT' for h in headers)
                cur.execute(f'CREATE TABLE "{table_name}" ({columns})')
                for row in data[1:]:
                    placeholders = ", ".join("?" for _ in headers)
                    cur.execute(
                        f'INSERT INTO "{table_name}" VALUES ({placeholders})', row)
            conn.commit()
            conn.close()
            db_build_count += 1
            logger.info(f"SQLite database created at {dest_db}")

    logger.info(
        f"Conversion completed successfully. {db_build_count} databases created.")
    return db_build_count


parser = argparse.ArgumentParser(
    description="Bulk convert Apple Numbers workbook to SQLite tables."
)
parser.add_argument(
    "phase", help="mkdocs phase", default="build"
)
parser.add_argument(
    "--src_path", help="Path to the .numbers directory", default="src/data")
parser.add_argument(
    "--dest_path", help="Path to the output directory for SQLite files", default="data")
parser.add_argument("--force", action="store_true",
                    help="Force conversion even if the destination already exists")
args = parser.parse_args()

try:
    src_path = Path(args.src_path)
    dest_path = Path(args.dest_path)

    bulk_convert(src_path, dest_path, force=args.force)

except Exception as e:
    logger.error(f"Conversion failed with error: {e}")
    exit(1)
