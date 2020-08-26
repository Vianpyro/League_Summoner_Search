function detect_region() {
    const region = document.getElementById("region"); // getting the selected server
    const selected_region = region.options[region.selectedIndex].text;

    const regions_dim = {
        "Brazil": "br",
        "Europe Nordic & East": "eune",
        "Europe West": "euw",
        "Japan": "jp",
        "Korea": "www",
        "Latin America (North)": "lan",
        "Latin America (South)": "las",
        "North America": "na",
        "Oceania": "oce",
        "Russia": "ru",
        "Turkey": "tr",
    }

    if (selected_region in regions_dim) {
        document.getElementById("REGION").action = `https://${regions_dim[selected_region]}.op.gg/summoner/`;
    } else {
        document.getElementById("REGION").action = `https://op.gg/summoner/`;
    }
}
