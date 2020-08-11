function detect_region() {
    const region = document.getElementById("region"); // getting the selected server
    const selected_region = region.options[region.selectedIndex].text;

    switch (selected_region) {
        case "North America":
            document.getElementById("REGION").action = "https://na.op.gg/summoner/";
            break;
        case "Korea":
            document.getElementById("REGION").action = "https://www.op.gg/summoner/";
            break;
        case "Japan":
            document.getElementById("REGION").action = "https://jp.op.gg/summoner/";
            break;
        case "Europe West":
            document.getElementById("REGION").action = "https://euw.op.gg/summoner/";
            break;
        case "Europe Nordic & East":
            document.getElementById("REGION").action = "https://eune.op.gg/summoner/";
            break;
        case "Oceania":
            document.getElementById("REGION").action = "https://oce.op.gg/summoner/";
            break;
        case "Brazil":
            document.getElementById("REGION").action = "https://br.op.gg/summoner/";
            break;
        case "Latin America (South)":
            document.getElementById("REGION").action = "https://las.op.gg/summoner/";
            break;
        case "Latin America (North)":
            document.getElementById("REGION").action = "https://lan.op.gg/summoner/";
            break;
        case "Russia":
            document.getElementById("REGION").action = "https://ru.op.gg/summoner/";
            break;
        case "Turkey":
            document.getElementById("REGION").action = "https://tr.op.gg/summoner/";
            break;
        default:
            document.getElementById("REGION").action = "https://op.gg/summoner/";
    }
}
