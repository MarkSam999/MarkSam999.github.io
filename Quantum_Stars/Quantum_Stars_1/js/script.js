function toggleMenu() {
    const navigation_links = document.getElementById('navigation_links');
    if (navigation_links.style.display === 'flex') {
        navigation_links.style.display = 'none';
    } else {
        navigation_links.style.display = 'flex';
    }
}