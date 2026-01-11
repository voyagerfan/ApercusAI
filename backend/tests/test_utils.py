import pytest
import pathlib
from utils import validation

TEST_DIR = pathlib.Path(__file__).parent
FILE_DIR = TEST_DIR / "test-files"

class TestUtils:
    def test_xls_validation(self):
        path = FILE_DIR / "blank_xlsx.xlsx"
        result = validation.file_extension(path)
        assert result["extension"] == "xlsx"

    def test_csv_validation(self):
        path = FILE_DIR / "blank_csv.csv"
        result = validation.file_extension(path)
        assert result["extension"] == "csv"
    
    def test_xls_validation(self):
        path = FILE_DIR / "blank_xls.xls"
        result = validation.file_extension(path)
        assert result["extension"] == "xls"

    def test_invalid_file_type_docx(self):
        path = FILE_DIR / "blank_doc.docx"
        result = validation.file_extension(path)
        assert result["extension"] == None
    
    def test_invalid_file_type_pdf(self):
        path = FILE_DIR / "blank_pdf.pdf"
        result = validation.file_extension(path)
        assert result["extension"] == None