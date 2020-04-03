async function displayChampions() {
    try {
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());
        console.log("There are " + champions.length + " champions in League of Legends.")

        for (i = 0; i < champions.length / 5; i++) {
            document.getElementById("champions").innerHTML += `<table class="champ_lines"><tr id="champ_line_${i}"></tr></table>`;
        }

        champions.slice().forEach((element, i) => {
            if (element.displayName) {
                document.getElementById(`champ_line_${Math.round((i - 2) / 5)}`).innerHTML += 
                `<td><figure><a>
                <img class="champ-img" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${element.name}_0.jpg">
                <br>${element.displayName}</a></figure></td>`;
            } else {
                document.getElementById(`champ_line_${Math.round((i - 2) / 5)}`).innerHTML += 
                `<td><figure><a>
                <img class="champ-img" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${element.name}_0.jpg">
                <br>${element.name}</a></figure></td>`;
            }
        });


    } catch (err) {
        console.error(err);
    }
}

displayChampions();