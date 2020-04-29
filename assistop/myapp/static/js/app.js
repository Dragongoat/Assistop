$(document).foundation();

$('[data-app-dashboard-toggle-shrink]').on('click', function(e) {
    e.preventDefault();
    $(this).parents('.app-dashboard').toggleClass('shrink-medium').toggleClass('shrink-large');
});

function hotspotCP() {
    window.open('http://assistop.local:8080')
}

function openForm(address) {
    document.getElementById("popupForm_" + address).style.display = "block";
}

function closeForm(address) {
    document.getElementById("popupForm_" + address).style.display = "none";
}

// closes the panel on click outside
$(document).mouseup(function(e) {
    $('.form-popup').each(function(i, obj) {
        var container = $('.form-popup');
        if (!container.is(e.target) // if the target of the click isn't the container...
            &&
            container.has(e.target).length === 0) // ... nor a descendant of the container
        {
            container.css("display", "none");
        }
    });
});