import requests
from bs4 import BeautifulSoup
import csv
import re

def scrape_race_detail_result(uuid):
    url = "https://results.checkpointspot.asia/myresults.aspx?uid=" + uuid
    response = requests.get(url)
    detail = {'finish_time': '', 'net_time': '', 'start': '', 'u_turn_checkpoint': '', 'finish': '', 'country': ''}
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        results_table = soup.find('table', {'class': 'table-borderless'})
        if results_table:
            rows = results_table.find_all('tr')[2:]  # Skip the header row
            for row in rows:
                columns = row.find_all('td')
                if len(columns) == 2:
                    country = columns[1].text.strip()
                    detail['country'] = country

        return detail


def scrape_race_results():
    # Make a GET request to the URL
    data_list = []
    e_id = "3"  # Change Type Here
    from_page = 31
    min_page = 41

    for page in range(from_page, min_page):
        url = "https://results.checkpointspot.asia/results.aspx?CId=17036&RId=14036&EId=" + e_id + "&dt=0&PageNo=" + str(page)
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract race results (adjust these based on the actual structure of the website)
            results_table = soup.find('table', {'class': 'xtable-striped'})
            if results_table:
                rows = results_table.find_all('tr')[1:]  # Skip the header row

                for row in rows:
                    columns = row.find_all('td')
                    bib_no = columns[1].text.strip()
                    name = columns[3].text.strip()
                    time = ''
                    gender = columns[5].text.strip()
                    gen_pos = ''
                    country = ''

                    result_dict = {
                        'Bib Number': bib_no,
                        'Name': name,
                        'Time': time,
                        'Gender': gender,
                        'Gender Position': gen_pos,
                        'Country': country,
                        'Type': '5KM'
                    }

                    # Read uuid from a href
                    href_value = columns[4].find('a', {'class': 'ltw-name'})['href']
                    match = re.search(r'uid=([\d-]+)', href_value)
                    if match:
                        uuid = match.group(1)
                        detail = scrape_race_detail_result(uuid)
                        # result_dict['Finish Time'] = detail['finish_time']
                        # result_dict['Net Time'] = detail['net_time']
                        # result_dict['Start'] = detail['start']
                        # result_dict['U-Turn Checkpoint'] = detail['u_turn_checkpoint']
                        result_dict['country'] = detail['country']

                    data_list.append(result_dict)

                    # print(f"Bib No: {bib_no}")
                    # print(f"Name: {name}")
                    # print(f"Time: {time}")
                    # print(f"Gender: {gender}")
                    # print(f"Gen Pos: {gen_pos}")
                    # print(f"Country: {country}")
                    # print("----")

    # Export data to CSV
    # print(result_dict)
    csv_file = 'race_results_5km-[31-41].csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=result_dict.keys())

        # Write header
        writer.writeheader()

        # Write data
        writer.writerows(data_list)

    print(f"Race results exported to {csv_file}")



if __name__ == "__main__":
    scrape_race_results()


