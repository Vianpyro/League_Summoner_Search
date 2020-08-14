async function loadChampData(champion_name) {
    try {
        // Retrieve champions data from json
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        // Target the selected champion
        const champ = champions.filter(e => e.name === champion_name);

        console.log(champ)

        // Replace datas
        const name = champ[0].displayName ? champ[0].displayName : champ[0].name;
        const skillcap = champ[0].difficulty_rank != "?" ? `#${champ[0].difficulty_rank}` : "?";
        const meta_tier = champ[0].meta_tier

        // Set champion details
        document.getElementById('modal-champ-name').innerHTML = name; 
        document.getElementById('modal-champ-skillcap').innerHTML = skillcap;
        document.getElementById('modal-champ-meta_tier').innerHTML = meta_tier;
        document.getElementById('modal-champ-icon').src = `../src/img/icon/${name}.jpg`;

        // Set champion details colors
        switch (meta_tier) {
            case 1: document.getElementById('modal-champ-meta_tier').style.color = 'red'; break
            case 2: document.getElementById('modal-champ-meta_tier').style.color = 'gray'; break
            case 3: document.getElementById('modal-champ-meta_tier').style.color = 'brown'; break
            case 4: document.getElementById('modal-champ-meta_tier').style.color = 'blue'; break
            case 5: document.getElementById('modal-champ-meta_tier').style.color = 'green'; break
        }

        // Doesn't worlk :(
        // const colors = ('red', 'blue', 'green', 'gray', 'black')
        // document.getElementById('modal-champ-meta_tier').style.color = colors[meta_tier - 1]

        const ablities = ["p","q","w","e","r"];
        ablities.forEach(e => {
            document.getElementById(`modal-champ-${e}`).src =  `../src/img/abilities/${name}/${e}.png`;
            document.getElementById(`modal-${e}`).innerHTML = champ[0][`${e}_name`]
            document.getElementById(`modal-${e}-desc`).innerHTML = champ[0][`${e}_description`];
        });
        document.getElementById('modal').style.display = 'flex';
    } catch (err) {
        console.error(err);
    }
}