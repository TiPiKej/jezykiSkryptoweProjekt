import re

confirm_query = "^[Tt1Yy]|[Tt][Aa][Kk]$"
reg_file_name_json = "^.+\\.json$"
reg_file_name_xlsx = "^.+\\.xlsx$"
confirm_reg = re.compile(confirm_query)
