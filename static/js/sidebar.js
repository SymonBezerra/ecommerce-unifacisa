function sidebar() {
    return {
        logout: async function () {
            const response = await fetch('/login/logout', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            if (response.ok) {
                window.location.href = '/login';
            } else {
                alert('Logout failed. Please try again.');
            }
        }
    }
}