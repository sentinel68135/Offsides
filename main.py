from player_data import PlayerStatsScraper

liver = 'https://fbref.com/en/squads/4ba7cbea/Bournemouth-Stats'

scraper = PlayerStatsScraper(liver)

heads = scraper.scrape_player_stats()

print(heads)
