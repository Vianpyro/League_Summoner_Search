async function displayChampions() {
    try {
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        document.getElementById("champ-toptext").innerHTML = ("With " + champions.length + " champions, you’ll find the perfect match for your playstyle. Master one, or master them all.")

        champions.slice().forEach((element, i) => {
            if (element.displayName) {
                document.getElementById(`champions`).innerHTML +=
                    `<figure><a>
                    <img class="champ-img" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${element.name}_0.jpg">
                    <figcaption>${element.displayName}</figcaption></a></figure>`;
            } else {
                document.getElementById(`champions`).innerHTML +=
                    `<figure><a>
                    <img class="champ-img" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${element.name}_0.jpg">
                    <figcaption>${element.name}</figcaption></a></figure>`;
            }
        });
    } catch (err) {
        console.error(err);
    }
}

displayChampions();