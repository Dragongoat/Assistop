$(document).foundation();

$('[data-app-dashboard-toggle-shrink]').on('click', function(e) {
    e.preventDefault();
    $(this).parents('.app-dashboard').toggleClass('shrink-medium').toggleClass('shrink-large');
  });
  
function hotspotCP() {
  window.open('http://assistop.local:8080')
}