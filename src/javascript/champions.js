async function displayChampions() {
    try {
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        document.getElementById("champ-toptext").innerHTML = ("With " + champions.length + " champions, you’ll find the perfect match for your playstyle. Master one, or master them all.")

        champions.slice().forEach((champion) => {
            // I change the 'on_error_link' because I often code without internet connection - the second link should always be inactive.
            document.getElementById(`champions`).innerHTML +=
                `<figure class="champion-figure">
                    <a onclick="loadChampData('${champion.name}');">
                    <img class="champ-img" src="../src/img/icon/${champion.name}.jpg" onerror="this.src='../src/img/image_not_found.png';this.onerror=null;">
                    <figcaption id="champ${champion.name}Name"></figcaption></a>
                </figure>`;

            if (champion.displayName) {
                document.getElementById(`champ${champion.name}Name`).innerHTML = `${champion.displayName}`;
            } else {
                document.getElementById(`champ${champion.name}Name`).innerHTML = `${champion.name}`;
            }
        });
    } catch (err) {
        console.error(err);
    }
}

displayChampions();