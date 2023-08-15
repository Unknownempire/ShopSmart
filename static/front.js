let browsed_product = document.getElementById('browsed_product');
let recommendations = document.getElementById('recommendations');
let cartButton =document.getElementById('cartButton')
function fetch_browsing_history () {fetch('http://127.0.0.1:5000/getUserBrowseHistory')
.then(response => response.json())
.then(dataArray => {
    // console.log(dataArray)
    dataArray.forEach(element => {
        // console.log(element);
        let newdiv = document.createElement("div")
        newdiv.className = 'browsed_items'
        styling_div(newdiv);
        newdiv.innerHTML = `<img src="./images/ ${element[1].jpg}></img>"
                            <p>${element[1]}</p><p>${element[2]}</p>`;
        browsed_product.append(newdiv);

            // console.log(element[1])
    });
})
.catch(error => {
    console.log("Error",error)
})};

fetch_browsing_history();

// console.log("---------------product recommendation------------")

fetch('http://127.0.0.1:5000/productRecommendation') 
    .then(response => response.json())
    .then(dataArray => {
        // console.log(dataArray)
        dataArray.forEach(element => {
            // console.log(element);
            let newdiv = document.createElement("div")
            newdiv.className = 'recommended_items'
            styling_div(newdiv);
            newdiv.innerHTML = `<img src="./images/${element[1]}" height: 100px width: 100px>
                                <p>${element[1]}</p>
                                <p> Brand : ${element[3]}</p>
                                <p>Price : ${element[2]}</p>`;
            recommendations.appendChild(newdiv);
            // console.log(element[1])
        });
    })
    .catch(error => {
        console.log("Error", error)
    });

function styling_div(div) {
    div.style.border = '2p solid green';
    div.style.maxWidth = '500px';
    div.style.width = '20vw';
    div.style.height = '20vh'
}

