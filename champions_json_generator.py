# -*- coding: utf-8 -*-
from lxml import html
import requests


class GetLeagueStatsBot:
    def __init__(self):
        self.get_patch()

    def load_page(self, url):
        try: return html.fromstring(requests.get(url).content)
        except: return

    def get_patch(self):
        tree = self.load_page('https://na.leagueoflegends.com/en-us/news/tags/patch-notes')
        return tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[1]/div/ol/li[1]/a/article/div[2]/div/h2/text()')[0][6:-6]

    def get_champion_rotation(self):
        tree = self.load_page('https://leagueoflegends.fandom.com/wiki/Free_champion_rotation')
        return [tree.xpath(f'//*[@id="mw-content-text"]/div[1]/div[1]/ol/li[{i}]/div/div[2]/a/text()')[0] for i in range (1, 16)]

    def get_champ_meta_tier(self, champion):
        tree = self.load_page('https://na.op.gg/champion/%s/statistics' % (champion.replace('-', '')))
        try: return tree.xpath('//*[@class="champion-stats-header-info__tier"]/b/text()')[0][-1]
        except: print(f"Unable to load {champion}'s meta tier.")
        
    def get_champ_abilities(self, champion):
        tree = self.load_page(f'https://na.leagueoflegends.com/en-us/champions/{champion.lower()}/')

        recent_abilities = {
            'Samira': (
                'Daredevil Impulse', "Samira builds a combo by hitting attacks or abilities from the previous hit. Each one increases her Style, from 'E' to 'S' grade. Samira gains movement speed according to her grade. Samira's attacks in melee range deal additional magic damage, increased with the target missing health. Samira's attacks against enemies affected by Immobilizing effects Knock Up for 0.5 seconds and deal damage over 6 separate attacks. Samira dashes into range against targets slightly outside of her attack range.",
                'Flair', f'Samira fires a shot, dealing physical damage to the first enemy hit. If this ability is cast towards an enemy in melee range, Samira will instead slash with her sword, dealing physical damage. Either hit can critically strike for 25% bonus damage. If cast during Wild Rush, Samira will strike all enemies in her path upon completion.',
                'Blade Whirl', 'Samira slashes around her for 1 second, damaging enemies twice dealing physical damage each and destroying any enemy missiles that enter the area.',
                'Wild Rush', "Samira dashes through an enemy or ally, slashing enemies she passes through and gaining Attack Speed. Killing an enemy champion refreshes this ability's cooldown.",
                'Inferno Trigger', "Samira can only use this ability if her current Style rating is 'S'. Samira unleashes a torrent of shots from her weapons, wildly shooting all enemies surrounding her 10 times over 2 seconds, each shot dealing physical damage and applying lifesteal. Each shot can also critically strike."
            )
        }

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
        except:
            try: return recent_abilities[champion]
            except: print(f"Unable to load {champion}'s abilities.")


