# -*- coding: utf-8 -*-
from lxml import html
import requests


class GetLeagueStatsBot:
    def __init__(self):
        base_url = 'https://na.leagueoflegends.com/en-us/news/tags/patch-notes'
        try:
            page = requests.get(f'{base_url}')
            tree = html.fromstring(page.content)
        except: pass

        try: self.PATCH = tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[1]/div/ol/li[1]/a/article/div[2]/div/h2/text()')[0][6:-6]
        except: self.PATCH = '"?"'
        print(self.PATCH)

    def get_champ_meta_tier(self, champion):
        base_url = 'https://na.op.gg/champion'
        try:
            page = requests.get(f'{base_url}/{champion.lower()}/statistics')
            tree = html.fromstring(page.content)
        except: pass

        try: return tree.xpath('//*[@class="champion-stats-header-info__tier"]/b/text()')[0][-1]
        except: pass

        
    def get_champ_abilities(self, champion):
        base_url = 'https://na.leagueoflegends.com/en-us/champions'
        page = requests.get(f'{base_url}/{champion.lower()}/')
        tree = html.fromstring(page.content)

        try:
            return (
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[1]/h5/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[1]/p/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[2]/h5/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[2]/p/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[3]/h5/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[3]/p/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[4]/h5/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[4]/p/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[5]/h5/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[5]/p/text()')[0].replace("\n", " ")
            )
        except: pass

if __name__ == '__main__':
    champ_stats = GetLeagueStatsBot()

new_champs, new_winrate = [], []

tier_op, tier_1, tier_2, tier_3, tier_4, tier_5 = [], [], [], [], [], []
for j in range (len(new_champs)):
    if new_winrate[j] > 53.0: tier_op.append(new_champs[j])
    elif 53.0 > new_winrate[j] > 51.0: tier_1.append(new_champs[j])
    elif 51.0 > new_winrate[j] > 50.0: tier_2.append(new_champs[j])
    elif 50.0 > new_winrate[j] > 49.0: tier_3.append(new_champs[j])
    elif 49.0 > new_winrate[j] > 48.0: tier_4.append(new_champs[j])
    else: tier_5.append(new_champs[j])

# List by hardest to easiest champion skill cap
s_tier = (
    'Aurelion Sol', 'Kalista', 'Draven', 'Gangplank', 'Thresh', 'Zed', 'Yasuo', 'Lee Sin', 'Azir', 'Nidalee', 
    'Riven', 'Leblanc', 'Akali', 'Bard'
)

a_tier = (
    'Rengar', 'Katarina', 'Cassiopeia', 'Elise', 'Twisted Fate', 'Shaco', 'Ivern', 'Pyke', 'Zoe', 'Vayne',
    'Qiyana', 'Lucian', 'Rakan', 'Tahm Kench', 'Jayce', 'Irelia', 'Fiora', 'Syndra', 'Kai\'Sa', 'Aatrox',
    'Rek\'Sai'
)

b_tier = (
    'Singed', 'Xerath', 'Anivia', 'Kha\'Zix', 'Ryze', 'Kled', 'Kindred', 'Orianna', 'Evelynn', 'Rumble',
    'Ekko', 'Taliyah', 'Vladimir', 'Karthus', 'Janna', 'Xayah', 'Ezreal', 'Camille', 'Gnar', 'Kayn',
    'Kog\'Maw', 'Alistar', 'Gragas', 'Sylas', 'Talon', 'Viktor', 'Aphelios'
)

c_tier = (
    'Fizz', 'Renekton', 'Heimerdinger', 'Ahri', 'Vel\'Koz', 'Jax', 'Twitch', 'Illaoi', 'Urgot', 'Jhin',
    'Yorick', 'Graves', 'Nunu & Willump', 'Kassadin', 'Shen', 'Ornn', 'Kennen', 'Sion', 'Quinn', 'Varus',
    'Senna', 'Fiddlesticks', 'Lissandra', 'Caitlyn', 'Lulu', 'Nami', 'Corki', 'Galio', 'Taric'
)

