let user_recom = document.getElementById('collab_recommendations')
function user_similarity() {fetch('https://shopsmart-cvl1.onrender.com/UserSim') 
    .then(response => response.json())
    .then(dataArray => {
        // console.log(dataArray)
        dataArray.forEach((element) => {
          console.log(element);
          let newdiv = document.createElement("div");
          newdiv.className = "user_sim";
          styling_div(newdiv);

          let img = document.createElement("img");
          img.src = `../static/images/` + element[1] + `.jpg`;
          img.className = "recommendation_img";
          // Use the image URL provided by Flask
          img.alt = element[1] + " img";

          // Use the image URL provided by Flask
          let imageLoaded = false; // Add a flag to track whether the image has loaded successfully
          img.alt = element[1] + " img";

          function handleImageError() {
            if (!imageLoaded) {
              imageLoaded = true;
              img.src = `../static/images/` + element[1] + `.png`;
              // console.log("image source change")
            }
          }
          if (element[1] == "Rolls/buns") {
            img.src = `../static/images/Rolls_buns.webp`;
          }

          img.addEventListener("error", handleImageError);
          img.addEventListener("load", () => {
            imageLoaded = true;
          });

          newdiv.appendChild(img);

          // Create paragraphs for text content
          let p1 = document.createElement("span");
          p1.textContent = element[1];
          let p2 = document.createElement("p");
          p2.textContent = "₹ " + element[2];
          let p3 = document.createElement("span");
          p3.textContent = element[3] + " ";
          // Append the text paragraphs to the new div
          newdiv.appendChild(p3);
          newdiv.appendChild(p1);
          newdiv.appendChild(p2);

          user_recom.appendChild(newdiv);
          let add_to_cart = document.createElement("button");
          add_to_cart.innerHTML = "Add To Cart";
          add_to_cart.className = "addToCart"

          // 2. Append somewhere
          newdiv.appendChild(add_to_cart);

          // 3. Add event handler
          add_to_cart.addEventListener("click", function () {
            alert("did something");
          });
          // console.log(element[1])
        });
    })
    .catch(error => {
        console.log("Error", error)
    })};
    // Get Recommendations on page load
    user_similarity();