if __name__ == '__main__':
    champ_stats = GetLeagueStatsBot()  
    free_champion_rotation = champ_stats.get_champion_rotation()
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
    champions_list = (
        'Aurelion Sol', 'Kalista', 'Draven', 'Gangplank', 'Thresh', 'Zed', 'Yasuo', 'Lee Sin', 'Azir', 'Nidalee',
        'Riven', 'Yone', 'Leblanc', 'Akali', 'Bard', 'Rengar', 'Katarina', 'Cassiopeia', 'Elise', 'Twisted Fate',
        'Shaco', 'Ivern', 'Pyke', 'Zoe', 'Vayne', 'Qiyana', 'Lucian', 'Rakan', 'Tahm Kench', 'Jayce', 'Irelia', 
        'Fiora', 'Syndra', 'Kai\'Sa', 'Aatrox', 'Rek\'Sai', 'Singed', 'Xerath', 'Anivia', 'Kha\'Zix', 'Ryze', 
        'Kled', 'Kindred', 'Orianna', 'Evelynn', 'Rumble', 'Ekko', 'Taliyah', 'Vladimir', 'Karthus', 'Janna', 
        'Xayah', 'Ezreal', 'Camille', 'Gnar', 'Kayn', 'Kog\'Maw', 'Alistar', 'Gragas', 'Sylas', 'Talon', 'Viktor',
        'Aphelios', 'Fizz', 'Renekton', 'Heimerdinger', 'Ahri', 'Vel\'Koz', 'Jax', 'Twitch', 'Illaoi', 'Urgot',
        'Jhin',  'Yorick', 'Graves', 'Nunu & Willump', 'Kassadin', 'Shen', 'Ornn', 'Kennen', 'Sion', 'Quinn', 
        'Varus', 'Senna', 'Fiddlesticks', 'Lissandra', 'Caitlyn', 'Lulu', 'Nami', 'Corki', 'Galio', 'Taric', 
        'Darius', 'Tryndamere', 'Mordekaiser', 'Master Yi', 'Neeko', 'Lillia', 'Swain', 'Teemo', 'Zyra', 'Kayle',
        'Olaf', 'Udyr', 'Tristana', 'Nocturne', 'Nasus', 'Shyvana', 'Poppy', 'Volibear', 'Zac', 'Sejuani',
        'Hecarim', 'Skarner', 'Diana', 'Cho\'Gath', 'Jarvan IV', 'Blitzcrank', 'Nautilus', 'Wukong', 'Trundle',
        'Morgana', 'Zilean', 'Karma', 'Braum', 'Leona', 'Sivir', 'Maokai', 'Sett', 'Brand', 'Jinx', 'Vi', 'Veigar',
        'Ziggs', 'Lux', 'Pantheon', 'Malzahar', 'Soraka', 'Miss Fortune', 'Ashe', 'Dr. Mundo', 'Yuumi', 'Xin Zhao',
        'Garen', 'Amumu', 'Rammus', 'Warwick', 'Malphite', 'Sona', 'Annie', 'Samira', 'Seraphine', 'Ultra-Heavy Tank Support'
    )

    no_data_champions = ('Samira', 'Seraphine', 'Ultra-Heavy Tank Support')

    word = '{\n"patch": %s,\n"champions":\n[' % (champ_stats.get_patch())
    total_champions = len(champions_list)
    for index, champ in enumerate(sorted(champions_list)):
        # Don't put a ',' if first element when opening champion part
        if index == 0: word += '{\n'
        else: word += ',\n{\n'

        # Add champion name and (maybe) display name
        LoL_names = {
            'Aurelion Sol': 'Aurelion-Sol',
            "Cho'Gath": 'Cho-Gath',
            'Dr. Mundo': 'Dr-Mundo',
            'Jarvan IV': 'Jarvan-IV',
            "Kai'Sa": 'Kai-Sa',
            "Kha'Zix": 'Kha-Zix',
            "Kog'Maw": 'Kog-Maw',
            'Lee Sin': 'Lee-Sin',
            'Master Yi': 'Master-Yi',
            'Miss Fortune': 'Miss-Fortune',
            'Nunu & Willump': 'Nunu', 
            "Rek'Sai": 'Rek-Sai',
            'Tahm Kench': 'Tahm-Kench',
            'Twisted Fate': 'Twisted-Fate',
            "Vel'Koz": 'Vel-Koz',
            'Xin Zhao': 'Xin-Zhao'
        }

        if champ in LoL_names:
            word += f'"name": "{LoL_names[champ]}",\n'
            word += f'"displayName": "{champ}",\n'
            champions_abilities = champ_stats.get_champ_abilities(LoL_names[champ])
            champ_meta_tier = champ_stats.get_champ_meta_tier(LoL_names[champ].lower())
        else:
            champions_abilities = champ_stats.get_champ_abilities(champ)
            word += f'"name": "{champ}",\n'
            champ_meta_tier = champ_stats.get_champ_meta_tier(champ.lower())

        if champ in free_champion_rotation: word += f'"free": true,\n'

        # Add abilities
        if champions_abilities != None:
            abilities = ['p', 'q', 'w', 'e', 'r']
            for j in range (len(abilities)):
                word += f'"{abilities[j]}_name": "{champions_abilities[j * 2]}",\n'
                word += f'"{abilities[j]}_description": "{champions_abilities[(j * 2) + 1]}",\n'

        # Add champion skill caps rank
        if champ in no_data_champions: word += '"difficulty_rank": "?",\n'
        else: word += f'"difficulty_rank": {champions_list.index(champ) + 1},\n'

        # Add champion meta rank
        word += '"meta_tier": '
        if champ_meta_tier != None: word += f'{champ_meta_tier}'
        else: word += '"?"'
        word += '\n'

        # Close champion part
        word += '}'

        # Print the amount of champions left
        print(total_champions - index)

    word += ']}'
    with open('src/json/champions.json', 'w') as f:
        f.write(word)

    input('JSON file generated successfuly, press enter to close this dialog...')
