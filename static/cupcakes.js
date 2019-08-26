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
    let newlyCreatedFlavor = newlyCreatedCupcake.data.cupcake.flavor;
    let newlyCreatedImage = newlyCreatedCupcake.data.cupcake.image;
    let $newCupcakeElement = $("<li>")
    let $newCupcakeAtag = $(`<a href="${newlyCreatedImage}">${newlyCreatedFlavor}</a>`)
    $newCupcakeElement.append($newCupcakeAtag)
    $cupcakesList.append($newCupcakeElement);


  })

  async function showCupcakes() {

    let cupcakesFromDB = await axios.get("/api/cupcakes");
    for (var i = 0; i < cupcakesFromDB.data.cupcakes.length; i++) {
      let newlyCreatedFlavor = cupcakesFromDB.data.cupcakes[i].flavor;
      let newlyCreatedImage = cupcakesFromDB.data.cupcakes[i].image;
      let $newCupcake = $("<li>")
      let $newCupcakeAtag = $(`<a href="${newlyCreatedImage}">${newlyCreatedFlavor}</a>`)
      $newCupcake.append($newCupcakeAtag)
      $cupcakesList.append($newCupcake);
    }

  }

  showCupcakes();









})