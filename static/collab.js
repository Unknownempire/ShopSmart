// let collab_recom = document.getElementById('collab_recommendations');
// console.log('helloooooo collab js ')
// // console.log("dataarray: ")
// // console.log(dataArray)
// // console.log(collab_recom)
// fetch('http://127.0.0.1:5000/UserSim') 
//     .then(response => response.json())
//     .then(dataArray => {
//         console.log("dataarray: ")
//         console.log(dataArray)
//         dataArray.forEach(element => {
//             // console.log(element);
//             let newdiv = document.createElement("div")
//             newdiv.className = 'recommended_items'
//             styling_div(newdiv);
         

//         let img = document.createElement("img");
//         img.src =`../static/images/` + element[1]+`.jpg`
//         img.className="recommendation_img"
//         // Use the image URL provided by Flask
//         img.alt = element[1]+" img";

//          // Use the image URL provided by Flask
//         let imageLoaded = false; // Add a flag to track whether the image has loaded successfully
//         img.alt = element[1]+" img";
        
//         function handleImageError() {
//             if (!imageLoaded) {
//             imageLoaded = true;
//             img.src =`../static/images/` + element[1]+`.webp`
//             console.log("image source change")
//             }
//         }
//         img.addEventListener('error', handleImageError);
//         img.addEventListener('load', () => {
//             imageLoaded = true;
//         });
        



//         newdiv.appendChild(img);


//         // Create paragraphs for text content
//         let p1 = document.createElement("span");
//         p1.textContent = element[1];
//         let p2 = document.createElement("p");
//         p2.textContent = '₹ ' + element[2];
//         let p3 = document.createElement("span");
//         p3.textContent = element[3] + " ";
//         // Append the text paragraphs to the new div
//         newdiv.appendChild(p3);
//         newdiv.appendChild(p1);
//         newdiv.appendChild(p2);



//             recommendations.appendChild(newdiv);
//             // console.log(element[1])
//         });
//     })
//     .catch(error => {
//         console.log("Error", error)
//     });

document.addEventListener('DOMContentLoaded', () => {
    const collabRecommendations = document.getElementById('collab_recommendations');

    fetch('http://127.0.0.1:5000/UserSim')
        .then(response => response.json())
        .then(dataArray => {
            console.log('dataArray:', dataArray); // Log the fetched data for inspection
            if (typeof dataArray === 'string') {
                dataArray = JSON.parse(dataArray); // Parse the string into a JavaScript object
            }

            if (Array.isArray(dataArray)) {
                // Clear any previous content
                collabRecommendations.innerHTML = '';

                // Iterate through the dataArray and create elements for each item
                dataArray.forEach(element => {
                    // ... create product elements as before ...
                });
            } else {
                console.error('Invalid data format 2:', typeof(dataArray));
            }
        })
        .catch(error => {
            console.error('Error fetching recommendations:', error);
        });
});
