import os

from db_tools import MetaExporter


def test_meta_exporter(db_url):
    meta_exporter = MetaExporter(db_url)
    meta_exporter.export("db_structure.xlsx")
    assert os.path.exists("db_structure.xlsx")
