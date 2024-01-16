import requests
from bs4 import BeautifulSoup
import csv
import re

def scrape_race_detail_result(uuid):
    url = "https://results.checkpointspot.asia/myresults.aspx?uid=" + uuid
    response = requests.get(url)
    detail = {'finish_time': '', 'net_time': '', 'start': '', 'u_turn_checkpoint': '', 'finish': ''}
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract finish and net time from span
        detail['finish_time'] = soup.find('span', {'id': 'ctl00_Content_Main_lblTime1Large'}).text
        detail['net_time'] = soup.find('span', {'id': 'ctl00_Content_Main_lblTime2Large'}).text

        # Extract result from table
        results_table = soup.find('table', {'class': 'table-bordered'})
        if results_table:
            rows = results_table.find_all('tr')[1:]  # Skip the header row
            split = {'start': '', 'u_turn_checkpoint': '', 'finish': ''}
            for row in rows:
                columns = row.find_all('td')
                detail['start'] = columns[0].text.strip()
                detail['u_turn_checkpoint'] = columns[1].text.strip()
                detail['finish'] = columns[2].text.strip()

        return detail


def scrape_race_results():
    # Make a GET request to the URL
    data_list = []
    e_id = "2"  # Change Type Here
    min_page = 81

    for page in range(1, min_page):
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
                    bib_no = columns[2].text.strip()
                    name = columns[4].text.strip()
                    time = columns[6].text.strip()
                    gender = columns[8].text.strip()
                    gen_pos = columns[9].text.strip()
                    country = columns[10].text.strip()

                    type_race = "21KM"
                    if e_id == 2:
                        type_race = "10KM"
                    elif e_id == 3:
                        type_race = "5KM"
                    else:
                        type_race = "3KM"

                    result_dict = {
                        'Bib Number': bib_no,
                        'Name': name,
                        'Time': time,
                        'Gender': gender,
                        'Gender Position': gen_pos,
                        'Country': country,
                        'Type': type_race,
                        'Finish Time': '',
                        'Net Time': '',
                        'Start': '',
                        'U-Turn Checkpoint': '',
                        'Finish': ''
                    }

                    # Read uuid from a href
                    href_value = columns[4].find('a', {'class': 'ltw-name'})['href']
                    match = re.search(r'uid=([\d-]+)', href_value)
                    if match:
                        uuid = match.group(1)
                        detail = scrape_race_detail_result(uuid)
                        result_dict['Finish Time'] = detail['finish_time']
                        result_dict['Net Time'] = detail['net_time']
                        result_dict['Start'] = detail['start']
                        result_dict['U-Turn Checkpoint'] = detail['u_turn_checkpoint']
                        result_dict['Finish'] = detail['finish']

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
    csv_file = 'race_results_10km.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=result_dict.keys())

        # Write header
        writer.writeheader()

        # Write data
        writer.writerows(data_list)

    print(f"Race results exported to {csv_file}")



if __name__ == "__main__":
    scrape_race_results()


