var my_func = function(event) {
    event.preventDefault();
};

// your form
var form = document.getElementsByTagName('form');

// attach event listener
form.forEach( f => {
    f.addEventListener("submit", my_func, true);
})
