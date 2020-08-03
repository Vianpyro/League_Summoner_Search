function loadChampData(on_error_link,
                       champion, champ_difficulty_rank, 
                       champ_p_name, champ_p_desc,
                       champ_q_name, champ_q_desc,
                       champ_w_name, champ_w_desc,
                       champ_e_name, champ_e_desc,
                       champ_r_name, champ_r_desc,
                       champ_meta_tier) {
    var w = window.open("");
    w.document.write(`<html>
                        <head>
                            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.13.0/css/all.css">
                            <link rel="stylesheet" href="../src/css/load-champions.css">
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>League of Help - ${champion}</title>
                        </head>
        
                        <body style="background-image: url(${on_error_link});background-repeat: no-repeat;background-attachment: fixed;background-size: cover;backdrop-filter: blur(8px);">
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
                                <a onclick="loadChampData('${champion}');">
                                <img id="champ-img" src="../src/img/icon/${champion}.jpg"
                                onerror="javascript: document.getElementById('champ-img').src = ${on_error_link}">
                                <figcaption id="champ-difficulty_rank"> Difficulty rank: #${champ_difficulty_rank}</figcaption></a>
                            </figure>
                            <div id="champ-stats">
                                <h3>Abilities:</h3>
                                <div class="tooltip" style="font-size:16px;">
                                    <img src="../src/img/abilities/${champion}/p.png" onerror="javascript: document.getElementById('abilities-p').src = '../src/img/image_not_found.png'" class="abilities" id='abilities-p'>
                                    <span class="tooltip-text"><b style='color:#d4af37;font-size:18px;'>${champ_p_name}</b></br>${champ_p_desc}</span>
                                </div>
                                <div class="tooltip" style="font-size:16px;">
                                    <img src="../src/img/abilities/${champion}/q.png" onerror="javascript: document.getElementById('abilities-q').src = '../src/img/image_not_found.png'" class="abilities" id='abilities-q'>
                                    <span class="tooltip-text"><b style='color:#d4af37;font-size:18px;'>${champ_q_name}</b></br>${champ_q_desc}</span>
                                </div>
                                <div class="tooltip" style="font-size:16px;">
                                    <img src="../src/img/abilities/${champion}/w.png" onerror="javascript: document.getElementById('abilities-w').src = '../src/img/image_not_found.png'" class="abilities" id='abilities-w'>
                                    <span class="tooltip-text"><b style='color:#d4af37;font-size:18px;'>${champ_w_name}</b></br>${champ_w_desc}</span>
                                </div>
                                <div class="tooltip" style="font-size:16px;">
                                    <img src="../src/img/abilities/${champion}/e.png" onerror="javascript: document.getElementById('abilities-e').src = '../src/img/image_not_found.png'" class="abilities" id='abilities-e'>
                                    <span class="tooltip-text"><b style='color:#d4af37;font-size:18px;'>${champ_e_name}</b></br>${champ_e_desc}</span>
                                </div>
                                <div class="tooltip" style="font-size:16px;">
                                    <img src="../src/img/abilities/${champion}/r.png" onerror="javascript: document.getElementById('abilities-r').src = '../src/img/image_not_found.png'" class="abilities" id='abilities-r'>
                                    <span class="tooltip-text"><b style='color:#d4af37;font-size:18px;'>${champ_r_name}</b></br>${champ_r_desc}</span>
                                </div>
                                <div class="meta">
                                    <h3>Meta tier ${champ_meta_tier}</h3>
                                </div>
                            </div>
                        </body>
                    </html>`);
    w.document.close();
}