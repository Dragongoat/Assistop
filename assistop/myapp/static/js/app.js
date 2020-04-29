$(document).foundation();

$('[data-app-dashboard-toggle-shrink]').on('click', function(e) {
    e.preventDefault();
    $(this).parents('.app-dashboard').toggleClass('shrink-medium').toggleClass('shrink-large');
});

function hotspotCP() {
    window.open('http://assistop.local:8080')
}

function openForm() {
    document.getElementById("popupForm").style.display = "block";
}

function closeForm() {
    document.getElementById("popupForm").style.display = "none";
}

// closes the panel on click outside
$(document).mouseup(function(e) {
    var container = $('#popupForm');
    if (!container.is(e.target) // if the target of the click isn't the container...
        &&
        container.has(e.target).length === 0) // ... nor a descendant of the container
    {
        document.getElementById("popupForm").style.display = "none";
    }
});