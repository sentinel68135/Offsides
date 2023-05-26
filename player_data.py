import pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup


class PlayerStatsScraper:
    def __init__(self, url):
        self.url = url

    def scrape_player_stats(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        #scraping standard table
        tables = soup.find_all('table', {'id': 'stats_standard_9'})

        for table in tables:
            headers = []

            for th in table.find('thead').find_all('th'):
                headers.append(th.text.strip())

            if 'Player' in headers:
                index = headers.index('Player')
                headers = headers[index:-1]

            rows = []
            for tr in table.find('tbody').find_all('tr'):
                row = []

                for th in tr.find_all('th'):
                    row.append(th.text.strip())

                    for td in tr.find_all('td')[:-1]:
                        row.append(td.text.strip())
                rows.append(row)
        standard = pd.DataFrame(data=rows, columns=headers)

        #scraping for passing table
        passings = soup.find_all('table', {'id':'stats_passing_9'})

        for passing in passings:
            headers1 = []
            for th in passing.find('thead').find_all('th'):
                headers1.append(th.text.strip())

            cmp = 'Cmp'
            if cmp in headers1:
                index = headers1.index(cmp)
                headers1 = headers1[index:-1]
            rows = []
            for tr in passing.find('tbody').find_all('tr'):
                row = []

                for td in tr.find_all('td')[4:-1]:
                    row.append(td.text.strip())

                rows.append(row)

        pass_ing = pd.DataFrame(data=rows, columns=headers1)

        #scraping for passing type table
        pass_types = soup.find_all('table', {'id': 'stats_passing_types_9'})

        for pass_type in pass_types:
            headers3 = []

            for th in pass_type.find('thead').find_all('th')[11:-1]:
                headers3.append(th.text.strip())
            cmp = 'Live'
            if cmp in headers1:
                index = headers3.index(cmp)
                headers3 = headers3[index:-1]
            rows = []
            for tr in pass_type.find('tbody').find_all('tr'):
                row = []

                for td in tr.find_all('td')[5:-1]:
                    row.append(td.text.strip())

                rows.append(row)

        lv_pass_types = pd.DataFrame(data=rows, columns=headers3)

        #shooting table
        shootings = soup.find_all('table', {'id': 'stats_shooting_9'})

        for shooting in shootings:
            headers2 = []

            for th in shooting.find('thead').find_all('th'):
                headers2.append(th.text.strip())
            cmp = 'Gls'
            if cmp in headers2:
                index = headers2.index(cmp)
                headers2 = headers2[index:-1]

            rows = []
            for tr in shooting.find('tbody').find_all('tr'):
                row = []

                for td in tr.find_all('td')[4:-1]:
                    row.append(td.text.strip())

                rows.append(row)

        shoot_ing = pd.DataFrame(data=rows, columns=headers2)

        #playing time table
        playings = soup.find_all('table', {'id': 'stats_playing_time_9'})

        for play in playings:
            headers5 = []

            for th in play.find('thead').find_all('th'):
                headers5.append(th.text.strip())

            cmp = 'MP'
            if cmp in headers5:
                index = headers5.index(cmp)
                headers5 = headers5[index:-1]

            rows = []

            for tr in play.find('tbody').find_all('tr'):
                row = []

                for td in tr.find_all('td')[3:-1]:
                    row.append(td.text.strip())

                rows.append(row)

        lv_play = pd.DataFrame(data=rows, columns=headers5)

        #defense table
        defenses = soup.find_all('table', {'id': 'stats_defense_9'})
        headers6 = []
        for defense in defenses:
            # headers6 = []
            for th in defense.find('thead').find_all('th'):
                headers6.append(th.text.strip())

            cmp = "Tkl"
            if cmp in headers6:
                index = headers6.index(cmp)
                headers6 = headers6[index:-1]

            rows = []
            for tr in defense.find('tbody').find_all('tr'):
                row = []

                for td in tr.find_all('td')[4:-1]:
                    row.append(td.text.strip())

                rows.append(row)

        lv_defenses = pd.DataFrame(data=rows, columns=headers6)

        #possession table
        possessions = soup.find_all('table', {'id': 'stats_possession_9'})

        for possession in possessions:
            headers4 = []

            for th in possession.find('thead').find_all('th')[11:-1]:
                headers4.append(th.text.strip())

            cmp = 'Gls'
            if cmp in headers4:
                index = headers4.index(cmp)
                headers4 = headers4[index:-1]

            rows = []

            for tr in possession.find('tbody').find_all('tr'):
                row = []

                for td in tr.find_all('td')[4:-1]:
                    row.append(td.text.strip())

                rows.append(row)

        lv_possession = pd.DataFrame(data=rows, columns=headers4)



        team_players = pd.concat([standard, pass_ing, lv_pass_types, shoot_ing,
                                  lv_play, lv_possession, lv_defenses], axis=1)
        team_players.dropna(subset=['Player'], inplace=True)

        team_players['Nation'] = team_players['Nation'].str[-3:]

        return team_players


