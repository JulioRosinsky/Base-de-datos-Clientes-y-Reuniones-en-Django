window.addEventListener('beforeunload', function() {
    document.cookie = "csfrtoken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    fetch('/logout', { method: 'POST' });
});
