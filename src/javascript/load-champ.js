async function loadChampData(champion_name) {
    try {
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        champions.slice().forEach((champion) => { 
            // I need help to simplify this !!!
            if (champion_name === champion.name) {
                console.log(champion.name)            
                var w = window.open("");
                w.document.write(`<html>
                        <head>
                            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.13.0/css/all.css">
                            <link rel="stylesheet" href="../src/css/load-champions.css">
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>League of Help - ${champion.name}</title>
                        </head>
        
                        <body id="load-champ-bg" style="background-image: url('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${champion.name}_0.jpg');"
                        onerror="onerror="this.src='../src/img/image_not_found.png';this.onerror=null;">
                            <nav class="header">
                                <h2 class="logo">League of Help</h2>
                                <input type="checkbox" id="chk">
                                <label for="chk" class="show-menu-btn">
                                    <i class="fas fa-ellipsis-h"></i>
                                </label>

                                <ul class="menu">
                                    <a href="../index.html">Stay home</a>
                                    <a href="#">Build tips</a>
                                    <a href="../pages/champs.html">Champions</a>
                                    <label for="chk" class="hide-menu-btn">
                                        <i class="fas fa-times"></i>
                                    </label>
                                </ul>
                            </nav>

                            <figure id="champ-icon">
                                <a onclick="loadChampData('${champion.name}');">
                                <img id="champ-img" src="../src/img/icon/${champion.name}.jpg" onerror="this.onerror=null;this.src='../src/img/image_not_found.png';">
                                <figcaption id="champ-difficulty_rank">${champion.name}</br>Difficulty rank: #${champion.difficulty_rank}</figcaption></a>
                            </figure>
                            <div id="champ-stats">
                                <h3>Abilities:</h3>
                                <div class="tooltip" style="font-size:16px;">
                                    <img src="../src/img/abilities/${champion.name}/p.png" onerror="this.onerror=null;this.src = '../src/img/image_not_found.png';" class="abilities" id='abilities-p'>
                                    <span class="tooltip-text"><b style='color:#d4af37;font-size:18px;'>${champion.passive_name}</b></br>${champion.passive_description}</span>
                                </div>
                                <div class="tooltip" style="font-size:16px;">
                                    <img src="../src/img/abilities/${champion.name}/q.png" onerror="this.onerror=null;this.src = '../src/img/image_not_found.png';" class="abilities" id='abilities-q'>
                                    <span class="tooltip-text"><b style='color:#d4af37;font-size:18px;'>${champion.q_name}</b></br>${champion.q_description}</span>
                                </div>
                                <div class="tooltip" style="font-size:16px;">
                                    <img src="../src/img/abilities/${champion.name}/w.png" onerror="this.onerror=null;this.src = '../src/img/image_not_found.png';" class="abilities" id='abilities-w'>
                                    <span class="tooltip-text"><b style='color:#d4af37;font-size:18px;'>${champion.w_name}</b></br>${champion.w_description}</span>
                                </div>
                                <div class="tooltip" style="font-size:16px;">
                                    <img src="../src/img/abilities/${champion.name}/e.png" onerror="this.onerror=null;this.src = '../src/img/image_not_found.png';" class="abilities" id='abilities-e'>
                                    <span class="tooltip-text"><b style='color:#d4af37;font-size:18px;'>${champion.e_name}</b></br>${champion.e_description}</span>
                                </div>
                                <div class="tooltip" style="font-size:16px;">
                                    <img src="../src/img/abilities/${champion.name}/r.png" onerror="this.onerror=null;this.src = '../src/img/image_not_found.png';" class="abilities" id='abilities-r'>
                                    <span class="tooltip-text"><b style='color:#d4af37;font-size:18px;'>${champion.r_name}</b></br>${champion.r_description}</span>
                                </div>
                                <div class="meta">
                                    <h3>Meta tier ${champion.meta_tier}</h3>
                                </div>
                            </div>
                        </body>
                    </html>`);
                w.document.close();

                if (champion.displayName) {
                    w.document.title = `League of Help - ${champion.displayName}`;
                    w.document.getElementById(`champ-difficulty_rank`).innerHTML = `${champion.displayName}</br>Difficulty rank: #${champion.difficulty_rank}`;
                }
            }
        });
    } catch (err) {
        console.error(err);
    }
}