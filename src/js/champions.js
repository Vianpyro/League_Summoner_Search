async function displayChampions() {
    try {
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        document.getElementById("champ-toptext").innerHTML = ("With "+ champions.length + " champions, you’ll find the perfect match for your playstyle. Master one, or master them all.")
        console.log("There are " + champions.length + " champions in League of Legends.")


        if (screen.width >= 580) {            
            document.getElementById("champions").innerHTML += `<table id="champ_lines"></table>`;
    
            for (i = 0; i < champions.length / 5; i++) {
                document.getElementById("champ_lines").innerHTML += `<tr id="champ_line_${i}"></tr>`;
            }
    
    
            champions.slice().forEach((element, i) => {
                if (element.displayName) {
                    document.getElementById(`champ_line_${Math.round((i - 2) / 5)}`).innerHTML += 
                    `<td><figure><a>
                    <img class="champ-img" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${element.name}_0.jpg">
                    <br><p>${element.displayName}</p></a></figure></td>`;
                } else {
                    document.getElementById(`champ_line_${Math.round((i - 2) / 5)}`).innerHTML += 
                    `<td><figure><a>
                    <img class="champ-img" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${element.name}_0.jpg">
                    <br><p>${element.name}</p></a></figure></td>`;
                }
            });
        } else {
            document.getElementById("champions").innerHTML += `<ul id="champs_list"></ul>`;


            champions.slice().forEach((element, i) => {
                if (element.displayName) {
                    document.getElementById(`champs_list`).innerHTML +=
                        `<li><figure><a>
                    <img class="champ-img" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${element.name}_0.jpg">
                    <br><p>${element.displayName}</p></a></figure></li>`;
                } else {
                    document.getElementById(`champs_list`).innerHTML +=
                        `<li><figure><a>
                    <img class="champ-img" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${element.name}_0.jpg">
                    <br><p>${element.name}</p></a></figure></li>`;
                }
            });
        }



    } catch (err) {
        console.error(err);
    }
}

displayChampions();