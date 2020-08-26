async function displayChampions() {
    try {
        // Retrieve champions data from json
        const data = new Request(`../src/json/champions.json`);
        const { champions } = await fetch(data).then(data => data.json());

        // Set header text
        document.getElementById("champ-toptext").innerHTML = `With ${champions.length} champions, you’ll find the perfect match for your playstyle. Master one, or master them all.`;

        // Create a grid with all the champions
        champions.forEach((champion) => {

            // Grid
            document.getElementById(`champions`).innerHTML += 
            `
            <figure class="#${champion.difficulty_rank}">
                <a class="championData" data-champion="${champion.name}">
                    <img class="champ-img" src="../src/img/champions/${champion.name}/icon.jpg">
                    <figcaption id="champ${champion.name}Name"></figcaption>
                </a>
            </figure>
            `;

            // Display champ data when clicked on
            document.querySelectorAll(".championData").forEach(e => {
                e.addEventListener("click", () => {
                    loadChampData(e.dataset.champion)
                })
            })

            const name = champion.displayName ? champion.displayName : champion.name;
            document.getElementById(`champ${champion.name}Name`).innerHTML = name;
        });        

        // Close modal by clicking on modal-close
        document.getElementById('modal-close').addEventListener('click', () => document.getElementById('modal').style.display = 'none');
        
        // Close modal by pressing esc key
        document.body.onkeyup = e => {
            if (e.key === 'Escape' || e.key === 'Esc') return document.getElementById('modal').style.display = 'none';
        }

        // Close modal by clicking out of it
        window.addEventListener('click', function (e) {
            if (!document.getElementById('modal-wrapper').contains(e.target)) {
                return document.getElementById('modal').style.display = 'none';
            }
        });

        // If champs img not found
        document.querySelectorAll('img').forEach(img => img.onerror = function () { this.src = '../src/img/image_not_found.png'; });

    } catch (err) {
        console.error(err);
    }
}

displayChampions();