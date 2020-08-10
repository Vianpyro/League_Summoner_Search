async function loadChampData(champion_name) {
    try {
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        champions.slice().forEach((champion) => { 
            // I need help to simplify this !!!
            if (champion_name === champion.name) {
                if (champion.displayName) { document.getElementById('modal-champ-name').innerHTML = champion.displayName } 
                else { document.getElementById('modal-champ-name').innerHTML = champion.name }
                if (champion.difficulty_rank != '?') { document.getElementById('modal-champ-skillcap').innerHTML = `#${champion.difficulty_rank}` } 
                else { document.getElementById('modal-champ-skillcap').innerHTML = '?' }
                document.getElementById('modal-champ-icon').src = `../src/img/icon/${champion.name}.jpg`
                document.getElementById('modal-champ-p').src = `../src/img/abilities/${champion.name}/p.png`
                document.getElementById('modal-champ-q').src = `../src/img/abilities/${champion.name}/q.png`
                document.getElementById('modal-champ-w').src = `../src/img/abilities/${champion.name}/w.png`
                document.getElementById('modal-champ-e').src = `../src/img/abilities/${champion.name}/e.png`
                document.getElementById('modal-champ-r').src = `../src/img/abilities/${champion.name}/r.png`
                document.getElementById('modal-p').innerHTML = champion.passive_name
                document.getElementById('modal-q').innerHTML = champion.q_name
                document.getElementById('modal-w').innerHTML = champion.w_name
                document.getElementById('modal-e').innerHTML = champion.e_name
                document.getElementById('modal-r').innerHTML = champion.r_name
                document.getElementById('modal-p-desc').innerHTML = champion.passive_description
                document.getElementById('modal-q-desc').innerHTML = champion.q_description
                document.getElementById('modal-w-desc').innerHTML = champion.w_description
                document.getElementById('modal-e-desc').innerHTML = champion.e_description
                document.getElementById('modal-r-desc').innerHTML = champion.r_description
            }
        });
        document.getElementById('modal').style.display = 'flex';
        console.log('a')
    } catch (err) {
        console.error(err);
    }
}