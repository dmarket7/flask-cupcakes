$(async function () {
    const $cupcakesContainer = $('#cupcakes-container');
    const $cupcakeForm = $('#cupcake-form');
    const $cupcakeFlavor = $('#cupcake-flavor');
    const $cupcakeSize = $('#cupcake-size');
    const $cupcakeRating = $('#cupcake-rating');
    const $cupcakeImage = $('#cupcake-image');
    const $cupcakesList = $('#cupcakes-list')


    $cupcakeForm.on("submit", async function (e) {
        e.preventDefault()

        let formCupcakeFlavor = $cupcakeFlavor.val()
        let formCupcakeSize = $cupcakeSize.val()
        let formCupcakeRating = $cupcakeRating.val()
        let formCupcakeImage = $cupcakeImage.val()

        let newCupcake = {
            "flavor": formCupcakeFlavor,
            "size": formCupcakeSize,
            "rating": formCupcakeRating,
            "image": formCupcakeImage
        }
        let newlyCreatedCupcake = await axios.post("/api/cupcakes", newCupcake);
        let newCupcakeElement= $("<li>")
        console.log(newlyCreatedCupcake)
        newCupcakeElement.text(newlyCreatedCupcake.data.cupcake.flavor);
        $cupcakesList.append(newCupcakeElement);

    
    })

    async function showCupcakes() {

        let cupcakesFromDB = await axios.get("/api/cupcakes");
        console.log(cupcakesFromDB)
        for (var i = 0; i < cupcakesFromDB.data.cupcakes.length; i++) {
            let newCupcake = $("<li>")
            newCupcake.text(cupcakesFromDB.data.cupcakes[i].flavor);
            $cupcakesList.append(newCupcake);
        }

    }

    showCupcakes();









})