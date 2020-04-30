function loadChampData(champion) {
    var w = window.open("");
    w.document.write(`<html>
                        <head>
                            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.13.0/css/all.css">
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>League of Help - ${champion}</title>
                        </head>
        
                        <body>
                            <nav class="header">
                                <h2 class="logo">League of Help</h2>
                                <input type="checkbox" id="chk">
                                <label for="chk" class="show-menu-btn">
                                    <i class="fas fa-ellipsis-h"></i>
                                </label>

                                <ul class="menu">
                                    <a href="https://vianpyro.github.io/League-of-Help/">Stay home</a>
                                    <a href="#">Build tips</a>
                                    <a href="https://vianpyro.github.io/League-of-Help/pages/champs.html">Champions</a>
                                    <label for="chk" class="hide-menu-btn">
                                        <i class="fas fa-times"></i>
                                    </label>
                                </ul>
                            </nav>

                            <center>
                                <div class="${champion}">
                                    <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/${champion}_0.jpg">
                                </div>
                            </center>
                        </body>

                        <style type="text/css" id="css-navbar">.header{background-color:#333;color:#f1f1f1;height:100px;padding:0 20px;}.logo{float:left;line-height:100px;text-transform:uppercase;}.menu{float:right;line-height:100px;}.menu a{color:#f1f1f1;padding:40px 10px;text-decoration:none;text-transform:uppercase;transition:350ms;}.show-menu-btn,.hide-menu-btn{cursor:pointer;display:none;transition:350ms;font-size:30px;}.show-menu-btn{float:right;}.show-menu-btn i{line-height:100px;}.menu a:hover,.show-menu-btn:hover,.hide-menu-btn:hover{color:#3498db;}#chk{position:absolute;visibility:hidden;z-index:-1111;}@media screen and (max-width:800px){.show-menu-btn,.hide-menu-btn{display:block;}.menu{position:fixed;width:100%;height:100vh;background:#333;right:-100%;top:0;text-align:center;padding:80px 0;line-height:normal;transition:.7s;}.menu a{display:block;padding:20px;}.hide-menu-btn{position:absolute;top:40px;right:40px;}#chk:checked ~ .menu{right:0;}}@media screen and (min-width:800px){.menu a:hover{background-color:#666;border-radius:10px;}}</style>
                        <style type="text/css" id="css-styles">*{font-family:sans-serif;margin:0;padding:0;}body{background-color:#888;}</style>
                    </html>`);
    w.document.close();
}