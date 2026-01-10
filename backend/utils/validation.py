"""
Docstring for backend.utlis.validation

This file is a collection of validation methods for inputs and/or outputs
"""

import filetype
import csv

def csv_helper(path: str) -> dict:
    try:
        with open(path, newline="") as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            return {"extension" : "csv", "msg": "valid CSV"}
    except UnicodeDecodeError as e:
        return {"extension" : None, "msg": "invalid CSV - UniCodeDecodeError"} 
    except csv.Error:
        return {"extension" : None, "msg": "invalid CSV - CSV error"}
    except FileNotFoundError:
        return {"extension" : None, "msg": "file does not exist"} 

def file_extension(path: str) -> dict:
    result = {"extension" : "", "msg": ""}
    kind = filetype.guess_extension(path)

    match kind:
        case "xlsx":
            result["extension"] = "xlsx"
            result["msg"] = "valid extension"
        case "xls":
            result["extension"] = "xls"
            result["msg"] = "valid extension"
        case _:
            result = csv_helper(path)
    return result
            


    