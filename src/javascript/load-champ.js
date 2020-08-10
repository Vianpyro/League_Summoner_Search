async function loadChampData(champion_name) {
    try {
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        champions.slice().forEach((champion) => { 
            // I need help to simplify this !!!
            if (champion_name === champion.name) {
                if (champion.displayName) { 
                    document.getElementById('modal-champ-name').innerHTML = champion.displayName
                } else {
                    document.getElementById('modal-champ-name').innerHTML = champion.name
                }

                document.getElementById('modal-champ-icon').src = `../src/img/icon/${champion.name}.jpg`

                if (champion.difficulty_rank != '?') { 
                    document.getElementById('modal-champ-skillcap').innerHTML = `#${champion.difficulty_rank}`
                } else {
                    document.getElementById('modal-champ-skillcap').innerHTML = '?'
                }
            }
        });
        document.getElementById('modal').style.display = 'flex';
        console.log('a')
    } catch (err) {
        console.error(err);
    }
}