d_tier = (
    'Darius', 'Tryndamere', 'Mordekaiser', 'Master Yi', 'Neeko', 'Swain', 'Teemo', 'Zyra', 'Kayle', 'Olaf',
    'Udyr', 'Tristana', 'Nocturne', 'Nasus', 'Shyvana', 'Poppy', 'Volibear', 'Zac', 'Sejuani', 'Hecarim',
    'Skarner', 'Diana', 'Cho\'Gath', 'Jarvan IV', 'Blitzcrank', 'Nautilus', 'Wukong', 'Trundle', 'Morgana',
    'Zilean', 'Karma', 'Braum', 'Leona', 'Sivir', 'Maokai', 'Sett'
)

e_tier = (
    'Brand', 'Jinx', 'Vi', 'Veigar', 'Ziggs', 'Lux', 'Pantheon', 'Malzahar', 'Soraka', 'Miss Fortune', 
    'Ashe', 'Dr. Mundo', 'Yuumi', 'Xin Zhao', 'Garen', 'Amumu', 'Rammus', 'Warwick', 'Malphite', 'Sona', 'Annie'
)

unkown_tier = ( 
    'Lillia', 'Yone', 'Samira', 'Seraphine'
)

# Regroup and sort every champion in a single list
champions_list = sorted(s_tier + a_tier + b_tier + c_tier + d_tier + e_tier + unkown_tier)

word = '{\n"patch": %s,\n"champions":\n[' % (champ_stats.PATCH)
total_champions = len(champions_list)
for index, champ in enumerate(champions_list):
    # Get a "clean" champion name
    clean_champ_name = champ.replace("'", '-').replace(".", '').replace(" ", '-')

    # Don't put a ',' if first element when opening champion part
    if index == 0: word += '{\n'
    else: word += ',\n{\n'

    # Add champion name and (maybe) display name
    if "'" in champ or ' ' in champ:
        if champ == 'Nunu & Willump':
            word += '"name": "Nunu",\n'
        else:
            word += '"name": "%s",\n' % (champ.replace("'", '').replace(' ', '').replace('.', ''))
        word += f'"displayName": "{champ}",\n'
    else:
        word += f'"name": "{champ}",\n'


    # Add champion skill caps rank
    word += '"difficulty_rank": '
    if champ in s_tier: word += '%i' %(s_tier.index(champ) + 1)
    elif champ in a_tier: word += '%i' %(a_tier.index(champ) + len(a_tier) + 1)
    elif champ in b_tier: word += '%i' %(b_tier.index(champ) + len(s_tier + a_tier) + 1)
    elif champ in c_tier: word += '%i' %(c_tier.index(champ) + len(s_tier + a_tier + b_tier) + 1)
    elif champ in d_tier: word += '%i' %(d_tier.index(champ) + len(s_tier + a_tier + b_tier + c_tier) + 1)
    elif champ in e_tier: word += '%i' %(e_tier.index(champ) + len(s_tier + a_tier + b_tier + c_tier + d_tier) + 1)
    else: word += '"?"'
    word += ',\n'

    # Add champion meta rank
    champ_meta_tier = champ_stats.get_champ_meta_tier(clean_champ_name.replace('-', ''))
    word += f'"meta_tier": '
    if champ_meta_tier != None: word += f'{champ_meta_tier}'
    else: word += '"?"'
    word += '\n'
    
    # Add abilities
    champions_abilities = champ_stats.get_champ_abilities(clean_champ_name)
    if champions_abilities != None:
        abilities = ['p', 'q', 'w', 'e', 'r']
        for j in range (len(abilities)):
            word += f',"{abilities[j]}_name": "{champions_abilities[j * 2]}"\n'
            word += f',"{abilities[j]}_description": "{champions_abilities[(j * 2) + 1]}"\n'

    # Close champion part
    word += '}'

    # Print the amount of champions left
    print(total_champions - index)

word += ']}'
with open('src/json/champions.json', 'w') as f:
    f.write(word)

input('JSON file generated successfuly, press enter to close this dialog...')
