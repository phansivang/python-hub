import locale
import datetime
def format_currency_usd(value):
    # Set locale to en_US
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    # Convert value to a string with appropriate formatting
    formatted_value = locale.currency(value, grouping=True)

    # Return the formatted value
    return formatted_value


def format_currency_kh(value):
    # Convert value to a string and split into integer and decimal parts
    str_value = str(round(value, 2))  # Round to 2 decimal places to handle precision errors

    if '.' in str_value:
        int_part, dec_part = str_value.split('.')
    else:
        int_part = str_value
        dec_part = ""

    # Add commas to the integer part
    int_part = add_commas(int_part)

    # Combine integer and decimal parts with a dot
    formatted_value = int_part + ('.' + dec_part if dec_part else '')

    # Add KHR symbol (៛) to the beginning
    formatted_value = '៛' + formatted_value

    # Return the formatted value
    return formatted_value


# Generate invoice with template INV-20230001
def generate_bill_no_by_year():
    inv_head = 'INV-'
    current_year = datetime.date.today().year
    current_inv_no = 'INV-202300001'
    next_invoice_int = int(current_inv_no[8:]) + 1
    return f'{inv_head}{current_year}{str(next_invoice_int).zfill(5)}'


def generate_invoice_no_1():
    inv_head = 'INV-'
    current_inv_no = 'INV-00001'
    current_inv_int = int(current_inv_no.replace(current_inv_no[:4], ''))
    next_inv_int = current_inv_int + 1
    # return inv_head + str(next_inv_int).zfill(5)
    return f'{inv_head}-{str(next_inv_int).zfill(5)}'


def generate_invoice_no_2():
    current_inv_no = 'INV-00001'
    next_inv_int = int(current_inv_no[4:]) + 1
    return f'INV-{str(next_inv_int).zfill(5)}'


def add_commas(value):
    # Add commas to the integer part of the value
    n = len(value)
    if n <= 3:
        return value
    else:
        return add_commas(value[:-3]) + ',' + value[-3:]


