from help import *
from attendance import *

print("Grand Total:", format_currency_usd(1200))
print("Grand Total:", format_currency_kh(1200000))
print("Invoice No.:", generate_invoice_no_2())
print("Bill No.:", generate_bill_no_by_year())
print("Attendance:", get_diff_in_two_hours('12:00', '18:00'))
