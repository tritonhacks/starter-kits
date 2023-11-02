const fishwatchEndpoint = 'http://127.0.0.1:5000/search/'

// Use this to load in auto-complete results
document.addEventListener("DOMContentLoaded", async function () {
    let searchButton = document.getElementById("submit")
    let resultsDiv = document.getElementById("results")
    let resultsDisplay = document.getElementById('result-text');
    let resultsBioDisplay = document.getElementById('result-bio-text');
    let resultsHeader = document.getElementById('result-header');
    let resultLocation = document.getElementById("result-location");
    let imageDisplay = document.getElementById("result-image");
    let queryArea = document.getElementById('query');
    let dataList = document.getElementById('fish-names')

    let results = await fetch('http://127.0.0.1:5000/names', {
        method: 'GET',
        headers: { 'Accept': 'application/json' }
    });

    let decoded = (await results.json());

    for (var i = 0; i < decoded.length; i++) {
        let option = document.createElement("option")
        option.value = decoded[i]
        dataList.appendChild(option)
    }

    resultsDiv.style.display = 'none'

    searchButton.addEventListener("click", async function (event) {
        event.preventDefault() // Prevent page redirection

        let fish = queryArea.value
        let results = await fetch(fishwatchEndpoint + fish, {
            method: 'GET',
            headers: { 'Accept': 'application/json' }
        });

        if (!results.ok) {
            resultsDiv.style.display = ''
            resultsHeader.innerHTML = `ERROR: "${fish}" not found`
            return
        }

        resultsDiv.style.display = ''

        // Fishing Rate, Habitat, Location, Population, Species Illustration Photo >src, Scientific Name
        let decoded = (await results.json())[0]
        let description = decoded["Physical Description"]

        // get random image from image gallery
        let images = decoded["Image Gallery"]

        console.log(images)
        console.log(decoded)
        /*
            This function returns a random number between 0 and max that is then stored in getRandomIndex.
        */
        const getRandomIndex = function(max) {
            return Math.floor(Math.random() * max)
        }
        
        /*
            This function returns an element of inArray at a random index, using our function above. 
            Here, it returns a random URL that will act as the source of an image.
        */
        const getRandomElementFromArray = function(inArray) {
            return inArray[getRandomIndex(inArray.length)]
        }


        imageDisplay.src = getRandomElementFromArray(images).src
        resultsDisplay.innerHTML = description;
        resultsHeader.innerHTML = decoded["Species Name"]
        resultLocation.innerHTML = decoded["Location"]
        resultsBioDisplay.innerHTML = decoded["Biology"]
    })
})

