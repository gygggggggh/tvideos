const buttons = document.querySelectorAll(".click-btn");

function animate(buttons) {
    button.classList.add("clicked");
    
    // Create an animated circle element
    const circle = document.createElement("div");
    circle.classList.add("circle");
    button.appendChild(circle);
    
    // Get the center point of the button element
    const rect = button.getBoundingClientRect();
    const centerX = rect.x + rect.width / 2;
    const centerY = rect.y + rect.height / 2;
    
    // Set the circle element's initial position and size
    circle.style.left = centerX + "px";
    circle.style.top = centerY + "px";
    circle.style.width = "0";
    circle.style.height = "0";
    
    // Animate the circle element's size and opacity
    const animation = circle.animate([
      { width: "0", height: "0", opacity: "1" },
      { width: "100px", height: "100px", opacity: "0" }
    ], {
      duration: 500,
      easing: "ease-out"
    });
    
    // Remove the circle element after the animation is complete
    animation.onfinish = () => {
      circle.remove();
    };
    
    // Remove the "clicked" class after a short delay
    setTimeout(() => {
      button.classList.remove("clicked");
    }, 500);
  }