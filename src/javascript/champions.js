async function displayChampions() {
    try {
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        document.getElementById("champ-toptext").innerHTML = ("With " + champions.length + " champions, you’ll find the perfect match for your playstyle. Master one, or master them all.")

        champions.slice().forEach((element, i) => {
            // I change the 'on_error_link' because I often code without internet connection - the second link should always be inactive.
            var on_error_link = 'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${element.name}_0.jpg'
            // var on_error_link = '../src/img/image_not_found.png'
            document.getElementById(`champions`).innerHTML +=
                `<figure>
                    <a id="get${element.name}Stats" onclick="loadChampData('${on_error_link}',
                    '${element.name}', '${element.difficulty_rank}', 
                    '${element.passive_name}', '${element.passive_description}',
                    '${element.q_name}', '${element.q_description}', '${element.w_name}', '${element.w_description}',
                    '${element.e_name}', '${element.e_description}', '${element.r_name}', '${element.r_description}',
                    '${element.meta_tier}');">
                    <img class="champ-img" id="get${element.name}Icon" src="../src/img/icon/${element.name}.jpg"
                    onerror="javascript: document.getElementById('get${element.name}Icon').src = '../src/img/image_not_found.png'">
                    <figcaption id="champ${element.name}Name"></figcaption></a>
                </figure>`;

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