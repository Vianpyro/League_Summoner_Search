from lxml import html
import requests


class GetMetaBot:
    def __init__(self):
        self.base_url = 'https://op.gg/champion/statistics'

        self.page = requests.get(f'{self.base_url}')
        self.tree = html.fromstring(self.page.content)

        self.get_meta()

    def get_meta(self):
        champions_list = self.tree.xpath('//*[@class="champion-index-table__name"]/text()')
        winrate = self.tree.xpath('//*[@class="champion-index-table__cell champion-index-table__cell--value"]/text()')
        patch = self.tree.xpath('//*[@class="champion-index__version"]/text()')

        winrate_list = [float(winrate[i * 4][0:-1]) for i in range (len(winrate) // 4)]

        return patch[-1][19:25], champions_list, winrate_list


class GetStatsBot:
    def __init__(self):
        self.base_url = 'https://na.leagueoflegends.com/en-us/champions'
        
    def get_champ_stats(self, champion):
        page = requests.get(f'{self.base_url}/{champion.lower()}/')
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
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[5]/p/text()')[0].replace("\n", " "),
            )
        except: pass

if __name__ == '__main__':
    bot = GetMetaBot()
    PATCH, CHAMPS, WINRATE = bot.get_meta()

champion_ability = GetStatsBot()

new_champs, new_winrate = [], []
for i in range (len(CHAMPS)):
    if not CHAMPS[i] in new_champs:
        new_champs.append(CHAMPS[i])
        new_winrate.append(WINRATE[i])

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
champions = sorted(s_tier + a_tier + b_tier + c_tier + d_tier + e_tier + unkown_tier)

word = '{\n"champions":\n['
for index, champ in enumerate(champions):
    #print champ stats
    clean_champ_name = champ.replace("'", '-').replace(".", '').replace(" ", '-')

    # Don't put a ',' if first element when opening champion part
    if index == 0: word += '{\n'
    else: word += ',\n{\n'

    # Add champion name and (maybe) display name
    if "'" in champ or ' ' in champ:
        if champ == 'Nunu & Willump':
            word += '"name": "Nunu",\n'
        elif "'" in champ:
            word += '"name": "%s",\n' % (champ[0] + champ[1:].replace("'", '').replace(' ', '').lower())
        else:
            word += '"name": "%s",\n' % (champ.replace("'", '').replace(' ', '').replace('.', ''))
        word += '"displayName": "%s",\n' % (champ)
    else:
        word += '"name": "%s",\n' % (champ)


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
    word += '"meta_tier": '
    if champ in tier_op: word += '"OP"'
    elif champ in tier_1: word += '1'
    elif champ in tier_2: word += '2'
    elif champ in tier_3: word += '3'
    elif champ in tier_4: word += '4'
    elif champ in tier_5: word += '5'
    else: word += '": unknown"'
    word += '\n'

    # Add abilities
    champions_abilities = champion_ability.get_champ_stats(clean_champ_name)
    if champions_abilities != None:
        word += f',"p_name": "{champions_abilities[0]}"\n'
        word += f',"p_description": "{champions_abilities[1]}"\n'
        word += f',"q_name": "{champions_abilities[2]}"\n'
        word += f',"q_description": "{champions_abilities[3]}"\n'
        word += f',"w_name": "{champions_abilities[4]}"\n'
        word += f',"w_description": "{champions_abilities[5]}"\n'
        word += f',"e_name": "{champions_abilities[6]}"\n'
        word += f',"e_description": "{champions_abilities[7]}"\n'
        word += f',"r_name": "{champions_abilities[8]}"\n'
        word += f',"r_description": "{champions_abilities[9]}"\n'

    # Close champion part
    word += '}'

word += ']}'
with open('src/json/champions.json', 'w') as f:
    f.write(word)

input('JSON file generated successfuly, press enter to close this dialog...')