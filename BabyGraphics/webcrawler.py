"""
File: webcrawler.py
Name: Tina Tsai
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        rank_order = 0
        female_sum = 0
        male_sum = 0
        # ----- Write your code below this line ----- #
        rankings = soup.tbody.find_all('tr')
        for rank in rankings:
            # Locate to the td tags that contain name and num of new born
            name_num = rank.find_all('td')
            rank_order += 1
            # Avoid the td tags in the bottom that contains non raking data
            if rank_order <= 200:
                male_sum += int(name_num[2].text.replace(',',''))
                female_sum += int(name_num[4].text.replace(',',''))
        print(f"Male Number: {male_sum}")
        print(f"Female Number: {female_sum}")



if __name__ == '__main__':
    main()
