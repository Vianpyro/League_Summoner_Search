async function loadChampData(champion_name) {
    try {
        //Retrieve champions data from json
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        //Take the selected champ
        const champ = champions.filter(e => e.name === champion_name);

        console.log(champ)

        //Replace datas
        const name = champ[0].displayName ? champ[0].displayName : champ[0].name;
        const rank = champ[0].difficulty_rank != "?" ? `#${champ[0].difficulty_rank}` : "?";

        //Set champ details
        document.getElementById('modal-champ-name').innerHTML = name; 
        document.getElementById('modal-champ-skillcap').innerHTML = rank;
        document.getElementById('modal-champ-icon').src = `../src/img/icon/${name}.jpg`;

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