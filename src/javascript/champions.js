async function displayChampions() {
    try {
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        document.getElementById("champ-toptext").innerHTML = ("With " + champions.length + " champions, you’ll find the perfect match for your playstyle. Master one, or master them all.")

        champions.slice().forEach((champion, i) => {
            // I change the 'on_error_link' because I often code without internet connection - the second link should always be inactive.
            var on_error_link = 'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${champion.name}_0.jpg'
            // var on_error_link = '../src/img/image_not_found.png'
            document.getElementById(`champions`).innerHTML +=
                `<figure>
                    <a id="get${champion.name}Stats" onclick="loadChampData('${on_error_link}',
                    '${champion.name}', '${champion.difficulty_rank}', 
                    '${champion.passive_name}', '${champion.passive_description}',
                    '${champion.q_name}', '${champion.q_description}', '${champion.w_name}', '${champion.w_description}',
                    '${champion.e_name}', '${champion.e_description}', '${champion.r_name}', '${champion.r_description}',
                    '${champion.meta_tier}');">
                    <img class="champ-img" id="get${champion.name}Icon" src="../src/img/icon/${champion.name}.jpg"
                    onerror="javascript: document.getElementById('get${champion.name}Icon').src = ${on_error_link}">
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