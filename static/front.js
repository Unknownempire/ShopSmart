let browsed_product = document.getElementById('browsed_product');
let recommendation = document.getElementById('recommendations');
function fetch_browsing_history () {fetch('http://127.0.0.1:5000/getUserBrowseHistory')
.then(response => response.json())
.then(dataArray => {
    console.log(dataArray)
    dataArray.forEach(element => {
        // console.log(element);
        let newdiv = document.createElement("div")
        newdiv.className = 'browsed_items'
        newdiv.innerHTML = `<p>${element[1]}`;
        browsed_product.append(newdiv);

            console.log(element[1])
    });
})
.catch(error => {
    console.log("Error",error)
})};

fetch_browsing_history();

console.log("---------------product recommendation------------")

fetch('http://127.0.0.1:5000/productRecommendation') 
    .then(response => response.json())
    .then(dataArray => {
        console.log(dataArray)
        dataArray.forEach(element => {
            // console.log(element);
            let newdiv = document.createElement("div")
            newdiv.className = 'recommended_items'
            newdiv.innerHTML = `<p>${element[1]}`;
            recommendations.append(newdiv);
            console.log(element[1])
        });
    })
    .catch(error => {
        console.log("Error", error)
    });