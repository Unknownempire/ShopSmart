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
       


        browsed_product.append(newdiv);
        let img = document.createElement("img");
        img.src =`../static/images/` + element[1]+`.jpg`
        img.className="browsed_product_img"
        // Use the image URL provided by Flask
        img.alt = element[1]+" img";

        newdiv.appendChild(img);


        // Create paragraphs for text content
        let p1 = document.createElement("p");
        p1.textContent = element[1];
        let p2 = document.createElement("p");
        p2.textContent = element[2];
        // Append the text paragraphs to the new div
        newdiv.appendChild(p1);
        newdiv.appendChild(p2);

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
         

        let img = document.createElement("img");
        img.src =`../static/images/` + element[1]+`.jpg`
        img.className="recommendation_img"
        // Use the image URL provided by Flask
        img.alt = element[1]+" img";

         // Use the image URL provided by Flask
        let imageLoaded = false; // Add a flag to track whether the image has loaded successfully
        img.alt = element[1]+" img";
        
        function handleImageError() {
            if (!imageLoaded) {
            imageLoaded = true;
            img.src =`../static/images/` + element[1]+`.webp`
            console.log("image source change")
            }
        }
        img.addEventListener('error', handleImageError);
        img.addEventListener('load', () => {
            imageLoaded = true;
        });
        



        newdiv.appendChild(img);


        // Create paragraphs for text content
        let p1 = document.createElement("span");
        p1.textContent = element[1];
        let p2 = document.createElement("p");
        p2.textContent = '₹ ' + element[2];
        let p3 = document.createElement("span");
        p3.textContent = element[3] + " ";
        // Append the text paragraphs to the new div
        newdiv.appendChild(p3);
        newdiv.appendChild(p1);
        newdiv.appendChild(p2);



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
