async function displayChampions() {
    try {
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        document.getElementById("champ-toptext").innerHTML = ("With " + champions.length + " champions, you’ll find the perfect match for your playstyle. Master one, or master them all.")

        champions.slice().forEach((element, i) => {
            document.getElementById(`champions`).innerHTML +=
                `<figure><a id="get${element.name}Stats" onclick="loadChampData('${element.name}');">
                    <img class="champ-img" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${element.name}_0.jpg">
                    <figcaption id="champ${element.name}Name"></figcaption></a></figure>`;

            if (element.displayName) {
                document.getElementById(`champ${element.name}Name`).innerHTML = `${element.displayName}`;
            } else {
                document.getElementById(`champ${element.name}Name`).innerHTML = `${element.name}`;
            }
        });
    } catch (err) {
        console.error(err);
    }
}

displayChampions();